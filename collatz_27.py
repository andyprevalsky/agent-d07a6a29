def collatz_sequence(start):
    sequence = [start]
    n = start
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    start = 27
    sequence = collatz_sequence(start)
    for number in sequence:
        print(number)
    transitions = len(sequence) - 1
    print(f"Total transitions to reach 1: {transitions}")


if __name__ == "__main__":
    main()
