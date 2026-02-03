def print_square_a(n):
    for i in range(1, n + 1):
        line = '*' * n
        print(line)


def print_square_b(n):
    for i in range(1, n + 1):
        line = '*' * i
        print(line)


def prefix_avg_lst(lst):
    n = len(lst)      # Θ(n)
    result = [0] * n  # Θ(n)

    # Θ(n)
    for i in range(n):
        curr_sum = sum(lst[0:i + 1])  # Θ(i), which we established is Θ(n)
        curr_avg = curr_sum / (i + 1)   # Θ(1)
        result[i] = curr_avg          # Θ(i)
    
    return result  # Θ(1)


def prefix_avg_sum(lst):
    n = len(lst)      # Θ(n)
    result = [0] * n  # Θ(n)
    curr_sum = 0      # Θ(1)

    # Θ(n)
    for i in range(n):
        curr_sum += lst[i]              # Θ(1)
        curr_avg  = curr_sum / (i + 1)  # Θ(1)
        result[i] = curr_avg            # Θ(i)
        
    return result  # Θ(1)


def main():
    print_square_a(4)
    print_square_b(4)
    print(prefix_avg_lst([10, 20, 30, 40, 50]))
    print(prefix_avg_sum([10, 20, 30, 40, 50]))


if __name__ == "__main__":
    main()