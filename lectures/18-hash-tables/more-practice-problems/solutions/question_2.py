from ChainingHashTableMap import ChainingHashTableMap


def intersection_list_worst(lst1, lst2):
    """
    Best worst-case runtime: Θ(n log n).

    Sort both lists, then walk them with two pointers. No hash table means no
    worst-case O(n²) collision behaviour — the sort dominates at O(n log n).
    """
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    result = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            result.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1

    return result


def intersection_list_average(lst1, lst2):
    """
    Best average-case runtime: Θ(n) expected.

    Load one list into a ChainingHashTableMap (O(n) average), then scan the
    other and check membership (O(1) expected per element). Total: O(n) average.
    Worst case is O(n²) if every hash key collides, but that is not expected.
    """
    seen = ChainingHashTableMap()
    
    for val in lst1:
        seen[val] = True

    return [val for val in lst2 if val in seen]
