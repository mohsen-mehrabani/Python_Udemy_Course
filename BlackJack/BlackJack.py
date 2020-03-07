
import random
try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ["hearts", "clubs", "diamonds", "spades"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    # For each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards from 1 to 10
        for card in range(1, 11):
            name = 'playing_cards/png/{}_of_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))
        # next the face cards
        for card in face_cards:
            name = 'playing_cards/png/{}_of_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


def deal_card(frame):
    # pop the next card of the top of the deck
    next_card = deck.pop(0)
    # add the image to the end of the doc
    deck.append(next_card)
    # add the image to the label and dis
    # play it
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the score of all cards in the list.
    # Only one ace can have the value of 11 and this will be reduced 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract to 10
        if score > 21 and ace:
            score -= 10
            ace = 10
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Player wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


def new_game():
    global player_card_frame
    global dealer_card_frame
    global player_hand
    global dealer_hand
    # Embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    # Embedded frame hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")
    # create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    deal_dealer()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


if __name__ == "__main__":
    mainWindow = tkinter.Tk()
    # Ste up the screen and frames for the dealer and player
    mainWindow.title("Black Jack")
    mainWindow.geometry("1080x420")
    mainWindow.resizable(True, True)
    mainWindow.config(background='green')

    result_text = tkinter.StringVar()
    result = tkinter.Label(mainWindow, textvariable=result_text)
    result.grid(row=0, column=0, columnspan=3)

    card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
    card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

    # Embedded frame hold the card images
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_score_label = tkinter.IntVar()
    # player_score = 0
    # player_ace = False
    tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

    # Embedded frame hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    button_frame = tkinter.Frame(mainWindow)
    button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

    dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
    dealer_button.grid(row=0, column=0)

    player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
    player_button.grid(row=0, column=1)

    new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
    new_game_button.grid(row=0, column=2)

    shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
    shuffle_button.grid(row=0, column=3)

    # load cards
    cards = []
    load_images(cards)
    print(cards)

    # create a new deck of cards and shuffle them
    deck = list(cards) + list(cards) + list(cards)
    shuffle()

    # create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    new_game()

    mainWindow.mainloop()