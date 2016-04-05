# Aimen Hassan
# CS-361
# 08/30/2015
#--------------------------------------------------------------

from CardDeck import *
import collections

class PokerHand(object):

    def __init__(self):
        # initilize list
        self.cards = []
    def setCard(self, position, card):
        # append card objects to list
        self.cards.append(card)
    def disCard(self):
        for i in self.cards:
            #print card in the exact format
            print(str(i))
    def attCard(self):
        # initilize two lists for value and suit
        list_value = []
        list_suit = []
        # variables to use for increments
        position_value = 0
        position_suit = 0
        for i in self.cards:
            # add card value to list
            list_value.append(i.getFaceValue())
            # increment
            position_value += 1
        for a in self.cards:
            # append suits
            list_suit.append(a.getSuitNumber())
            position_suit += 1
        # sort lists
        list_suit.sort()
        list_value.sort()
        # creat a set object
        seen = set()
        seen_add = seen.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        seen_twice = set( x for x in list_value if x in seen or seen_add(x) )
        # turn the set into a list
        list( seen_twice )
        # create another for suits, and same thing we did before
        seen_suit = set()
        seen_addsuit = seen_suit.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        seen_twiceSuit = set(l for l in list_suit if l in seen_suit or seen_addsuit(l))
        # turn the set into a list
        list(seen_twiceSuit)
        # create a list where the duplicates are removed from the original list_value and list_suit lists
        non_dupValue = set(list_value) - set(seen_twice)
        non_dupsuit = set(list_suit) - set(seen_twiceSuit)
        # checks if the list where duplicates are removed has only 1 item in it, and the duplicate list has 2 items
        if (len(non_dupValue) == 1) and (len(seen_twice) == 2):
            return 'Two Pairs'
        # checks if the list where duplicates are removed has 3 items, and the duplicate list has an item
        elif len(non_dupValue) == 3:
            return 'Two of a Kind'
        # if the non-duplicate list has 0 items, then its a full house
        elif len(non_dupValue) == 0:
            return 'Full House'
        # if non-duplicate list has only 2 values in it, then it must mean that that hand equals three of a kind
        elif len(non_dupValue) == 2:
            return 'Three of a Kind'
        # if non-duplicate list has one item in it, and duplicate list has 1, then its a four of a kind
        elif len(non_dupValue) == 1 and len(seen_twice) == 1:
            return 'Four of a Kind'
        else:
            # give variables ti every item in list
            card_1 = list_value[0]
            card_2 = list_value[1]
            card_3 = list_value[2]
            card_4 = list_value[3]
            card_5 = list_value[4]
            # check if every card is one more higher than the next
            if (card_2 == card_1 + 1) and (card_3 == card_2 + 1) and (card_4 == card_3 + 1) and (card_5 == card_4 + 1):
                # if the non-duplicate list of suites equal 0, then its staraigh fluhs
                if len(non_dupsuit) == 0:
                    return 'Straight Flush'
                else:
                    #otherwise, its just straight
                    return 'Straight'
            else:
                # if the non-duplicate suit equals 0, then its a flush
                if len(non_dupsuit) == 0:
                    return 'Flush'
                # otherwise it will be high card
                else:
                    return 'High Card'
    def sortedHand(self):
        # initialize two lists
        list_value = []
        list_suit = []
        # initialize increments
        position_value = 0
        position_suit = 0
        # for loop to add the face value of every card to a list
        for i in self.cards:
            list_value.append(i.getFaceValue())
            position_value += 1
        # for loop to add card suits to list
        for a in self.cards:
            list_suit.append(a.getSuitNumber())
            position_suit += 1
        # sort both lists
        list_suit.sort()
        list_value.sort()
        return list_value



        














