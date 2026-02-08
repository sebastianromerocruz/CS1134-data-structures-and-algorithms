def binary_search(sorted_list: list, val: int) -> int:
    """
    Performs binary search on a list of integers, returning the index of the
    target integer or None if not found.

    Args:
        sorted_list (list): The int list to be search
        val (int): The target value we search for

    Returns:
        int: The index of the target value, None if not found
    """
    start = 0                    # Θ(1)
    stop = len(sorted_list) - 1  # Θ(1)

    # Θ(number of iterations, k)
    while start <= stop:
        med_idx = (stop + start) // 2  # Θ(1)

        # Θ(1)
        if sorted_list[med_idx] == val:
            return med_idx
        elif sorted_list[med_idx] > val:
            stop = med_idx - 1
        else:
            start = med_idx + 1
        
    return None  # Θ(1)

def main():
    lst = [1, 2, 3, 4, 5, 6]

    print(binary_search(lst, 9))


if __name__ == "__main__":
    main()
