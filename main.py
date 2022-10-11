#run this code to start game
from player import Player
from deck import Deck
import random

deck = Deck()
#Create deck and empty hand
available_cards = deck.build()
hand = []

#Add card to hand and remove from deck
card = random.choice(available_cards)
available_cards.remove(card)
hand.append(card)

#Create Player with hand and stay/hit
pc = Player(hand)
action = random.randint(0,1)
pc.make_action(action)
