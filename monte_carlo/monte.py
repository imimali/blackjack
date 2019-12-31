'''
    created on 30 December 2019
    
    @author: Gergely
'''
import operator

from environment.env import (step,
                             init_state,
                             Easy21Action)

from collections import namedtuple

StateActionPair = namedtuple('StateActionPair', 'state action')


def player_policy(state, q):
    action_values = q[state] if state in q else Easy21Action.to_action_map()
    return max(action_values.items(), key=operator.itemgetter(1))[0]
    # return Easy21Action.HIT if state.player_sum < 17 else Easy21Action.STICK


def sample_episode(q):
    state = init_state()
    episode = []
    while True:
        action = player_policy(state, q)
        next_state, done, reward = step(state, action)
        episode.append((state, action, reward, next_state, done))
        state = next_state
        if done:
            return episode


def monte_carlo(nr_episodes=50000):
    visits = {}
    q = {}
    for _ in range(nr_episodes):
        episode = sample_episode(q)
        final_reward = episode[-1][2]
        for sample in episode:
            state = sample[0]
            action = sample[1]
            if state not in visits:
                visits[state] = Easy21Action.to_action_map()
            visits[state][action] += 1
            if state not in q:
                q[state] = Easy21Action.to_action_map()
            q[state][action] = (q[state][action] + (final_reward - q[state][action]) /
                                visits[state][action])

    return q


qs = monte_carlo()
for q in qs:
    print(q,qs[q])
