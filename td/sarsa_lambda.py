'''
    created on 01 January 2020
    
    @author: Gergely
'''
import operator
import random

from environment.env import Easy21Action, init_state, step


def player_policy(state, q, epsilon=1e-1):
    action_values = q[state] if state in q else Easy21Action.to_action_map()
    if random.random() > epsilon / 2 + 1 - epsilon:
        return random.choice(list(action_values.keys()))
    return max(action_values.items(), key=operator.itemgetter(1))[0]
    # return Easy21Action.HIT if state.player_sum < 17 else Easy21Action.STICK


def sarsa_lambda(nr_episodes=800000, gamma=0.99, alpha=0.1, lam=0.1):
    q = {}
    for episode in range(nr_episodes):
        eligibility_traces = {}
        state = init_state()
        action = player_policy(state, q)
        while True:
            s_prime, done, reward = step(state, action)
            a_prime = player_policy(s_prime, q)
            if state not in q:
                q[state] = Easy21Action.to_action_map()
            if s_prime not in q:
                q[s_prime] = Easy21Action.to_action_map()
            if state not in eligibility_traces:
                eligibility_traces[state] = Easy21Action.to_action_map()

            delta = reward + gamma * q[s_prime][a_prime] - q[state][action]
            eligibility_traces[state][action] += 1
            for s in q:
                for a in Easy21Action.to_action_map():
                    q[s][a] += alpha * delta * eligibility_traces[s][a]
                    eligibility_traces[s][a] = gamma * lam * eligibility_traces[s][a]

            state = s_prime
            action = a_prime
            if done:
                break
