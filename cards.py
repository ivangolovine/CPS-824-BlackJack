class Card:
    card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    def __init__(self, value):
        self.value = value
        self.card = cards[(self.value % 13)]
        self.card_value = card_values[self.card]
        self.visible = False

        if self.value < 13:
            self.suit = "Hearts"
        elif self.value < 26:
            self.suit = "Spades"
        elif self.value < 26:
            self.suit = "Diamonds"
        elif self.value < 52:
            self.suit = "Clubs"

    def get_card(self):
        return self.card
    
    def get_suit(self):
        return self.suit

    def get_card_value(self):
        return self.card_value

    def get_visibility(self):
        return self.visible

    def set_visibility(self, visible):
        self.visible = visible

    def print_card(self):
        print(self.card + " " + self.suit + ", " + str(self.visible))

#arrays/dictionarys for card class
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = {"0":"Hearts", "1":"Spades", "2":"Diamonds", "3":"Clubs"}
card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

#deck creation
deck = []

#adding cards to deck
for i in range(52):
    deck.append(Card(i))

#testing cards are working
for card in deck:
    card.print_card()

#creation of agent and dealer hands
agent_hand = []
dealer_hand = []

