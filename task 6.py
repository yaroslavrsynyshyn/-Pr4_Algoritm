def print_digits_direct(n):
    if n >= 10:
        print_digits_direct(n // 10)
    print(n % 10, end=" ")

n = int(input())
print_digits_direct(n)