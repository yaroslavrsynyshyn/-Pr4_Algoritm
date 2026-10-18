def print_digits_reversed(n):
    print(n % 10, end=" ")
    if n >= 10:
        print_digits_reversed(n // 10)

n = int(input())
print_digits_reversed(n)