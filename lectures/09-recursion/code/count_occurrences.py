def count_occurrences_v1(lst, val):
    if len(lst) == 0:  # Θ(1)
        # base case
        return 0  # Θ(1)
    else:
        head = lst[0]  # Θ(1)
        tail = lst[1:]  # Θ(n)

        # assumption
        count_tail = count_occurrences_v1(tail, val)

        if head == val:  # Θ(1)
            return count_tail + 1  # Θ(1)
        else:
            return count_tail  # Θ(1)


def count_occurrences_v2(lst, val):
    def count_appearances_helper(lst, low, high, val):
        print(f"high: {high} | low: {low}")

        # base case
        if low == high:
            # if the only value in the list equals to the target
            if lst[low] == val:
                return 1  # return 1
            else:
                return 0  # otherwise, return 0
        else:
            # recursive case
            # assume that that this count will do its job by calling it
            # on a smaller range
            count_rest = count_appearances_helper(lst, low + 1, high, val)
            # after that count is done
            # check if the low element is the target value
            if lst[low] == val:
                # if it is, then return the count of the smaller ranger + 1
                return count_rest + 1
            else:
                # otherwise, just return the count of the smaller range
                return count_rest

    # we only do this if the list is not empty, anyway
    if len(lst) == 0:
        return 0
    else:
        return count_appearances_helper(lst, 0, len(lst) - 1, val)


if __name__ == "__main__":
    print(count_occurrences_v2([3, 5, 2, 7, 2, 5, 2, 1], 2))
