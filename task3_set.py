import time
import math


def is_prime(number: int) -> bool:
    """Return True if number is prime using trial division up to sqrt(number)."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_dense_window_set(S: str, W: int, N: int) -> str:
    """
    Find the window of length W with the maximum count of unique primes
    formed by all substrings inside the window (numbers must be < N).

    Task 3 change vs Task 2: use a SET to store unique primes (fast membership).
    """
    if not isinstance(S, str) or not S.isdigit():
        return "0, 0: Invalid input"
    if W <= 0 or W > len(S) or N <= 0:
        return "0, 0: Invalid input"

    max_count = 0
    best_index = 0
    best_primes_set: set[int] = set()

    # Slide the window
    for i in range(len(S) - W + 1):
        current_primes: set[int] = set()  # key change: set instead of list

        # Generate all substrings inside the window
        for start in range(i, i + W):
            for end in range(start, i + W):
                number = int(S[start:end + 1])
                if number < N and is_prime(number):
                    current_primes.add(number)

        # Update maximum (ties keep the earliest index automatically)
        if len(current_primes) > max_count:
            max_count = len(current_primes)
            best_index = i
            best_primes_set = current_primes

    if max_count == 0:
        return "0, 0: No primes found"

    best_primes = sorted(best_primes_set)

    # Format output: show first 3 and last 3 if 6+ primes, otherwise show all
    if len(best_primes) >= 6:
        display_primes = best_primes[:3] + best_primes[-3:]
    else:
        display_primes = best_primes

    return f"{best_index}, {max_count}: " + ", ".join(map(str, display_primes))


if __name__ == "__main__":
    # Example manual test
    S = "12319"
    W = 3
    N = 50

    t0 = time.time()
    print("Output:", prime_dense_window_set(S, W, N))
    print("Time taken:", time.time() - t0, "seconds")