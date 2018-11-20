# Import random


class Deck:
    """
    52 cards in a set
    """

    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = list("Clubs","Hearts","Diamonds","Spades")

    def __init__(self,rank,suit):
        self._cards = [52]  # Your code goes inside the listcomp
        if self.ranks == "Ace":
            return 1
        if self.ranks =="Joker":
             return 11
        if self.ranks == "Queen":
            return 12
        if self.ranks == "King":
            return 13

    def __repr__(self):
        pass

    def __len__(self):
        return len(self._cards)

    def deal(self):
        for suits in rank:
          cards.append((rank,suit))
          random.shuffle(cards)
