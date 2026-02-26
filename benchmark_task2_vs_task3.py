import time
from task2_list import prime_dense_window
from task3_set import prime_dense_window_set

PI_100 = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"


def make_tests():
    return [
        (PI_100[:10], 2, 50, "First 10 digits of Pi"),
        (PI_100[:10], 4, 5_000, "First 10 digits of Pi"),
        (PI_100[:20], 6, 5_000, "First 20 digits of Pi"),
        (PI_100[:20], 8, 500_000, "First 20 digits of Pi"),
        (PI_100[:40], 8, 500_000, "First 40 digits of Pi"),
        (PI_100[:40], 10, 50_000_000, "First 40 digits of Pi"),
        (PI_100[:60], 12, 500_000_000, "First 60 digits of Pi"),
        (PI_100[:60], 14, 500_000_000, "First 60 digits of Pi"),
        (PI_100[:80], 16, 5_000_000_000, "First 80 digits of Pi"),
        (PI_100[:100], 20, 500_000_000_000, "First 100 digits of Pi"),
    ]


def timed_run(func, S, W, N, limit_seconds=60):
    t0 = time.time()
    out = func(S, W, N)
    elapsed = time.time() - t0
    if elapsed > limit_seconds:
        return out, f">{limit_seconds}"
    return out, f"{elapsed:.4f}"


if __name__ == "__main__":
    tests = make_tests()

    print("Case | Description | Task2 | Task3 | Outputs match")
    print("-" * 70)

    for idx, (S, W, N, desc) in enumerate(tests, 1):
        out2, t2 = timed_run(prime_dense_window, S, W, N)
        out3, t3 = timed_run(prime_dense_window_set, S, W, N)
        print(f"{idx:>4} | {desc:<20} | {t2:>6} | {t3:>6} | {out2 == out3}")