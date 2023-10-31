def alphabetize(word):
    letters = list(word)
    normal_order = sorted(letters)   
    reverse_order = sorted(letters, reverse=True)   
    normal_str = ' '.join(normal_order)
    reverse_str = ' '.join(reverse_order)    
    return normal_str, reverse_str
word = input("Enter the word: ")
normal, reverse = alphabetize(word.upper())
print(f"Alphabetical Order Normal: {normal}")
print(f"Alphabetical Order Reverse: {reverse}")
