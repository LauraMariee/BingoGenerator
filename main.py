from number import *
from card import Card


def main():
    x = Number
    print(x.getDescription(34))

    # load the numbers
    numbers = Number.loadNumbers()

    # create a bingo card with some numbers on it
    card = Card(height=3, width=5)
    card.put_number(0, 0, numbers[12])
    card.put_number(0, 1, numbers[63])
    card.put_number(0, 2, numbers[25])
    card.put_number(0, 3, numbers[90])
    card.put_number(0, 4, numbers[32])
    card.put_number(1, 0, numbers[13])
    card.put_number(1, 1, numbers[14])
    card.put_number(1, 2, numbers[15])
    card.put_number(1, 3, numbers[16])
    card.put_number(1, 4, numbers[17])
    card.put_number(2, 0, numbers[87])
    card.put_number(2, 1, numbers[65])
    card.put_number(2, 2, numbers[4])
    card.put_number(2, 3, numbers[54])
    card.put_number(2, 4, numbers[32])

    # show the card
    print("Your bingo card:")
    card.pretty_print()

    # the caller randomly calls out the number 13 (chosen by fair dice roll)
    called_number = numbers[13]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 10 (chosen by fair dice roll)
    called_number = numbers[10]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 14 (chosen by fair dice roll)
    called_number = numbers[14]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 54 (chosen by fair dice roll)
    called_number = numbers[54]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 15 (chosen by fair dice roll)
    called_number = numbers[15]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 17 (chosen by fair dice roll)
    called_number = numbers[17]
    print(called_number.description)
    card.mark_number(called_number)

    # the caller randomly calls out the number 16 (chosen by fair dice roll)
    called_number = numbers[16]
    print(called_number.description)
    card.mark_number(called_number)

    # surprise, looks like we won!
    if card.check():
        print("You win!")
    else:
        print("BAd luck - maybe next time...")

    # Show the card again with the crossed out fields
    card.pretty_print()


if __name__ == "__main__":
    main()
