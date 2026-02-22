def pos_ints_list(n):
    if n == 1:
        return [1]
    else:
        smaller_list = pos_ints_list(n - 1)
        smaller_list.append(n)
        return smaller_list
    

if __name__ == "__main__":
    print(pos_ints_list(5))
