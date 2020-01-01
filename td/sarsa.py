'''
    created on 31 December 2019
    
    @author: Gergely
'''

from environment.env import (step, Easy21Action, init_state, Easy21State)
from td.epsilon_greedy import epsilon_greedy_player_policy


def sarsa(nr_episodes=8000000, alpha=0.01, gamma=0.99):
    q = {}
    for episode in range(nr_episodes):
        if episode % 10000 == 0:
            print(f'{episode} episodes run')
            if Easy21State(dealer_card=5, player_sum=20) in q:
                print(q[Easy21State(dealer_card=5, player_sum=20)])
        state = init_state()
        action = epsilon_greedy_player_policy(state, q)
        while True:
            s_prime, done, reward = step(state, action)
            a_prime = epsilon_greedy_player_policy(s_prime, q)
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
