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
    
    #save player 1 deck card amount in hand
    def deck_player1(self):
        count1, count2 = count(self.deck1, self.deck2)
        with open('memory_deck1.txt', 'w') as file:
            file.write(f'{count1}')
        with open('memory_deck1.txt', 'r') as file:
            content1 = file.read()
        print(f'deck1: {content1}, deck2: {count2}')
        content1int = int(content1)
        if content1int == 0:
            print('Player 2 WIN.')
            menu()
    
    #save player 2 deck card amount in hand
    def deck_player2(self):
        count1, count2 = count(self.deck1, self.deck2)
        with open('memory_deck2.txt', 'w') as file:
            file.write(f'{count2}')
        with open('memory_deck2.txt', 'r') as file:
            content2 = file.read()
        print(f'deck1: {count1}, deck2: {content2}')
        content2int = int(content2)
        if content2int == 0:
            print('Player 1 WIN.')
            menu()
    
    #save player 1, and player 2 deck card amount in hands when its tie. 
    def tie(self):
        count1, count2 = count(self.deck1, self.deck2)
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
    #save all cycles in the game in .csv file.
    def stats(self):
        count1, count2 = count(self.deck1, self.deck2)
        with open(self.stats_file, mode='w', newline='') as file:
            self.stats_list.append({"Player1": count1, "Player2": count2})
            writer = csv.DictWriter(file, fieldnames=["Player1", "Player2"])
            writer.writeheader()
            writer.writerows(self.stats_list)
            
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
            
#create deck
def deck():
    deck = []
    suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']    
    for x in range(2,15):
        for y in suit:
            z = x, y
            deck.append(z)
    deal(deck)
    
#dealing deck to two amount of 26 card
def deal(deck): 
    deck2 = random.sample(deck, 26)
    for x in deck2:
        deck.remove(x)
    deck1 = deck
    draw(deck1,deck2)

#both players draw a card
def draw(deck1,deck2):
    count1, count2 = count(deck1, deck2)
    print(f'deck1: {count1}, deck2: {count2}')
    card1 = random.choice(deck1)
    card2 = random.choice(deck2)
    fight_list = []
    deck_content = deckscontents(card1, card2, deck1, deck2)
    deck_content.stats()
    fight(card1, card2, deck1, deck2, fight_list, deck_content)

#card counter in hand
def count(deck1,deck2):
    count1 = len(deck1)
    count2 = len(deck2)
    return count1, count2

#checking if any player has won
def zerocheck(deck1, deck2, deck_content: deckscontents):
    count1, count2 = count(deck1, deck2)
    if count1 == 0:
        deck_content.deck_player1() 
    elif count2 == 0:
        deck_content.deck_player2() 

#the function 'fight' compares two cards. If there is a tie, the cards are added to the 'fight_list.'
#If any player wins the fight, the respective cards are removed from the decks and added back accordingly, and the fight continues.
def fight(card1,card2, deck1, deck2, fight_list, deck_content: deckscontents):
    zerocheck(deck1, deck2, deck_content)
    card1 = random.choice(deck1)
    card2 = random.choice(deck2)
    card1_power = card1[0]
    card2_power = card2[0]
    while True:
        if card1_power > card2_power:
            p1fightwin(deck1, deck2, card1, card2, fight_list, deck_content)

        elif card1_power < card2_power:
            p2fightwin(deck1, deck2, card1, card2, fight_list, deck_content)
            
        else:
            p1p2tie(deck1,deck2, card1, card2, fight_list, deck_content)

def p1fightwin(deck1, deck2, card1, card2, fight_list, deck_content: deckscontents):
    deck1.extend(fight_list)
    fight_list = []
    deck1.append(card2)
    deck2.remove(card2)
    deck_content.stats()
    deck_content.deck_player1()
    fight(card1,card2, deck1, deck2, fight_list, deck_content)

def p2fightwin(deck1,deck2, card1, card2, fight_list, deck_content: deckscontents):
    deck2.extend(fight_list)
    fight_list = []
    deck1.remove(card1)
    deck2.append(card1)
    deck_content.stats()
    deck_content.deck_player2()
    fight(card1,card2, deck1, deck2, fight_list, deck_content)

def p1p2tie(deck1,deck2, card1, card2, fight_list, deck_content: deckscontents):
    deck1.remove(card1)
    deck2.remove(card2)
    fight_list.append(card1)
    fight_list.append(card2)
    deck_content.stats()
    deck_content.tie()
    fight(card1,card2, deck1, deck2, fight_list, deck_content)


if __name__ == '__main__':
     intro()
