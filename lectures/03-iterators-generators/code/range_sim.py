def simulated_range(start, stop, step=1):
    """
    Returns a list simulating a generator returned by built-in range:

    Args:
        start (int): The first element of the list.
        stop (int): The cap of the list, making its final element stop-1.
        step (int, optional): By how many integers we skip elements. Defaults to 1.

    Returns:
        list: A list of integers.
    """
    result = []

    current = start

    while current < stop:
        result.append(current)
        current += step
    
    return result


def main():
    """
    Driver
    """
    print("Built-in range...")
    for elem in range(3, 10, 2):
        print(elem)

    print("Simulated range...")
    for elem in simulated_range(3, 10, 2):
        print(elem)


if __name__ == "__main__":
    main()