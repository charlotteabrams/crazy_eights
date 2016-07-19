# Required dependencies
from random import shuffle

# Deck of cards

class Card(object):
    def __init__(self, suit, value, image=None):
        self.suit = suit
        self.value = value
        self.image = image

class Deck(object):
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))
        self.shuffle()
        return self

    def shuffle(self):
        shuffle(self.deck)
        return self

    def deal(self):
        if self.deck: # empty lists return as False
            # removes and returns card from deck, shuffled or not
            return self.deck.pop()
        else:
            print "No more cards"

    # def returnCard(self, card, reShuffle = False):
    #     self.deck.append(card)
    #     if reShuffle:
    #         self.shuffle()
    #     return self

    def resetDeck(self):
        self.deck = []
        self.buildDeck()
        return self

class Player(object):
    def __init__(self, deck, name):
        self.hand = []
        self.name = name

    def getHand(self):
        for i in range (1,9):
            card = deck.deal()
            self.hand.append(card)
        return self.hand
    def showHand(self):
        count = 0
        print self.name
        for j in self.hand:
            print count, "-", j.value, "of", j.suit
            count += 1
    def draw(self):
        draw = deck.deal()
        # self.hand.append(draw)
        return draw
    def flipCard(self):
        flip = deck.deal()
        return flip
    def play(self, flip, hand):
        self.flip = flip
        self.hand = hand
        self.showHand()
        displayCard = self.flip
        print self.name,": Your Turn. Which card would you like to play?\n It must match: ", displayCard.value, "of", displayCard.suit, "Or you can press 'D' to Draw."
        choice = raw_input()
        cycle = True
        while (cycle==True):
            for x in range(0, len(self.hand)):
                if(choice==str(x)):
                    print "card ", x
                    # discardPile.append(self.hand[x])
                    displayCard = self.hand[x]
                    showCard(displayCard)
                    del self.hand[x]
                    cycle = False
                    break
                elif(choice=="D" or choice=="d"):
                    draw = self.draw()
                    self.hand.append(draw)
                    self.showHand()
                    choice = raw_input("Which card would you like to play? Or you can press 'D' to Draw.")
                    break
            # print discardPile
    
def showCard(card):
    print card.value, "of", card.suit



class Game(Card):
    def __init__(self, deck):
        playgame = True
        answer = raw_input("Do you want to play Crazy Eights? Y/N \n")
        if (answer == "Y" or answer == "y"):
            playgame = True
        else:
            print "Alrighty, have a nice day anyways."
            playgame = False

        player1 = Player(deck, "Player 1")
        player2 = Player(deck, "Player 2")
        # hand1 = player1.getHand()
        # hand2 = player2.getHand()
        # player1.showHand()
        # player2.showHand()

        while playgame == True:
            # player1.showHand()
            displayCard = player1.flipCard()
            discardPile = []
            discardPile.append(displayCard)
            player1.play(player1.flipCard(),player1.getHand())
            player2.play(player2.flipCard(),player2.getHand())
            playgame = False
            # print "\nPlayer: You Go First! Which card would you like to play? It must match:", showCard(displayCard)
            # print "To draw a card, press 'D'"
            # index = input()
            # for x in range(0, len(hand1)):
            #     if(index==x):
            #         discardPile.append(hand1[x])
            #         showCard(hand1[x])
            #         displayCard = hand1[x]
            #     elif(index=="D"):
            #         player1.draw()
            # print discardPile
# class Game(Player, Deck):
#     def __init__(self):
#         super(Game, self, self.deck, self.name).__init__()
#         self.deck = []
#     def flipCard(self):
#         flip = self.deck.deal()
#         print flip.value, flip.suit
    

# game.flipCard()
# def show


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
deck = Deck(suits, values)
game = Game(deck)

# GAME

# discardPile = []
# player1 = Player(deck, "Player 1")
# player2 = Player(deck, "Player 2")

# hand1 = player1.getHand()
# player1.showHand()
# flip = player1.flipCard()
# discardPile.append(flip)
# print "\nPlayer 1: You Go First! Which card would you like to play? It must match:", showCard(flip)
# print "To draw a card, press 'D'"
# index = input()
# for x in range(0, len(hand1)):
#     if(index==x):
#         discardPile.append(hand1[x])
#         showCard(hand1[x])
#     elif(index=="D"):
#         player1.draw()
# print discardPile
    # else:
    #     print "That's not a valid attempt. Exit Game."


# player2.getHand().showHand()




# player1.play()


# game = Game(hand)

# deck.buildDeck()

# print deck.deck.pop().value
# print deck.deck.pop().suit

# deck.shuffle()

# deck.resetDeck()




# print deck.deck[0].value
# print deck.deck[0].suit



# print card.value