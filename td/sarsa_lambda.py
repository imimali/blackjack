'''
    created on 01 January 2020
    
    @author: Gergely
'''

from environment.env import Easy21Action, init_state, step
from td.epsilon_greedy import epsilon_greedy_player_policy


def sarsa_lambda(nr_episodes=800000, gamma=0.99, alpha=0.01, lam=0.1):
    q = {}
    for episode in range(nr_episodes):
        eligibility_traces = {}
        state = init_state()
        action = epsilon_greedy_player_policy(state, q)
        while True:
            s_prime, done, reward = step(state, action)
            a_prime = epsilon_greedy_player_policy(s_prime, q)
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
