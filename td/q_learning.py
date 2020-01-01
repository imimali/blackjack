'''
    created on 01 January 2020
    
    @author: Gergely
'''

from environment.env import (step, Easy21Action, init_state)
from td.epsilon_greedy import epsilon_greedy_player_policy


def q_learning(nr_episodes=800000, alpha=0.01, gamma=0.99):
    q = {}
    for episode in range(nr_episodes):
        state = init_state()
        while True:
            action = epsilon_greedy_player_policy(state, q)
            s_prime, done, reward = step(state, action)
            if state not in q:
                q[state] = Easy21Action.to_action_map()
            if s_prime not in q:
                q[s_prime] = Easy21Action.to_action_map()
            q[state][action] += alpha * (reward + gamma * max(q[s_prime].values()) - q[state][action])
            state = s_prime
            if done:
                break
