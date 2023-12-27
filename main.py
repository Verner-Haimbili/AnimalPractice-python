class Goat:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Goat: name = {self.name}, color = {self.color}, price = {self.price}"


class App:
    @staticmethod
    def main():
        g1 = Goat("Kamela", "White", 900)
        print(g1)


# Run app
App.main()

