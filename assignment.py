# Exercise 1
def print_love_python():
    for i in range(10):
        print("I Love Python")


# Exercise 2
def sum_of_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Exercise 3
def count_divisible_by_7():
    count = 0
    for i in range(1, 101):
        if i % 7 == 0:
            count += 1
    return count


# Exercise 4
def print_cubes():
    for i in range(1, 11):
        print(i ** 3)


# Exercise 5
def print_from_five_to(n):
    if n >= 5:
        for i in range(5, n + 1):
            print(i)
    else:
        for i in range(5, n - 1, -1):
            print(i)
