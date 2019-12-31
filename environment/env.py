'''
    created on 29 December 2019
    
    @author: Gergely
'''

import random
from collections import namedtuple
from enum import Enum

Easy21State = namedtuple('Easy21State', 'dealer_card player_sum')


# Easy21State.__hash__ = lambda state: state.dealer_card + state.player_sum


class Easy21Action(Enum):
    HIT = 'hit'
    STICK = 'stick'

    @staticmethod
    def to_action_map():
        return {e.value: 0 for e in Easy21Action}


def dealer_policy(dealer_sum):
    return Easy21Action.HIT.value if dealer_sum < 17 else Easy21Action.STICK.value


def _sample_card():
    card_number = random.randint(1, 10)
    card_color = -1 if random.random() < 1 / 3 else 1
    return card_color * card_number


def step(state: Easy21State, action):
    if action == Easy21Action.HIT.value:
        player_card = _sample_card()

        player_sum = player_card + state.player_sum
        reward = 0
        done = False
        if not 21 > player_sum >= 1:
            reward = -1
            done = True
        if player_sum == 21:
            reward = 1
        return Easy21State(dealer_card=state.dealer_card, player_sum=player_sum), done, reward
    elif action is Easy21Action.STICK.value:
        dealer_card = _sample_card()
        dealer_sum = state.dealer_card + dealer_card

        action = dealer_policy(dealer_sum)
        while action is Easy21Action.HIT.value and 21 > dealer_sum >= 1:
            dealer_sum += _sample_card()
            action = dealer_policy(dealer_sum)
        print('dealer sum is', dealer_sum)
        if action is Easy21Action.STICK.value:
            reward = (0 if dealer_sum == state.player_sum
                      else 1 if dealer_sum < state.player_sum or dealer_sum > 21 else -1)
            return state, True, reward
        else:
            reward = -1 if dealer_sum == 21 else 1
            return state, True, reward


def init_state():
    return Easy21State(dealer_card=random.randint(1, 10), player_sum=random.randint(1, 10))


def game():
    state = init_state()
    done = False
    print(state)
    while not done:
        action = Easy21Action.HIT.value if state.player_sum < 17 else Easy21Action.STICK.value
        state, done, reward = step(state, action)
        print(state, action, reward)
    print()

# [game() for _ in range(10)]
