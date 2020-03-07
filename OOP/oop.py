class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


Kenwood = Kettle("Kenwood", 8.99)
print(Kenwood.make)
print(Kenwood.price)

Kenwood.price = 12.99
print(Kenwood.price)

Hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(Kenwood.make, Kenwood.price, Hamilton.make, Hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Kenwood, Hamilton))

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics.
Object: An instance of a class.
Instantiate: Create an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to an instance of a class.
"""
print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)

Kettle.switch_on(Kenwood)
print(Kenwood.on)
Kenwood.switch_on()

print("*" * 60)
Kenwood.power = 1.5
print(Kenwood.power)
# print(Hamilton.power)
