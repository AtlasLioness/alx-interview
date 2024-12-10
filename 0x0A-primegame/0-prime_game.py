#!/usr/bin/python3
""" Module to find the winner of the prime game """


def isWinner(x, nums):
    """ function to determine the winner of each game """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
