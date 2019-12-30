'''
    created on 29 December 2019
    
    @author: Gergely
'''

import random
from collections import namedtuple

Easy21State = namedtuple('Easy21State', 'dealer_card player_sum')


# Easy21State.__hash__ = lambda state: state.dealer_card + state.player_sum


class Easy21Action:
    HIT = 'hit'
    STICK = 'stick'


def dealer_action(dealer_sum):
    return Easy21Action.HIT if dealer_sum < 17 else Easy21Action.STICK


def _sample_card():
    card_number = random.randint(1, 10)
    card_color = -1 if random.random() < 1 / 3 else 1
    return card_color * card_number


def step(state: Easy21State, action: str):
    if action is Easy21Action.HIT:
        player_card = _sample_card()

        player_sum = player_card + state.player_sum
        reward = 0
        done = False
        if not 21 > player_sum > 1:
            reward = -1
            done = True
        return Easy21State(dealer_card=state.dealer_card, player_sum=player_sum), done, reward
    elif action is Easy21Action.STICK:
        dealer_card = _sample_card()
        dealer_sum = state.dealer_card + dealer_card

        action = dealer_action(dealer_sum)
        while action is Easy21Action.HIT and 21 > dealer_sum > 1:
            dealer_sum += _sample_card()
        print('dealer sum is', dealer_sum)
        if action is Easy21Action.STICK:
            reward = 0 if dealer_sum == state.player_sum else 1 if dealer_sum < state.player_sum else -1
            return state, True, reward
        else:
            return state, True, 1


def init_state():
    return Easy21State(dealer_card=random.randint(1, 10), player_sum=random.randint(1, 10))


def game():
    state = init_state()
    done = False
    while not done:
        action = Easy21Action.HIT
        state, done, reward = step(state, action)


s = Easy21State(dealer_card=1, player_sum=12)
s1 = Easy21State(dealer_card=2, player_sum=13)
print(s.__hash__())
print(s.__hash__())
print(s1.__hash__())
print(s1.__hash__())

