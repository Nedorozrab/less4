from kurka import Chicken
from ciplatko import Chick

def main():
    chicken = Chicken("коричновий", 2)
    print(chicken.describe())
    print(chicken.cluck())

    chick = Chick("жовтий", 2)
    print(chick.describe())
    print(chick.peep())

if __name__ == "__main__":
    main()
