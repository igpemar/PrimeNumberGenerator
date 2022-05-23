import time
from primefinder import *

N = 1000
print(f"Finding the first {N} prime numbers...")
print("Algorithm: old brute force.")
start_1 = time.time()
primes_1 = first_N_prime_numbers(N, False)
end_1 = time.time()


print("Elapsed time: " + str(round(end_1 - start_1, 3)) + " s.")
print("Checking results with 30k optimization...")
if is_all_array_primes_30k(primes_1, True):
    print("---> Array is entirely prime.")
    print(f"Last 5 primes: {primes_1[-5:]}")
    print(f"Prime density: {round(len(primes_1)/primes_1[-1]*100,1)} %")
else:
    print("ARRAY NOT PRIME.")
print("\n")

N = 1000000
print(f"Printing all the the prime numbers up to {N} ...")
print("Algorithm: Sieve of Eratosthenes.")
start_2 = time.time()
primes_2 = prime_numbers_smaller_than_N_sieve_Eratho(N, False)
end_2 = time.time()
print("Elapsed time: " + str(round(end_2 - start_2, 4)) + " s.")
print("Checking results with 30k optimization...")
if is_all_array_primes_30k(primes_2, True):
    print("---> Array is entirely prime.")
    print(f"Last 5 primes: {primes_2[-5:]}")
    print(f"Total primes found: {len(primes_2)}.")
    print(f"Prime density: {round(len(primes_2)/N*100,1)} %")
else:
    print("ARRAY NOT PRIME.")
print("\n")

print(f"Printing all the the prime numbers up to {N} ...")
print("Algorithm: Sieve of Sundaram.")
start_3 = time.time()
primes_3 = prime_numbers_smaller_than_N_sieve_Sundaram(N, False)
end_2 = time.time()
print("Elapsed time: " + str(round(end_2 - start_3, 4)) + " s.")
print("Checking results with 30k optimization...")
if is_all_array_primes_30k(primes_3, True):
    print("---> Array is entirely prime.")
    print(f"Last 5 primes: {primes_3[-5:]}")
    print(f"Total primes found: {len(primes_3)}.")
    print(f"Prime density: {round(len(primes_3)/N*100,1)} %")
else:
    print("ARRAY NOT PRIME.")
print("\n")
