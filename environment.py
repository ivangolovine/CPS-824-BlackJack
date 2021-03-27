from player.py import Player

class Environment:
    def __init__(self, agent, dealer):
        self.agent = agent
        self.dealer = dealer
        self.dealer_thresh = 17
        self.bust_thresh = 21

    def state(self):
        return self.player.get_hand_value(), self.dealer.get_faceup_card_value()

    def reset(self):
        self.agent.hand_reset()
        self.dealer.hand_reset()

    def step(self, action):
        if action == 0:
            self.player.hit()
        elif action == 1:
            self.player.stay()
        state = self.state()
        done = (action == 1) or (self.player.get_hand_value() > bust_thresh)
        reward = self.reward(self, state, done)
        return state, reward, done

    def episode_reward(self, state, done):
        if not done:
            return 0
        while self.dealer.get_hand_value() < self.dealer_thresh():
            self.dealer.hit()
        
        player_bust = self.player.get_hand_value() > self.bust_thresh()
        dealer_bust = self.dealer.get_hand_value() > self.bust_thresh()

        if player_bust:
            return -1
        if not player_bust and dealer_bust:
            return 1

        if self.player.get_hand_value() == self.dealer.get_hand_value():
            return 0 
        if self.player.get_hand_value() > self.dealer.get_hand_value():
            return 1
        if self.player.get_hand_value() < self.dealer.get_hand_value():
            return -1