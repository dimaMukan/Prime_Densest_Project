import math

# Cache for prime num
prime_cache = {}


def is_prime_optimised(number: int) -> bool:
    """ Memorisation, Skipping even numbers"""

    if number in prime_cache:
        return prime_cache[number]

    if number <= 1:
        prime_cache[number] = False
        return False

    if number == 2:
        prime_cache[number] = True
        return True

    if number % 2 == 0:
        prime_cache[number] = False
        return False

    limit = int(math.isqrt(number))

    for i in range(3, limit + 1, 2):
        if number % i == 0:
            prime_cache[number] = False
            return False

    prime_cache[number] = True
    return True


def prime_dense_window_optimised(S: str, W: int, N: int) -> str:
    """ Optimised version"""

    if not isinstance(S, str) or not S.isdigit():
        return "0, 0: Invalid input"
    if W <= 0 or W > len(S) or N <= 0:
        return "0, 0: Invalid input"

    max_count = 0
    best_index = 0
    best_primes_set = set()

    for i in range(len(S) - W + 1):
        current_primes = set()

        for start in range(i, i + W):
            number = 0

            for end in range(start, i + W):
                digit = int(S[end])
                number = number * 10 + digit

                if number >= N:
                    break

                if is_prime_optimised(number):
                    # Add to set primes
                    current_primes.add(number)

        if len(current_primes) > max_count:
            max_count = len(current_primes)
            best_index = i
            best_primes_set = current_primes

    if max_count == 0:
        return "0, 0: No primes found"

    best_primes = sorted(best_primes_set)

    if len(best_primes) >= 6:
        display_primes = best_primes[:3] + best_primes[-3:]
    else:
        display_primes = best_primes

    return f"{best_index}, {max_count}: " + ", ".join(map(str, display_primes))
