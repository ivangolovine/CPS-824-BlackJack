import numpy as np
from cards.py import *
from player.py import *
from environment.py import *

def sample_action(policy, state):
    nS, nA = policy.shape
    all_actions = np.arange(nA)
    return np.random.choice(all_actions, p=policy[state])

def take_one_step(env, policy, state):
    action = sample_action(policy, state)
    new_state, reward, done, _ = env.step(action)
    return action, reward, new_state, done

def generate_episode(env, policy):
    episode = []
    curr_state = env.reset()
    done = False
    while not done:
        action, reward, new_state, done = take_one_step(env, policy, curr_state)
        episode.append((curr_state, action, reward))
        curr_state = new_state
    return episode