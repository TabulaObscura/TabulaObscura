"""Find prime numbers by iterating through integers.

For each number:
  1. 2 is the only even prime, so any other even number is skipped.
  2. An odd number is checked against the previous odd numbers (3, 5, 7, ...).
     If any of them divides it evenly, it is not prime.
  3. Numbers that pass are stored in the `primes` array.

Only odd divisors up to the square root of the number need to be tried:
if n = a * b, at least one of a or b must be <= sqrt(n).
"""

import sys


def is_prime(n):
    """Return True if n is prime, using the odd-divisor check."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # even numbers greater than 2 are not prime
        return False

    divisor = 3
    while divisor * divisor <= n:  # previous odd numbers up to sqrt(n)
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def find_primes(limit):
    """Iterate from 2 to limit and return an array of the primes found."""
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    primes = find_primes(limit)
    print(f"Primes up to {limit}: {primes}")
    print(f"Found {len(primes)} primes.")


if __name__ == "__main__":
    main()
