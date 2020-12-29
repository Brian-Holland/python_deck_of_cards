from random import shuffle

#card instance should have suit
#card instance should have value
#card repr should display value and suit

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"


#deck instance should have card attr with all 52 combinations
#deck instance method count to show remaining number of cards indeck
#dek repr should display how many cards in deck
#deck instance method called _deal. Accepts number of cards and removes that many from deck
#deck instance method called shuffle. Shuffles ONLY full decks
#deck instance method called deal_card. Uses _deal to deal single card
#deck instance method called deal_hand. Accepts number and uses _deal to deal list of cards and return list of cards

class Deck:
    def __init__(self):
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]
        
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count() 

        if count == 0:
            raise ValueError("All cards have been dealt")

        num_cards_to_remove = min([count,num])

        print(f"Removing {num_cards_to_remove} cards")

        cards = self.cards[-num_cards_to_remove:]

        self.cards = self.cards[:-num_cards_to_remove]

        return cards

    def shuffle(self):
        count = self.count()

        if count != 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)

        return self
            
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


