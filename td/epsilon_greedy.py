'''
    created on 01 January 2020
    
    @author: Gergely
'''
import operator
import random

from environment.env import Easy21Action


def epsilon_greedy_player_policy(state, q, epsilon=1e-1):
    action_values = q[state] if state in q else Easy21Action.to_action_map()
    if random.random() > epsilon / 2 + 1 - epsilon:
        return random.choice(list(action_values.keys()))
    return max(action_values.items(), key=operator.itemgetter(1))[0]
    # return Easy21Action.HIT if state.player_sum < 17 else Easy21Action.STICK
