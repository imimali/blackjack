'''
    created on 31 December 2019
    
    @author: Gergely
'''
from environment.env import (step, Easy21Action, init_state)


def sarsa(nr_episodes=80000):
    q = {}
    for _ in range(nr_episodes):
        state = init_state()

