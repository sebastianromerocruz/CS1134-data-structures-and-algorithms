def swap(lst, curr, min_idx):
    temp = lst[curr]
    lst[curr] = lst[min_idx]
    lst[min_idx] = temp


def selection_sort(lst):
    n = len(lst)
    for curr in range(n):
        min_idx = curr
        for j in range(curr + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        swap(lst, curr, min_idx)

        # These print statements are, of course,
        # not part of the implementation
        print(lst)

        print("Curr:", curr)
        print("Min idx:", min_idx, end="\n\n")


if __name__ == "__main__":
    lst = [5, 8, 12, 7, 8, 10]

    selection_sort(lst)
    print(lst)
