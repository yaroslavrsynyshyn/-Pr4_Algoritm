def print_a_to_b(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        print_a_to_b(a + 1, b)
    else:
        print_a_to_b(a - 1, b)

a = int(input())
b = int(input())
print_a_to_b(a, b)