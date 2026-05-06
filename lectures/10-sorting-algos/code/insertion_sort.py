def insertion_sort(lst):
    # Θ(n)
    for curr_idx in range(1, len(lst)):
        curr = lst[curr_idx]  # Θ(1)
        j = curr_idx  # Θ(1)

        print(f"- PASS #{curr_idx}:\n")
        print(f"idx -> {j}")
        print(f"Current (lst[idx]) -> {curr}")
        print("List before insertion:", lst)

        print("-----------------------------------------------------------------")
        print("Inserting...")
        # Θ(curr_idx) === Θ(n)
        print(
            f"[idx: {j}] Is lst[idx - 1] ({lst[j - 1]}) > current ({curr})? {'Yes' if lst[j - 1] > curr else 'No, so we stop here.'}"
        )
        while j >= 1 and lst[j - 1] > curr:
            print(f"Then SWAP! lst[{j}] ({lst[j]}) <-> lst[{j - 1}] ({lst[j - 1]})\n")

            lst[j] = lst[j - 1]  # Θ(1)
            j -= 1  # Θ(1)

            if j > 0:
                print(
                    f"[idx: {j}] Is lst[idx - 1] ({lst[j - 1]}) > current ({curr})? {'Yes' if lst[j - 1] > curr else 'No, so we stop here.'}"
                )

        lst[j] = curr

        print("-----------------------------------------------------------------")
        print(f"List after insertion: {lst}\n\n")


if __name__ == "__main__":
    lst = [5, 8, 6, 1, 9, 3, 0, 2]

    insertion_sort(lst)
    print(lst)
