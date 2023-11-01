def find_character(char, string):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

string = input("Enter a string: ")
char = input("Enter a character to search for: ")
index = find_character(char, string)
if index != -1:
    print(f"The character '{char}' is present at index {index}.")
else:
    print(f"The character '{char}' is not found in the string.")
