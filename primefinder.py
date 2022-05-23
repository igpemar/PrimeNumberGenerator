import time
import math


def first_N_prime_numbers(N: int, print_flag: bool = False) -> list:
    """This function provides the first N prime numbers using the
    up to N."""
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


def prime_numbers_smaller_than_N_sieve_Eratho(N: int, print_flag: bool = False):
    """This function provides all the prime numbers in the range [0;N] using
    the sieve of Erathosthenes algorithm."""
    if N < 2:
        return []
    A = [True] * (N + 1)
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        if A[i]:
            j = i**2
            while j <= N:
                A[j] = False
                j = j + i
    primes, idx = [0] * A[2:].count(True), 0
    for i in range(2, N + 1):
        if A[i]:
            primes[idx] = i
            idx += 1

    return primes


def prime_numbers_smaller_than_N_sieve_Sundaram(n: int, print_flag: bool = False):
    """This function provides all the prime numbers in the range [0;N] using
    the sieve of Sundaram algorithm."""
    if n < 2:
        return []
    elif n == 2:
        return [2]

    k = math.floor((n - 1) / 2)
    A = [True] * (k + 1)
    for i in range(1, math.floor(math.sqrt(k)) + 1):
        if A[i]:
            j = i
            while i + j + 2 * i * j <= k:
                A[i + j + 2 * i * j] = False
                j += 1
            # end
    # end
    primes, idx = [0] * (A.count(True)), 1
    primes[0] = 2
    printif(primes[0], print_flag)
    for i in range(1, (k + 1)):
        if A[i]:
            primes[idx] = 2 * i + 1
            printif(primes[idx], print_flag)
            idx += 1

    return primes


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


def is_prime_2k(number: int) -> bool:
    if number <= 3:
        return number > 1
    if not number % 2:
        return False
    max_div = math.floor(math.sqrt(number))
    for divider in range(3, max_div + 1, 2):
        if number % divider == 0:
            return False
    return True


def is_prime_6k(number: int) -> bool:
    if number <= 3:
        return number > 1
    if not number % 2 or not number % 3:
        return False
    max_div = math.floor(math.sqrt(number))
    for divider in range(5, max_div + 1, 6):
        if not number % divider or not number % (divider + 2):
            return False
    return True


def is_prime_30k(number: int) -> bool:
    if number <= 3:
        return number > 1
    elif number == 5:
        return number
    if not number % 2 or not number % 3 or not number % 5:
        return False
    max_div = math.floor(math.sqrt(number))
    for divider in range(7, max_div + 1, 30):
        if (
            not number % divider
            or not number % (divider + 2)
            or not number % (divider + 4)
            or not number % (divider + 10)
            or not number % (divider + 12)
            or not number % (divider + 16)
            or not number % (divider + 22)
            or not number % (divider + 24)
        ):
            return False
    return True


def is_all_array_primes(primes, print_flag: bool = False):
    start = time.time()
    for prime in primes:
        if not is_prime(prime):
            if print_flag:
                print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
            return False
    if print_flag:
        print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
    return True


def is_all_array_primes_2k(primes, print_flag: bool = False):
    start = time.time()
    for prime in primes:
        if not is_prime_2k(prime):
            if print_flag:
                print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
            return False
    if print_flag:
        print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
    return True


def is_all_array_primes_6k(primes, print_flag: bool = False):
    start = time.time()
    for prime in primes:
        if not is_prime_6k(prime):
            if print_flag:
                print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
            return False
    if print_flag:
        print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
    return True


def is_all_array_primes_30k(primes, print_flag: bool = False):
    start = time.time()
    for prime in primes:
        if not is_prime_30k(prime):
            if print_flag:
                print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
            return False
    if print_flag:
        print("--> Check time: " + str(round(time.time() - start, 4)) + " s.")
    return True
