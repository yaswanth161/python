text = input("Enter text: ")
sentences = text.split('.')
count = sum(1 for sentence in sentences if sentence.strip().startswith('B'))
print("Number of sentences starting with 'B':", count)
