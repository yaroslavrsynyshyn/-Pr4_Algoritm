def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

n = int(input())
print_1_to_n(n)