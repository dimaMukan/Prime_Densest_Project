import math

def is_prime(n):
    # Basic prime check (trial division up to sqrt(n))
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

def format_output(primes_sorted):
    # If 6 or more primes -> show first 3 and last 3, otherwise show all
    if len(primes_sorted) >= 6:
        primes_sorted = primes_sorted[:3] + primes_sorted[-3:]
    return ", ".join(map(str, primes_sorted))


def prime_dense_window_set(S, W, N):
    # Basic validation
    if not S.isdigit():
        return "0, 0: Invalid input"
    if W <= 0 or W > len(S) or N <= 0:
        return "0, 0: Invalid input"

    best_index = 0
    max_count = 0
    best_primes_set = set()

    # Sliding window
    for i in range(len(S) - W + 1):
        current_primes_set = set()  # Task 3 key change

        # All substrings inside the window
        for start in range(i, i + W):
            for end in range(start, i + W):
                number = int(S[start:end + 1])

                if number < N and is_prime(number):
                    current_primes_set.add(number)

        # Update best window (ties keep earliest index automatically)
        if len(current_primes_set) > max_count:
            max_count = len(current_primes_set)
            best_index = i
            best_primes_set = current_primes_set

    if max_count == 0:
        return "0, 0: No primes found"

    best_primes_sorted = sorted(best_primes_set)
    return f"{best_index}, {max_count}: " + format_output(best_primes_sorted)


if __name__ == "__main__":
    print(prime_dense_window_set("12319", 3, 50))