#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the least number of
    operations needed to result in exactly n H
    if n is impossible to achieve, then return 0
    '''
    characters = 1
    list = 0
    counter = 0

    while characters < n:
        if list == 0:
           list = characters
           counter += 1

        if characters == 1:
           characters += list
           counter += 1
           continue

        remaining = n - characters
        ''' check the list to determine whether
        the number desired is reached'''
        if remaining < list:
            return 0

        if remaining % characters != 0:
            characters += list
            counter += 1
        else:
            list = characters
            characters += list
            counter += 2
            
    if characters == n:
        return counter
    else:
        return 0
