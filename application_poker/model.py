import random
import time

#define decorator
def print_html_page(func):
    def wrapper(*args, **kwargs):
        f = open("game.html", "w")
        html_code = """
                <!DOCTYPE html>
                <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="mystyle.css">
                    <meta http-equiv="refresh" content="2" />
                    <title>POKER GAME</title>	
                </head>
                <body>
                    <div id="poker_table">
                        <div id="card_area">
                            {} 
                        </div>
                    </div>
                </body>
                </html>
                """.format(func(*args, **kwargs))
        f.write(html_code)
        f.close()
    return wrapper

###########################################################################
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


#print_html_page(print_card(list_card))
@print_html_page
def print_card(list_card):

    html_code=""
    for val,sym in list_card:
        if sym in ["♦","♥"]:
            class_card="card_poker_red"
        else:
            class_card = "card_poker_black"

        html_code =html_code+ """
                            <div class={}>
                                {}
                                <div class="card_symbol">
                                    {}
                                </div>                         
                            </div>
                """.format(class_card,val,sym)
    return html_code

#################################################
while True:
    for i in range(3,6):
        time.sleep(2)
        list_card_generated=generate_cards(i)
        print("Python has generated:")
        print(list_card_generated)
        print_card(list_card_generated)