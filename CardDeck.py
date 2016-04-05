#!/usr/bin/env python
# Aimen Hassan
# CS160

#----------------------------------------------------------------------

import random
import os.path

#----------------------------------------------------------------------

class Card:

    'class for representing a single card'

    #------------------------------------------------------------------
    # class variables shared by all instances
    
    # string version of the face value
    FACES = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'j', 'q', 'k')

    # single character string for each suit
    SUITS = ('c', 's', 'h', 'd')
    FACE_NAMES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King')
    SUIT_NAMES = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    
    #------------------------------------------------------------------

    def __init__(self, value):
        
        '''create a card represented by numbers 0-51 or a string where
        the last letter is the character c, s, h, or d for the suit
        and the first character is a, 2, 3, 4, 5, ..., 9 or two
        characters 10 for the face value'''

        # check if value is a string for the card
        try:
            face = value[:-1].lower()
            suit = value[-1].lower()
            face_pos = self.FACES.index(face)
            suit_pos = self.SUITS.index(suit)
            self.value = suit_pos * 13 + face_pos
        # if exception generated, assume it is a number
        except TypeError:
            self.value = value

    #------------------------------------------------------------------

    def getFilename(self):

        '''returns the filename of the form: ##s.gif where ## is a two
        digit number (leading 0 if less than 10) and s is a letter
        corresponding to the suit value d for diamond, h for heart, c
        for club, s for spade'''

        suitNum = self.value / 13
        faceNum = self.value % 13 + 1
        return '{:02d}{:}.gif'.format(face_num, self.SUITS[suit_num])
                               
    #------------------------------------------------------------------

    def getFaceValue(self):

        '''returns the face value in the range 2-14 (Jack is 11, Queen
        is 12, King is 13, Ace is 14)'''

        value = self.value % 13 + 1
        if value == 1:
            value = 14
        return value
    
    #------------------------------------------------------------------

    def getSuitNumber(self):

        '''returns suit number card (0 for clubs, 1 for spades, 2 for
        hearts, or 3 for diamonds)'''

        return self.value // 13
    
    #------------------------------------------------------------------
    
    def getBlackjackValue(self):

        '''returns blackjack value for card (11 for Ace)'''

        face = self.value % 13 + 1
        if face > 10:
            face = 10
        elif face == 1:
            face = 11
        return face

    #------------------------------------------------------------------

    def __str__(self):

        '''returns string representation of card such as
        2 of Clubs'''

        value = self.value % 13
        suit = self.value // 13
        return '%s of %s' % (self.FACE_NAMES[value], self.SUIT_NAMES[suit])

#----------------------------------------------------------------------

class CardDeck:

    'class for representing a deck of cards'

    #------------------------------------------------------------------

    def __init__(self):
        
        '''create a deck of cards represented by numbers 0-51'''

        self.freshDeck()

    #------------------------------------------------------------------
    
    def freshDeck(self):

        '''orders the cards from 0 to 51 and sets next card to be dealt
        to card 0'''


        self.cards = list(range(52))
        self.pos = 0
        self.stacked = False

        # allow deck to be stacked with contents of first line in stacked-deck.txt
        if os.path.exists("stacked-deck.txt"):
            self.stacked = True
            infile = open("stacked-deck.txt", "r")
            line = infile.readline()
            if line[:-1] == '\n':
                line = line[:-1]
            for i, c in enumerate(line.split()):
                c = Card(c)
                self.cards[i] = c.value
            #print(self.cards[:10])

    #------------------------------------------------------------------

    def shuffle(self):

        '''shuffles all 52 cards'''

        if not self.stacked:
            # for each card in the deck
            for i in range(52):
                # pick a random card to swap it with
                r = random.randrange(0, 52)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    #------------------------------------------------------------------

    def dealOne(self):

        '''returns the number corresponding to the next card;
        returns None if there are no cards left to be dealt'''
        
        # if cards left to deal
        if self.pos < 52:
            # get card and update the next card to deal
            c = self.cards[self.pos]
            self.pos = self.pos + 1
            return Card(c)
        else:
            return None

#----------------------------------------------------------------------
