import random
import os
import sys
import csv
sys.setrecursionlimit(100000)

class deckscontents:
    def __init__(self, card1, card2, deck1, deck2, countfight_list):
        self.countfight_list = countfight_list
        self.card1 = card1
        self.card2 = card2
        self.deck1 = deck1
        self.deck2 = deck2
    
    #print player 1 deck card amount
    def deck_player1(self):
        count1, count2 = countdecks(self.deck1, self.deck2)
        print(f'Player A: {count1}   Player B: {count2}')
        count2int = int(count2)
        if count2int == 0:
            print('Player A WIN.')
            menu()
    
    #print player 2 deck card amount
    def deck_player2(self):
        count1, count2 = countdecks(self.deck1, self.deck2)
        print(f'Player A: {count1}   Player B: {count2}')
        count1int = int(count1)
        if count1int == 0:
            print('Player B WIN.')
            menu()
    
    #print player 1, and player 2 deck card amount when its tie. 
    def tie(self):
        count1, count2 = countdecks(self.deck1, self.deck2)
        print(f'Player A: {count1}   Player B: {count2} TIE')
        content1int = int(count1) 
        content2int = int(count2)
        if content1int == 0:
            print('Player B WIN.')
            menu()
        elif content2int == 0:
            print('Player A WIN.')
            menu()
            
    #save all cycles in the game in .csv file.
class stats:
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.stats_file = 'stats.csv'
    def substats(self, stats_list):
        count1, count2 = countdecks(self.deck1, self.deck2)
        with open(self.stats_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Player1", "Player2"])
            stats_list.append({"Player1": count1, "Player2": count2})
            writer.writeheader()
            writer.writerows(stats_list)
            
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
    random.shuffle(deck)
    deck1 = deck[26:]
    deck2 = deck[:26]
    fight_list_memory(deck1,deck2)

#starting to count the deck of cards. 
#starting fight cards list 'fight_list'(using in tie 'p1p2tie' function). 
#starting 'stats_list' for .csv file in 'stats' class.
def fight_list_memory(deck1,deck2):
    count1, count2 = countdecks(deck1, deck2)
    print(f'Player A: {count1}   Player B: {count2}')
    fight_list = []
    stats_list = []
    stats_file = stats(deck1, deck2)
    stats_file.substats(stats_list)
    fight(deck1, deck2, fight_list, stats_list, stats_file)

#card counter in hand
def countdecks(deck1,deck2):
    count1 = len(deck1)
    count2 = len(deck2)
    return count1, count2

#checking if any player has won
def zerocheck(deck1, deck2, deck_content: deckscontents, stats_file: stats, stats_list):
    count1, count2 = countdecks(deck1, deck2)
    if count1 == 0:
        stats_file.substats(stats_list)
        deck_content.deck_player1() 
    elif count2 == 0:
        stats_file.substats(stats_list)
        deck_content.deck_player2() 

#the function 'fight' compares two cards. If there is a tie, the cards are added to the 'fight_list'
#If any player wins the fight, the respective cards are removed from the decks and added back accordingly, and the fight continues.
def fight(deck1, deck2, fight_list, stats_list, stats_file):
    card1 = deck1.pop()
    card2 = deck2.pop()
    countfight_list = len(fight_list)
    deck_content = deckscontents(card1, card2, deck1, deck2, countfight_list)
    zerocheck(deck1, deck2, deck_content, stats_file, stats_list)
    card1_power = card1[0]
    card2_power = card2[0]
    while True:
        if card1_power > card2_power:
            p1fightwin(deck1, deck2, card1, card2, fight_list, stats_list, stats_file, deck_content)
        elif card1_power < card2_power:
            p2fightwin(deck1, deck2, card1, card2, fight_list, stats_list, stats_file, deck_content)
        else:
            p1p2tie(deck1,deck2, card1, card2, fight_list, stats_list, stats_file, deck_content)

def p1fightwin(deck1, deck2, card1, card2, fight_list, stats_list, stats_file :stats, deck_content: deckscontents):
    deck1.extend(fight_list)
    fight_list = []
    deck1.append(card2)
    deck1.append(card1)
    random.shuffle(deck1)
    stats_file.substats(stats_list)
    deck_content.deck_player1()
    fight(deck1, deck2, fight_list, stats_list, stats_file)

def p2fightwin(deck1,deck2, card1, card2, fight_list, stats_list, stats_file: stats, deck_content: deckscontents):
    deck2.extend(fight_list)
    fight_list = []
    deck2.append(card1)
    deck2.append(card2)
    random.shuffle(deck2)
    stats_file.substats(stats_list)
    deck_content.deck_player2()
    fight(deck1, deck2, fight_list, stats_list, stats_file)

def p1p2tie(deck1,deck2, card1, card2, fight_list, stats_list, stats_file: stats, deck_content: deckscontents):
    fight_list.append(card1)
    fight_list.append(card2)
    random.shuffle(fight_list)
    stats_file.substats(stats_list)
    deck_content.tie()
    fight(deck1, deck2, fight_list, stats_list, stats_file)

if __name__ == '__main__':
     intro()
