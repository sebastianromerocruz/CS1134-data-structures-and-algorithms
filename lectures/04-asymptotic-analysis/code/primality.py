from math import sqrt


def is_prime_naive(num):
    divisor_count = 0

    for curr in range(1, num + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 2 # that is, only 1 and num


def is_prime_left_half(num):
    divisor_count = 0

    for curr in range(1, num // 2 + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 1 # that is, only 1


def is_prime_left_half(num):
    divisor_count = 0

    for curr in range(1, sqrt(num) + 1):
        if num % curr == 0:
            divisor_count += 1
    
    return divisor_count == 1 # that is, only 1


def main():
    num = 13
    print(f"{num} is a prime number: {is_prime_left_half(num)}")

    num = 12
    print(f"{num} is a prime number: {is_prime_left_half(num)}")

if __name__ == "__main__":
    main()