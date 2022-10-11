
class Card():
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        
class Deck():
    def __init__(self) -> None:
        self.cards = []
         
    def build(self):
        
        vals = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        vals = [vals] * 4
        output = sum(vals, [])
        return output
        