# Answer - 1

def print_down(n):
    if n == 0:
        return
    print(n, end=" ")
    print_down(n - 1)

print("Answer 1:")
print_down(5)
print("\n")

print("-------------")

# Answer - 2

def sum_odd(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return sum_odd(n - 1)
    else:
        return n + sum_odd(n - 1)

print("Answer 2:")
print(sum_odd(7))
print()

print("-------------")

# Answer - 3

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

print("Answer 3:")
print(power(2, 4))
print()

print("-------------")

# Answer - 4

def max_in_list(lst: list):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], max_in_list(lst[1: ]))

print("Answer 4:")
print(max_in_list([3, 8, 2, 15, 6]))
print()

print("-------------")

# Answer - 5

def count_even(lst: list):
    if len(lst) == 0:
        return 0
    else:
        if lst[0] % 2 == 0:
            return 1 + count_even(lst[1:])
        else:
            return count_even(lst[1: ])

print("Answer 5:")
print(count_even([2, 5, 8, 7, 6, 3, 10]))
print()

print("-------------")

# Bonus

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

print("Bonus:")
print(sum_digits(583))
print()