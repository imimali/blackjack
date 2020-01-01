# Blackjack and Hookers
 
See [Futurama](https://www.youtube.com/watch?v=e35AQK014tI)

The aim of this project is to present several reinforcement learning algorithms applied in a simple Markov Decision Process emerged by a modified version of the game originally known as Blackjack. 

The rules of the game are defined as:

- The game is played with an infinite deck of cards (i.e. cards are sampled
with replacement) 
- Each draw from the deck results in a value between 1 and 10 (uniformly
distributed) with a colour of red (probability 1/3) or black (probability
2/3). 
- There are no aces or picture (face) cards in this game 
- At the start of the game both the player and the dealer draw one black
card (fully observed) 
- Each turn the player may either stick or hit 
- If the player hits then she draws another card from the deck 
- If the player sticks she receives no further cards 
- The values of the player’s cards are added (black cards) or subtracted (red
cards) 
- If the player’s sum exceeds 21, or becomes less than 1, then she “goes
bust” and loses the game (reward -1)  
- If the player sticks then the dealer starts taking turns. The dealer always
sticks on any sum of 17 or greater, and hits otherwise. If the dealer goes
bust, then the player wins; otherwise, the outcome – win (reward +1),
lose (reward -1), or draw (reward 0) – is the player with the largest sum.


## Monte Carlo Control: 
- Monte Carlo Control uses the generalised policy iteration scheme, with the empirical mean as the target 
## Sarsa: 
- The classical SARS'A' algorithm
## Sarsa Lambda:
- SARS'A' with eligibility traces 
## Q-Learning:
- The classical tabular Q-Learning algorithm
