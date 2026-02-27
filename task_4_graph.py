import time
import matplotlib.pyplot as plt

from task2_list import prime_dense_window
from task3_set import prime_dense_window_set
from task_4 import prime_dense_window_optimised

PI_100 = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def make_tests():
    #test cases
    return [
        (PI_100[:10], 2, 50),
        (PI_100[:10], 4, 5_000),
        (PI_100[:20], 6, 5_000),
        (PI_100[:20], 8, 500_000),
        (PI_100[:40], 8, 500_000),
        (PI_100[:40], 10, 50_000_000),
        (PI_100[:60], 12, 500_000_000),
        (PI_100[:60], 14, 500_000_000),
        (PI_100[:80], 16, 5_000_000_000),
        (PI_100[:100], 20, 500_000_000_000),
    ]

def measure(func, S, W, N):
    start = time.perf_counter()
    func(S, W, N)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    tests = make_tests()
    task2_times = []
    task3_times = []
    task4_times = []
    print("Running main benchmark...\n")

    for i, (S, W, N) in enumerate(tests, 1):
        t2 = measure(prime_dense_window, S, W, N)
        t3 = measure(prime_dense_window_set, S, W, N)
        t4 = measure(prime_dense_window_optimised, S, W, N)
        task2_times.append(t2)
        task3_times.append(t3)
        task4_times.append(t4)
        print(f"Test {i}:")
        print(f"  Task 2: {t2:.6f} sec")
        print(f"  Task 3: {t3:.6f} sec")
        print(f"  Task 4: {t4:.6f} sec\n")
    x = list(range(1, len(tests) + 1))

    # -------- FIRST GRAPH --------
    plt.figure(figsize=(9, 5))

    plt.plot(x, task2_times, marker='o')
    plt.plot(x, task3_times, marker='s')
    plt.plot(x, task4_times, marker='^')

    plt.yscale("log")
    plt.xlabel("Test Case Number")
    plt.ylabel("Runtime (seconds)")
    plt.title("Performance Comparison: Task 2 vs Task 3 vs Task 4")
    plt.legend(["Task 2 (List)", "Task 3 (Set)", "Task 4 (Optimised)"])
    plt.grid(True)

    plt.show()

    # -------- SECOND GRAPH --------

    fixed_S = PI_100[:80]
    fixed_N = 5_000_000_000

    window_sizes = [2, 4, 6, 8, 10, 12, 14, 16]

    task2__times = []
    task3__times = []
    task4__times = []

    print("Running window size benchmark...\n")

    for W in window_sizes:
        t2 = measure(prime_dense_window, fixed_S, W, fixed_N)
        t3 = measure(prime_dense_window_set, fixed_S, W, fixed_N)
        t4 = measure(prime_dense_window_optimised, fixed_S, W, fixed_N)

        task2__times.append(t2)
        task3__times.append(t3)
        task4__times.append(t4)

        print(f"W={W}:  T2={t2:.6f}  T3={t3:.6f}  T4={t4:.6f}")

    plt.figure(figsize=(9, 5))

    plt.plot(window_sizes, task2__times, marker='o')
    plt.plot(window_sizes, task3__times, marker='s')
    plt.plot(window_sizes, task4__times, marker='^')

    plt.yscale("log")  # important to see Task 2 vs Task 3 difference
    plt.xlabel("Window Size (W)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Window Size")
    plt.legend(["Task 2", "Task 3", "Task 4"])
    plt.grid(True)

    plt.show()