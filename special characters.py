def count_special_characters(statement):
    special_characters = "!@#$%^&*()_+{}[]|\/:;<>,.?`~"
    count = 0
    for char in statement:
        if char in special_characters:
            count += 1
    return count
given_statement = "Modi Birthday @ September 17, #&amp;$% is the wishes code for him."
special_count = count_special_characters(given_statement)
print(f"Number of special Characters: {special_count}")
