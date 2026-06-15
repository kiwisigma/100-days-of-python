# import art
import random
# from art import logo
# print(logo)
# #
# print(f"Do you want to play a game of Blackjack? type 'y' or 'n':")
# 
def deal_cards():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.choice(cards)
    return random.choice(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_cards()
    user_cards.append(new_card)