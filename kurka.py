class Chicken:
    def __init__(self, feathers_color: str, legs: int):
        self.feathers_color = feathers_color
        self.legs = legs
        self.size = "велика"

    def cluck(self):
        return "курлик курлик!"

    def describe(self):
        return f"A {self.size} курча з {self.feathers_color} пір'я з {self.legs} ноги."
