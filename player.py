import random
import numpy as np
from deck import Deck

class Player():
    
    def __init__(self, cards) -> None:
        self.cards = cards
  
    def make_action(self, action):
        cards = self.cards
        if action == 0: #hit
            print('Hit!')
            if sum(cards) > 21:
                return -10, True
            else:
                return +1, False #Round not done
        elif action == 1: #stay
            print('Stay')
            return 0, True
            