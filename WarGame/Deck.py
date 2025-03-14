import Card
import random
import Global
# values = {'Two': 2,'Three':3, 'Four':4, 'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12, 'King':13,'Ace':14 }
# suits = ['Hearts','Diamonds','Spades','Clubs']
# ranks = ['Two','Three','Four','Five','Six','Seven','Eight', 'Nine','Ten','Jack','Queen','King','Ace']
class Deck:
    def __init__(self):
        
        self.all_cards = []

        for suit in Global.constant().suits:
            for rank in Global.constant().ranks:
                created_card = Card.Card(suit,rank)
                self.all_cards.append(created_card)

    def Sheffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
# def f():
#     decks = Deck()
#     print(len(decks.all_cards))
#     decks.Sheffle()
#     c = decks.deal_one()
#     print(c)
#     print(len(decks.all_cards))
#     # for d in decks.all_cards:
#     #     print(d)
#     #print(decks.all_cards.count)


# f()