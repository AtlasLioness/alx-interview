#!/usr/bin/python3
"""
Script to detrmine fewest nb of coins needed
to meet giver amount total
"""


def makeChange(coins, total):
    """
    Function to rturn fewest nb of coins needed to meet total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    add = 0
    nbcoins = 0

    for i in coins:
        while add < total:
            add += i
            nbcoins += 1
        if add == total:
            return nbcoins
        add -= i
        nbcoins -= 1
    return -1
