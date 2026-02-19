import time
import math


def is_prime(number):
    """Basic prime checking using trial division"""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


def prime_dense_window(S, W, N):
    # Check if input string is numeric
    if not S.isdigit():
        return "0, 0: Invalid input"

    max_count = 0
    best_index = 0
    best_primes = []

    # Slide the window
    for i in range(len(S) - W + 1):

        current_primes = []

        # Generate all substrings inside the window
        for start in range(i, i + W):
            for end in range(start, i + W):

                sub = S[start:end + 1]
                number = int(sub)

                if number < N and is_prime(number):
                    if number not in current_primes:
                        current_primes.append(number)

        # Update maximum
        if len(current_primes) > max_count:
            max_count = len(current_primes)
            best_index = i
            best_primes = current_primes.copy()

    # If no primes found
    if max_count == 0:
        return "0, 0: No primes found"

    # Sort primes
    best_primes.sort()

    # Format output
    if len(best_primes) >= 6:
        display_primes = best_primes[:3] + best_primes[-3:]
    else:
        display_primes = best_primes

    return f"{best_index}, {max_count}: " + ", ".join(map(str, display_primes))


# ---------------------------
# Example manual test
# ---------------------------

if __name__ == "__main__":
    S = "12319"
    W = 3
    N = 50

    start_time = time.time()
    result = prime_dense_window(S, W, N)
    end_time = time.time()

    print("Output:", result)
    print("Time taken:", end_time - start_time, "seconds")