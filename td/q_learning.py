'''
    created on 01 January 2020
    
    @author: Gergely
'''
import operator
import random

from environment.env import (step, Easy21Action, init_state)


def player_policy(state, q, epsilon=1e-1):
    action_values = q[state] if state in q else Easy21Action.to_action_map()
    if random.random() > epsilon / 2 + 1 - epsilon:
        return random.choice(list(action_values.keys()))
    return max(action_values.items(), key=operator.itemgetter(1))[0]
    # return Easy21Action.HIT if state.player_sum < 17 else Easy21Action.STICK


def q_learning(nr_episodes=800000, alpha=0.9, gamma=0.99):
    q = {}
    for episode in range(nr_episodes):
        state = init_state()
        while True:
            action = player_policy(state, q)
            s_prime, done, reward = step(state, action)
            if state not in q:
                q[state] = Easy21Action.to_action_map()
            if s_prime not in q:
                q[s_prime] = Easy21Action.to_action_map()
            q[state][action] += alpha * (reward + gamma * max(q[s_prime].values()) - q[state][action])
            state=s_prime
            if done:
                break
