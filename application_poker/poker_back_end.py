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
    active_player=1


    def __init__(self, name, chips, avatar, id):
        self.name = name
        self.chips = chips
        self.avatar = avatar
        self.cards = generate_cards(2)
        self.id = id

    @classmethod
    def move_to_next_player(cls,list_players):
        index_active=cls.active_player-1
        index_next_player=(index_active+1)%len(list_players)

        i=index_next_player
        while True:
            if list_players[i].is_in:
                index_next_player = i
                break
            else:
                i=(i+1)%4

        cls.active_player=index_next_player+1











    def __init__(self,name,chips,avatar,id):
        self.name=name
        self.chips=chips
        self.avatar=avatar
        self.cards=generate_cards(2)
        self.is_in=True
        self.id=id

    def bet_money(self,chips):
        self.chips=self.chips-chips

    def win_game(self,chips):
        self.chips=self.chips+chips

    def fold(self):
        self.is_in=False



players=[]
