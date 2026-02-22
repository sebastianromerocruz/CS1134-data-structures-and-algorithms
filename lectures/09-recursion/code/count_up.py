def count_up(start, end):
    if start == end:
        # the base case
        print(start)
    else:
        # the recursive step
        count_up(start, end - 1)
        print(end)


def main():
    count_up(1, 5)


if __name__ == "__main__":
    main()
