def is_composite(number):
    if number < 4:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
composite_count = sum(1 for num in numbers if is_composite(num))
print("Number of composite numbers:", composite_count)
