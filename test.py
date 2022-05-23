import time
from primefinder import (
    first_N_prime_numbers,
    prime_numbers_smaller_than_N,
    is_all_array_prime,
)

N = 1000
print(f"Finding the first {N} prime numbers by brute force ...")
start_1 = time.time()
primes_1 = first_N_prime_numbers(N, False)
end_1 = time.time()

print("Elapsed time: " + str(round(end_1 - start_1, 3)) + " s.")
if is_all_array_prime(primes_1):
    print("Checking results...")
    print("---> Array is entirely prime.")
    print(f"Last 5 primes: {primes_1[-5:]}")
    print(f"Prime density: {round(len(primes_1)/primes_1[-1]*100,1)} %")
else:
    print("ARRAY NOT PRIME.")
print("\n")

N = 10000000
print(f"Printing all the the prime numbers up to {N} ...")
start_2 = time.time()
primes_2 = prime_numbers_smaller_than_N(N, False)
end_2 = time.time()
print("Elapsed time: " + str(round(end_2 - start_2, 3)) + " s.")
if is_all_array_prime(primes_2):
    print("Checking results...")
    print("---> Array is entirely prime.")
    print(f"Last 5 primes: {primes_2[-5:]}")
    print(f"Total primes found: {len(primes_2)}.")
    print(f"Prime density: {round(len(primes_2)/N*100,1)} %")
else:
    print("ARRAY NOT PRIME.")
