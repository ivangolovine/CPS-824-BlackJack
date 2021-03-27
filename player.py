from cards.py import card

class Player:
    def __init__(self)
        self.hand = []
        self.stay = False

    def take_card(self, deck):
        self.hand.append(deck.pop)

    def reset_hand(self):
        self.hand = []

    #for agent
    def get_hand_value(self):
        handValue = 0
        for card in hand:
            handValue += card.get_card_value()
        return handvalue
    
    #for dealer
    def get_faceup_card_value(self):
        return self.hand[1].get_card_value()
    
    def stay(self):
        self.stay = True

    def hit(self):
        self.take_card(card)

    

                
    
    