num1 = 5
num2 = 7
num3 = 9
total = 0
for i in range(1, 4):
    if i == 1:
        total += num1
    elif i == 2:
        total += num2
    else:
        total += num3
counter = 1
while counter <= 3:
    total += counter
    counter += 1
print("The sum of the three numbers and 1 to 3 is:", total)
