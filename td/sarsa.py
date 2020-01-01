'''
    created on 31 December 2019
    
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


def sarsa(nr_episodes=800000, alpha=0.9, gamma=0.99):
    q = {}
    for episode in range(nr_episodes):
        if episode % 10000 == 0:
            print(f'{episode} episodes run')
        state = init_state()
        action = player_policy(state, q)
        while True:
            s_prime, done, reward = step(state, action)
            a_prime = player_policy(s_prime, q)
            if state not in q:
                q[state] = Easy21Action.to_action_map()
            if s_prime not in q:
                q[s_prime] = Easy21Action.to_action_map()
            q[state][action] += alpha * (reward + gamma * q[s_prime][a_prime] - q[state][action])

            action = a_prime
            state = s_prime
            if done:
                break

    return {k: q[k] for k in q if 1 <= k.player_sum < 21}


qs = sarsa()

for q in qs:
    print(q, qs[q])
print(len(qs))
