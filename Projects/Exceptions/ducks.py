class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print(f"Wee, this is fun")
        elif self.ratio == 1:
            print(f"This is hard work, but I'm flying")
        else:
            print(f"I think I''l just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle , Waddle, Waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack, Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print(" Waddle, Waddle, I waddle too")

    def swim(self):
        print("Come on it, but it's a bit chilly this fo South")

    def quack(self):
        print("Are you 'avin' a larf, I'm a Penguin!")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        self.flock.append(duck)

    def migrate(self):
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError:
                print("One duck down")




if __name__ == '__main__':
    donald = Duck()
    donald.fly()
