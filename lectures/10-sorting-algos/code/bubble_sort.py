def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        for j in range(n - i - 1):
            # These print statements are, of course,
            # not part of the implementations
            print(f"lst[{j}] -> {lst[j]}")
            print(f"lst[{j + 1}] -> {lst[j + 1]}")

            if lst[j] > lst[j + 1]:
                # swap
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp

                print("Swap!")  # not part of implementation
            else:
                print("No swap.")  # not part of implementation

            print(lst, end="\n\n")  # not part of implementation


if __name__ == "__main__":
    lst = [5, 8, 6, 1, 9, 3, 0, 1]

    bubble_sort(lst)
    print(lst)
