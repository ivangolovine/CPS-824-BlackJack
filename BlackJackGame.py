import gym
import numpy as np
import matplotlib.pyplot as plt

#initialize environment
env = gym.make('Blackjack-v0')

#initialize variables
agentStates = [i for i in range(4, 22)]
dealerStates = [i+1 for i in range(10)]
agentAce = [False, True]
nA = 2
actions = [0, 1]
states = []
Q_value = {}
returns = {}
n_visits = {}
visit_flag_reset = {}
policy = {}
policy_reset = {}
epsilon = 1
gamma = 1 

#monte carlo functions
def sample_action(policy, state):
    return np.random.choice(actions, p=policy[state])

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

def generate_returns(episode, gamma):
    len_episode = len(episode)
    epi_returns = np.zeros(len_episode)
    rewards_arr = np.zeros(len_episode)
    gamma_arr = np.zeros(len_episode)
    for val in range(len(gamma_arr)):
        gamma_arr[val] = gamma**val
    for step in range(len(episode)):
        rewards_arr[step] = episode[step][2]
    for iter in range(len_episode):
        end = len(gamma_arr) - iter
        reward = np.dot(rewards_arr[iter:], gamma_arr[:end])
        epi_returns[iter] = reward
    return epi_returns

def mc_policy_evaluation(env, policy, Q_value, n_visits, gamma):
    episode = generate_episode(env, policy)
    episode_returns = generate_returns(episode, gamma)
    visit_flag = visit_flag_reset
    for i in range(len(episode)):
        step = episode[i]
        if visit_flag[step[0]][step[1]] == 0:
            n_visits[step[0]][step[1]] += 1
            Q_value[step[0]][step[1]] += (1/n_visits[step[0]][step[1]])*(episode_returns[i] - Q_value[step[0]][step[1]])
            visit_flag[step[0]][step[1]] = 1
    return Q_value, n_visits

def epsilon_greedy_policy_improve(Q_value, nA, epsilon):
    new_policy = policy_reset
    for total in agentStates:
        for card in dealerStates:
            for ace in agentAce:
                state = (total, card, ace)
                max_vals = np.argwhere(Q_value[state] == np.amax(Q_value[state]))
                max_vals = max_vals.flatten().tolist()
                for act in range(len(Q_value[state])):
                    if act in max_vals:
                        new_policy[state][act] = (1 - epsilon)/len(max_vals) + epsilon/nA
                    else:
                        new_policy[state][act] = epsilon/nA
    return new_policy



#create initial dictionaries of all states for Q_value, returns and visit_flag
'''
for total in agentStates:
    for card in dealerStates:
        for ace in agentAce:
            for action in actions:
                Q_value[((total, card, ace), action)] = 0
                rewards[((total, card, ace), action)] = 0
                n_visits[((total, card, ace), action)] = 0
                visit_flag_reset[((total, card, ace), action)] = 0
            states.append((total, card, ace))
            '''

for total in agentStates:
    for card in dealerStates:
        for ace in agentAce:
            Q_value[(total, card, ace)] = [0, 0]
            returns[(total, card, ace)] = [0, 0]
            n_visits[(total, card, ace)] = [0, 0]
            visit_flag_reset[(total, card, ace)] = [0, 0]
            states.append((total, card, ace))

#create inital policy where all actions have equal probability    
for state in states:
    policy[state] = [1/nA, 1/nA]
    policy_reset[state] = [1/nA, 1/nA]


#training of agent
iterations = 10000
counter = 0

while counter < iterations:
        Q_value, n_visits = mc_policy_evaluation(env, policy, Q_value, n_visits, gamma)
        policy = epsilon_greedy_policy_improve(Q_value, nA, epsilon)
        counter += 1
        epsilon = 1/counter

numGames = 1000
rewards = np.zeros(numGames)
totalReward = 0
wins = 0
losses = 0
draws = 0


print('getting ready to test policy')   
for i in range(numGames):
    curr_state = env.reset()
    done = False
    while not done:
        action, reward, new_state, done = take_one_step(env, policy, curr_state)
        curr_state = new_state
    totalReward += reward
    rewards[i] = totalReward

    if reward >= 1:
        wins += 1
    elif reward == 0:
        draws += 1
    elif reward == -1:
        losses += 1
    
wins /= numGames
losses /= numGames
draws /= numGames
print('win rate:', wins)
print('loss rate:', losses)
print('draw rate:', draws)
plt.plot(rewards)
plt.show()    
