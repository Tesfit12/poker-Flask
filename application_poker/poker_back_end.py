import random
def generate_cards(number):
    value=["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    symbol=["♣","♦","♥","♠"]

    gen_card=[]

    for i in range(number):
        random_value=random.choice(value)
        random_symbol=random.choice(symbol)

        while (random_value,random_symbol) in gen_card:
            random_value = random.choice(value)
            random_symbol = random.choice(symbol)

        gen_card.append((random_value,random_symbol))
    return gen_card


class Player():
    def __init__(self,name,chips):
        self.name=name
        self.chips=chips

players=[]
