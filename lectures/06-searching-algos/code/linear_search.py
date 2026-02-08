def linear_search(lst: list, val: int) -> int:
    """
    Checks the elements of a list for a specified value, returning the index
    location of that value if found in the list, or None otherwise. 

    Args:
        lst (list): A list of integers
        val (int): An integer value

    Returns:
        int: The index of the location of val within lst, None if not found
    """
    # Θ(n)
    for i in range(len(lst)):
        # Θ(1)
        if (lst[i] == val):
            return i  # Θ(1)
    
    return None  # Θ(1)


def main():
    integers = [5, 8, 12, 7, 8, 10]

    print(linear_search(integers, 8))
    print(linear_search(integers, 4))


if __name__ == "__main__":
    main()
