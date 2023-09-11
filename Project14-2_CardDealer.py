import random

#Card class
class Card:
    ranks = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    def __init__(self):
        pass

    #method to get string
    def string(self, num):
        string = ""
        if 1 <= num <= 13:
            string = self.ranks[num] + " of " + self.suits[0]
        elif 14 <= num <= 26:
            string = self.ranks[(num % 13) + 1] + " of " + self.suits[1]
        elif 17 <= num <= 39:
            string = self.ranks[(num % 13) + 1] + " of " + self.suits[2]
        elif 40 <= num <= 52:
            string = self.ranks[(num % 13) + 1] + " of " + self.suits[3]
        return string

#deck class to store 52 cards
class Deck:
    numbers = list(range(1,53))
    def __init__(self):
        self.shuffle()
        print("I have shuffled a deck of 52 careds.\n")

    #method to shuffle deck
    def shuffle(self):
        random.shuffle(self.numbers)
    #method to count number of cards in deck
    def count(self):
        return len(self.numbers)
    #method to deal card from deck
    def deal(self):
        self.shuffle()
        num = random.choice(self.numbers)
        self.numbers.remove(num)
        c = Card()
        x = c.string(num)
        return x

def main():
    print("Card Dealer\n")

    d = Deck()
    card_num = int(input("How mmany cards would you like?: "))
    print("\nHere are your cards:")
    for i in range(1, card_num + 1):
        print(d.deal())
    print("\nThere are", d.count(), "cards left in the deck.\n")
    print("Good luck!")

if(__name__ == "__main__"):
    main()