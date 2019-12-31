'''
    created on 30 December 2019
    
    @author: Gergely
'''
import operator
import random
from environment.env import (step,
                             init_state,
                             Easy21Action)


def player_policy(state, q, state_visits):
    action_values = q[state] if state in q else Easy21Action.to_action_map()
    epsilon_t = 100 / (100 + state_visits)
    if random.random() > epsilon_t / 2 + 1 - epsilon_t:
        return random.choice(list(action_values.keys()))
    return max(action_values.items(), key=operator.itemgetter(1))[0]
    # return Easy21Action.HIT if state.player_sum < 17 else Easy21Action.STICK


def sample_episode(q, visits):
    state = init_state()
    episode = []
    while True:
        state_visits = 0 if not state in visits else sum(visits[state].values())
        action = player_policy(state, q, state_visits)
        next_state, done, reward = step(state, action)
        episode.append((state, action, reward, next_state, done))
        state = next_state
        if done:
            return episode


def monte_carlo(nr_episodes=800000):
    visits = {}
    q = {}
    for _ in range(nr_episodes):
        episode = sample_episode(q, visits)
        final_reward = episode[-1][2]
        # print('final reward is',final_reward)
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
print(len(qs))
for q in qs:
    pass
    print(q, qs[q])
