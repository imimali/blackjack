'''
    created on 30 December 2019
    
    @author: Gergely
'''
from environment.env import (step,
                             init_state,
                             Easy21State,
                             Easy21Action)

from collections import namedtuple

StateActionPair = namedtuple('StateActionPair', 'state action')


def player_policy(state, q):
    action_values = {pair.action: q[pair] for pair in q if pair.state == state}
    max_action = Easy21Action.HIT
    max_action_value = 0
    for action in action_values:
        if action_values[action] > max_action_value:
            max_action_value = action_values[action]
            max_action = action
    return max_action


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


def monte_carlo(nr_episodes=100):
    visits = {}
    q = {}
    for _ in range(nr_episodes):
        print(len(q))
        episode = sample_episode(q)
        final_reward = episode[-1][2]
        for sample in episode:
            pair = StateActionPair(sample[0], sample[1])
            visits[pair] = 1 if pair not in visits else visits[pair] + 1
            q[pair] = (final_reward / visits[pair]
                       if pair not in q
                       else q[pair] + (final_reward - q[pair]) / visits[pair])


monte_carlo()
