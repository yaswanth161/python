def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

n = int(input("Enter an N-digit number: "))
result = digit_sum(n)
print("Sum of digits:", result)
