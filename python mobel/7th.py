def nth_largest_number(numbers, n):
    numbers.sort(reverse=True)
    if n <= len(numbers):
        return numbers[n - 1]
    else:
        return None

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
n = int(input("Enter N: "))
result = nth_largest_number(numbers, n)
if result is not None:
    print(f"The {n}th largest number is {result}.")
else:
    print("N is out of range.")
