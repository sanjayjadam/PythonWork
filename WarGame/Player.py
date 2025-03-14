import Card
import random
# values = {'Two': 2,'Three':3, 'Four':4, 'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12, 'King':13,'Ace':14 }
# suits = ['Hearts','Diamonds','Spades','Clubs']
# ranks = ['Two','Three','Four','Five','Six','Seven','Eight', 'Nine','Ten','Jack','Queen','King','Ace']

class Player:

    def __init__(self, name):
        self.all_cards = []
        self.name = name

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'