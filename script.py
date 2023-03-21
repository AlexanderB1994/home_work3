# 1
def sum_int_float(*args, **kwargs):
    numbers = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            numbers += arg
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            numbers += value
    return numbers


print(sum_int_float(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_int_float())
print(sum_int_float(2, 4, 'abc', param1=2))


# 2
def calculate_sums(num):
    if num == 0:
        return 0, 0, 0
    else:
        sums = calculate_sums(num - 1)
        even_sum_ = sums[0] + num if num % 2 == 0 else sums[0]
        odd_sum_ = sums[1] + num if num % 2 == 1 else sums[1]
        total_sum = sums[2] + num
        return even_sum_, odd_sum_, total_sum


while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

all_sum, even_sum, odd_sum = calculate_sums(n)[2], calculate_sums(n)[0], calculate_sums(n)[1]

print("The sum of all numbers from 0 to", n, "is:", all_sum)
print("The sum of all even numbers from 0 to", n, "is:", even_sum)
print("The sum of all odd numbers from 0 to", n, "is:", odd_sum)


# 3
def read_integer_from_input():
    try:
        value = int(input("Enter an integer number: "))
        return value
    except ValueError:
        return 0
