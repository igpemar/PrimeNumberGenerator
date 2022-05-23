import math


def first_N_prime_numbers(N: int, print_flag: bool = False) -> list:
    primes = [0] * N
    if N <= 0:
        printif(primes, print_flag)
        return primes
    elif N == 1:
        printif(2, print_flag)
        return [2]
    else:
        candidate, primes[0], idx = 3, 2, 1
        printif(primes[0], print_flag)
        while idx < N:
            if is_prime(candidate):
                primes[idx] = candidate
                printif(primes[idx], print_flag)
                idx += 1
            candidate += 2
        return primes


def prime_numbers_smaller_than_N(N: int, print_flag: bool = False):
    primes = [True] * N
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        if primes[i]:
            j = i**2
            while j <= N - 1:
                primes[j] = False
                j = j + i
    A, idx = [0] * primes[2:].count(True), 0
    for i in range(2, N):
        if primes[i]:
            A[idx] = i
            idx += 1

    return A


def printif(value, print_flag: bool = False):
    if print_flag:
        print(value)


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    max_div = math.floor(math.sqrt(number))
    for divider in range(2, max_div + 1):
        if number % divider == 0:
            return False
    return True


def is_all_array_prime(primes):
    for prime in primes:
        if not is_prime(prime):
            return False
    return True
