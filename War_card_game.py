import random
import os
import sys
import csv
sys.setrecursionlimit(100000)

class deckscontents:
    def __init__(self, card1, card2, deck1, deck2):
        self.card1 = card1
        self.card2 = card2
        self.deck1 = deck1
        self.deck2 = deck2
        self.stats_list = []
        self.stats_file = 'stats.csv'

    def deck_player1(self):
        count1 = len(self.deck1)
        count2 = len(self.deck2)

        with open('memory_deck1.txt', 'w') as file:
            file.write(f'{count1}')
        with open('memory_deck1.txt', 'r') as file:
            content1 = file.read()
            print(f'deck1: {content1}, deck2: {count2}')
            content1int = int(content1)
            if content1int == 0:
                print('Player 2 WIN.')
                menu()

    def deck_player2(self):
        count2 = len(self.deck2)
        count1 = len(self.deck1)

        with open('memory_deck2.txt', 'w') as file:
            file.write(f'{count2}')
        with open('memory_deck2.txt', 'r') as file:
            content2 = file.read()
            print(f'deck1: {count1}, deck2: {content2}')
            content2int = int(content2)
            if content2int == 0:
                print('Player 1 WIN.')
                menu()
    
    def tie(self):
        count1 = len(self.deck1)
        count2 = len(self.deck2)

        with open('memory_deck1.txt', 'w') as file:
            file.write(f'{count1}')
        with open('memory_deck2.txt', 'w') as file:
            file.write(f'{count2}')

        with open('memory_deck1.txt', 'r') as file:
            content1 = file.read()
        with open('memory_deck2.txt', 'r') as file:
            content2 = file.read()
        print(f'deck1: {content1}, deck2: {content2} TIE')
        content1int = int(content1)
        content2int = int(content2)
        if content1int == 0:
            print('Player 2 WIN.')
            menu()
        elif content2int == 0:
            print('Player 1 WIN.')
            menu()

def intro():
    os.system('cls')
    print('Welcome in War Card Game')
    menu()

def menu():
    while True:
        print('\n1. New Game')
        print('2. Exit')
        choice = input('Enter Your choice(1/2): ')
        if choice == '1':
            deck()
        elif choice == '2':
            os.system('cls')
            print('Exiting War Card Game, Goodbye.\n')
            quit()
        else:
            os.system('cls')
            print('Invalid Value.')
            menu()

def deck():
    deck = []
    suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']    
    for x in range(2,15):
        for y in suit:
            z = x, y
            deck.append(z)
    deal(deck)

def deal(deck):
    
    deck2 = random.sample(deck, 26)
    for x in deck2:
        deck.remove(x)
    draw(deck,deck2)

def draw(deck,deck2):
    deck1 = deck
    card1 = random.choice(deck1)
    card2 = random.choice(deck2)
    fight_list = []
    deck_content = deckscontents(card1, card2, deck1, deck2)
    fight(card1, card2, deck1, deck2, fight_list, deck_content)
    #print(card1, card2)

def fight(card1,card2, deck1, deck2, fight_list, deck_content: deckscontents):
    count1 = len(deck1)
    count2 = len(deck2)
    if count1 == 0:
        deck_content.deck_player1() 
    if count2 == 0:
        deck_content.deck_player2() 
    card1 = random.choice(deck1)
    card2 = random.choice(deck2)
    card1_power = card1[0]
    card2_power = card2[0]
    while True:
        if card1_power > card2_power:
            #print(f'{card1} > {card2}')
            deck1.extend(fight_list)
            fight_list = []
            deck1.append(card2)
            deck2.remove(card2)
            deck_content.stats()
            deck_content.deck_player1()
            fight(card1,card2, deck1, deck2, fight_list, deck_content)
            #deck()
        elif card1_power < card2_power:
            #print(f'{card1} < {card2}')
            deck2.extend(fight_list)
            fight_list = []
            deck1.remove(card1)
            deck2.append(card1)
            deck_content.stats()
            deck_content.deck_player2()
            fight(card1,card2, deck1, deck2, fight_list, deck_content)
            #deck()
        else:
            #print(f'{card1} = {card2}')
            deck1.remove(card1)
            deck2.remove(card2)
            fight_list.append(card1)
            fight_list.append(card2)
            #print(fight_list)
            deck_content.stats()
            deck_content.tie()
            fight(card1,card2, deck1, deck2, fight_list, deck_content)

if __name__ == '__main__':
     intro()