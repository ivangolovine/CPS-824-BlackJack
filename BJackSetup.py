import numpy as np
import random


class Environment:

    def __init__(self):
        self.dealer_sum = 0  # Stores dealer hand total
        self.player_sum = 0  # Stores Player hand total
        self.dealer_cards = []  # Stores the dealer cards
        self.player_cards = []  # Stores the player cards
        self.deck = []  # Stores the deck
        self.ace = 1  # Checks if an ace is usable
        self.first = True  # checks for natural blackJack

    def cmp(self, a, b):
        return float(a > b) - float(a < b)

    def fill_deck(self):
        self.deck = []
        for i in range(0, 52):
            value = i
            self.deck.append(value % 13)  # makes them all 1 - 13
            random.shuffle(self.deck)  # shuffle the deck

    def get_hands(self):
        for i in range(0, 2):
            self.player_cards.append(self.deck.pop())
            self.dealer_cards.append(self.deck.pop())

    def get_card_VAL(self, card):
        if card > 9:
            return 10
        else:
            return card

    def add_CardVal(self, hand):
        sum_hand = 0
        for card in hand:
            if card != 0:
                sum_hand += self.get_card_VAL(card)
        for card in hand:
            if card == 0:
                if sum_hand + 11 <= 21:
                    sum_hand += 11
                    self.ace = 1
                else:
                    sum_hand += 1
                    self.ace = 0
        return sum_hand

    def hit_player(self):
        self.player_cards.append(self.deck.pop())

    def hit_dealer(self):
        self.dealer_cards.append(self.deck.pop())

    def hand_bust(self, hand):
        return self.get_card_VAL(hand) > 21

    def Player_total(self):
        self.player_sum = self.add_CardVal(self.player_cards)
        return self.player_sum

    def Dealer_total(self):
        self.dealer_sum = self.add_CardVal(self.dealer_cards)
        return self.dealer_sum

    def reset(self):  # start game
        self.deck = []
        self.player_cards = []
        self.dealer_cards = []
        self.player_sum = 0
        self.dealer_sum = 0
        self.fill_deck()
        self.get_hands()
        self.dealer_sum = self.add_CardVal(self.dealer_cards)
        self.player_sum = self.add_CardVal(self.player_cards)
        # print("dealer bob", self.dealer_sum)
        # print("player sam", self.player_sum)
        ##print(self.Player_total())
        # print(self.dealer_cards[0])
        return (self.Player_total(), self.dealer_cards[0], self.ace), 0, False

    def step(self, action):
        if self.Player_total() == 21 and self.first:
            if self.Dealer_total() != 21:
                return (21, self.dealer_cards[0], self.ace), +1.5, True
            self.first = False
        if action == 1:  #Hit
            self.hit_player()
            if self.hand_bust(self.Player_total()):
                done = True
                reward = -1.
            else:
                done = False
                reward = 0
        else:  # Stay
            done = True
            while self.Dealer_total() < 17:
                self.hit_dealer()
            reward = self.cmp(self.Player_total(), self.Dealer_total())
        return (self.Player_total(), self.dealer_cards[0], self.ace), reward, done

    def tester(self):  # testing methods
        self.fill_deck()
        print(len(self.deck))
        for i in range(4):
            print(self.deck[i])

        self.get_hands()
        print("player cards = ", self.player_cards)
        print("dealer cards = ", self.dealer_cards)

        self.dealer_sum = self.add_CardVal(self.player_cards)
        self.player_sum = self.add_CardVal(self.dealer_cards)
        print("player sum = ", self.dealer_sum)
        print("dealer sum = ", self.player_sum)

        print(len(self.deck))

        self.hit_player()
        print(self.player_cards)
        print(self.step(1))
        print(self.step(0))

        print(self.reset())
        print(self.player_sum)
        print(self.dealer_sum)
        print(self.step(1))
        print(self.step(0))
        print(self.player_sum)
        print(self.dealer_sum)
        print(self.reset())
        self.hit_player()
        self.hit_dealer()
        print(self.player_cards)
        print(self.dealer_cards)


a = Environment()
b = a.tester()
