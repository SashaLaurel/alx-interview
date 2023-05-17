#!/usr/bin/python3
'''
   Determines the fewest number of coins needed to meet
   a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: 
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you 
    have, return -1
    '''
    sum = 0
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    for i in coins:
        if (total < i):
            pass
        q, r = divmod(total, i)
        total = r
        sum += q
    if (total != 0):
        return -1
    return sum
