import Global
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Global.constant().values[rank.capitalize()]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
# def func():
#         c =  Card('Hearts','two')
#         print( c.value)
#         print(c.suit)
#         print(c.rank)
#         #print(values['Ace'])

# func()