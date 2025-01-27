A = str(input("Enter the String "))

words = A.split()

five_char_words = [word for word in words if len(word) == 5]

print("5-character-long words:", five_char_words)


