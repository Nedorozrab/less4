from kurka import Chicken

class Chick(Chicken):
    def __init__(self, feathers_color: str, legs: int):
        super().__init__(feathers_color, legs)
        self.size = "маленька"

    def peep(self):
        return "пі пі пі пі!"

    def describe(self):
        return f"A {self.size} курча з {self.feathers_color} із пір'ям {self.legs} ноги."
