import time
import matplotlib.pyplot as plt


def main():
    def fibonacci_recursive(n):
        if n <= 1:
            return 1
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    def fibonacci_iterative(n):
        n1 = 0
        n2 = 1
        for _ in range(n):
            tmp = n2
            n2 += n1
            n1 = tmp
        return n2

    def fibonacci_logical(n):
        PHI = (1 + 5 ** 0.5) / 2
        return int((PHI ** (n + 1) - (1 - PHI) ** (n + 1)) / 5 ** 0.5)

    recursive_times = []
    iterative_times = []
    logical_times = []

    for i in range(0, 36):
        print("Getting data for n =", i)
        start = time.time()
        print(fibonacci_recursive(i))
        recursive_times.append(time.time() - start)
        start = time.time()
        print(fibonacci_iterative(i))
        iterative_times.append(time.time() - start)
        start = time.time()
        print(fibonacci_logical(i))
        logical_times.append(time.time() - start)

    print("Plotting graph")

    plt.plot(range(36), recursive_times, label="Recursive")
    plt.plot(range(36), iterative_times, label="Iterative")
    plt.plot(range(36), logical_times, label="Logical")
    plt.legend()
    plt.show()

    print("Done!")


if __name__ == "__main__":
    main()
