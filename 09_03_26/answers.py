# Answer - 1

def print_down(n):
    if n == 0:
        return
    print(n, end=" ")
    print_down(n - 1)

print("Answer 1:")
print_down(5)
print()

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

