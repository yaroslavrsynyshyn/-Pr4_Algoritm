def is_power_of_two(n):
    if n == 1:
        return "YES"
    if n <= 0 or n % 2 != 0:
        return "NO"
    return is_power_of_two(n // 2)

n = int(input())
print(is_power_of_two(n))