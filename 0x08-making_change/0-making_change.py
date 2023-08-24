#!/usr/bin/python3
""" Module definition """
# https://stackoverflow.com/questions/14992411/understanding-change-making-algorithm
# https://www.reddit.com/r/algorithms/comments/70wo52/can_someone_please_explain_this_coinchange/


def makeChange(coins, total):
    """makeChange implementation with greedy algorithm

    Returns:
        - fewest number of coins if total can be met
        - 0 if total is 0 or less
        - -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin

    if total != 0:
        return -1

    return num_coins
