#!/usr/bin/env python

#----------------------------------------------------------------------
# poker.py
# Aimen Hassan
# 08/30/2015
#----------------------------------------------------------------------

import sys
import collections

from PokerHand import *
from CardDeck import *

#----------------------------------------------------------------------

def dealHands():

    '''returns two PokerHands each containing 5 cards'''

    # create a card deck
    deck = CardDeck()
    deck.shuffle()

    # create two poker hands
    hand1 = PokerHand()
    hand2 = PokerHand()

    # deal 5 cards to first hand
    for i in range(5):
        c = deck.dealOne()
        hand1.setCard(i, c)

    # deal 5 cards to second hand
    for i in range(5):
        c = deck.dealOne()
        hand2.setCard(i, c)

    # return the two PokerHand objects
    return hand1, hand2

#----------------------------------------------------------------------

def textGame():

    '''plays a game of poker displaying all the data using print'''
    # call function to get layer hand and dealer hand
    player_hand, dealer_hand = dealHands()
    # prints player hand
    print("Player hand")
    # calls discard method to print hands
    player_hand.disCard()
    # call attcard method to get hand value
    hand_value = player_hand.attCard()
    print(hand_value)
    print('')
    print('Dealer Hand')
    #display dealer hand
    dealer_hand.disCard()
    # get dealer hand value
    dealer_value = dealer_hand.attCard()
    print(dealer_value)
    # call method to get sorted lists of each hand
    list_values = player_hand.sortedHand()
    list_values2 = dealer_hand.sortedHand()
    # create a set object
    player_seen = set()
    # use add method
    player_add = player_seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    player_twice = set(x for x in list_values if x in player_seen or player_add(x))
    # turn the set into a list
    player_list = list(player_twice)
    #sorts it
    player_sorted = sorted(player_list)
    # create a set
    dealer_seen = set()
    dealer_add = dealer_seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    dealer_twice = set(t for t in list_values2 if t in dealer_seen or dealer_add(t))
    # turn the set into a list
    dealer_list = list(dealer_twice)
    # sort the list
    dealer_sorted = sorted(dealer_list)
    # remove duplicates from original set
    fin_player = set(list_values) - set(player_twice)
    fin_dealer = set(list_values2) - set(dealer_twice)
    # make them a list
    fin_list2 = list(fin_dealer)
    fin_list = list(fin_player)
    # sort each of them
    fin_list.sort()
    fin_list2.sort()
    print('')
    if hand_value == 'High Card':
        # if both hands are same
        if dealer_value == hand_value:
            pos_1 = 4
            # make while loop to see which hand has the highest card
            while pos_1 >= 0:
                # if they're equal and pos_1 doesnt equal zero then decremnt pos_1
                if (list_values[pos_1] == list_values2[pos_1]) and (pos_1 != 0):
                    pos_1 -= 1
                # if player's card is higher then he wins
                elif list_values[pos_1] > list_values2[pos_1]:
                    print('Player wins')
                    break
                # if all cards are equal then its a tie
                elif (list_values[pos_1] == list_values2[pos_1]) and (pos_1 == 0):
                    print('Pot is Split')
                    break
                else:
                    # otherwise dealer wins
                    print('Dealer wins')
                    break
        else:
            print('Dealer wins')
    elif hand_value == 'Two of a Kind':
        # if dealer hand equals high card, then player wins
        if dealer_value == 'High Card':
            print('Player wins')
        # if both hands are the same
        elif dealer_value == hand_value:
            # check which duplicate list is the highest
            if player_sorted[0] > dealer_sorted[0]:
                print('Player wins')
            elif player_sorted[0] < dealer_sorted[0]:
                print('Dealer wins')
            # run a while loop to determine which value is the highest (excluding duplicates)
            else:
                pos_1 = 2
                while pos_1 >= 0:
                    if (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 != 0):
                        pos_1 -= 1
                    elif fin_list[pos_1] > fin_list2[pos_1]:
                        print('Player wins')
                        break
                    elif (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 == 0):
                        print('Pot is Split')
                        break
                    else:
                        print('Dealer wins')
                        break
        else:
            print('Dealer wins')
    elif hand_value == 'Two Pairs':
        # if the dealer hand equals any of those, then player wins
        if dealer_value == 'High Card' or dealer_value == 'Two of a Kind':
            print('Player wins')
        elif dealer_value == hand_value:
            # check the duplicate lists to see which person has the higher duplicate
            if player_sorted[1] > dealer_sorted[1]:
                print('Player wins')
            elif player_sorted[1] < dealer_sorted[1]:
                print('Dealer wins')
            elif player_sorted[0] > dealer_sorted[0]:
                print('Player wins')
            elif player_sorted[0] < dealer_sorted[0]:
                print('Dealer wins')
            else:
                pos_1 = 0
                # run while loop once to check the one remaining item in list
                while pos_1 >= 0:
                    if (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 != 0):
                        pos_1 -= 1
                    elif fin_list[pos_1] > fin_list2[pos_1]:
                        print('Player wins')
                        break
                    elif (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 == 0):
                        print('Pot is Split')
                        break
                    else:
                        print('Dealer wins')
                        break
        else:
            print('Dealer wins')
    # if player hand is three of a kind
    elif hand_value == 'Three of a Kind':
        # if the dealer's hand is any of these, then player wins
        if dealer_value == 'High Card' or dealer_value == 'Two of a Kind' or dealer_value == 'Two Pairs':
            print('Player wins')
        elif dealer_value == hand_value:
            # check the duplicate list to see whose got higher value
            if player_sorted[0] > dealer_sorted[0]:
                print('Player wins')
            else:
                print('Dealer wins')
        else:
            print('Dealer wins')
    elif hand_value == 'Straight':
        # if the dealer's hand is any of these then player wins
        if (dealer_value == 'High Card') or (dealer_value == 'Two of a Kind') or (dealer_value == 'Two Pairs') or (dealer_value== 'Three of a Kind'):
            print('Player wins')
        elif dealer_value == hand_value:
            pos_1 = 4
            # run loop to determine which hand has the highest value
            while pos_1 >= 0:
                if (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 != 0):
                    pos_1 -= 1
                elif fin_list[pos_1] > fin_list2[pos_1]:
                    print('Player wins')
                    break
                elif (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 == 0):
                    print('Pot is Split')
                    break
                else:
                    print('Dealer wins')
                    break
        else:
            print('Dealer wins')
    elif hand_value == 'Flush':
        # if dealer's hand is any of these, then he lost
        if (dealer_value == 'High Card') or (dealer_value == 'Two of a Kind') or (dealer_value == 'Two Pairs') or (dealer_value == 'Three of a Kind') or (dealer_value == 'Straight'):
            print('Player wins')
        elif dealer_value == hand_value:
            pos_1 = 4
            # while loop to determine highest value in both hands
            while pos_1 >= 0:
                if (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 != 0):
                    pos_1 -= 1
                elif fin_list[pos_1] > fin_list2[pos_1]:
                    print('Player wins')
                    break
                elif (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 == 0):
                    print('Pot is Split')
                else:
                    print('Dealer wins')
                    break
        else:
            print('dealer wins')
    elif hand_value == 'Full House':
        # if dealer' hand is any of these then he lost
        if (dealer_value == 'High Card') or (dealer_value == 'Two of a Kind') or (dealer_value == 'Two Pairs') or (dealer_value == 'Three of a Kind') or (dealer_value == 'Straight') or (dealer_value == 'Flush'):
            print('Player wins')
        elif dealer_value == hand_value:
            # check the highest value in the non-duplicate lists (it will be different for each list)
            if list_values[2] > list_values2[2]:
                print('Player wins')
            else:
                print('Dealer wins')
        else:
            print('Dealer wins')
    elif hand_value == 'Four of a Kind':
        # if dealer's hand is straight flush then he wins
        if dealer_value == 'Straight Flush':
            print('Dealer wins')
        elif dealer_value == hand_value:
            # check the duplicate lists' highest value for both dealer and player
            if player_sorted[0] > dealer_sorted[0]:
                print('Player wins')
            else:
                print('Dealer wins')
        else:
            print('Player wins')
    else:
        # if dealer hand isn't straight flush then player wins
        if dealer_value != hand_value:
            print('Player wins')
        else:
            # run loop to determine highest value in both hands
            pos_1 = 4
            while pos_1 >= 0:
                if (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 != 0):
                    pos_1 -= 1
                elif fin_list[pos_1] > fin_list2[pos_1]:
                    print('Player wins')
                    break
                elif (fin_list[pos_1] == fin_list2[pos_1]) and (pos_1 == 0):
                    print('Pot is split')
                    break
                else:
                    print('Dealer wins')
                    break






#----------------------------------------------------------------------

def main(argv):

    textGame()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
