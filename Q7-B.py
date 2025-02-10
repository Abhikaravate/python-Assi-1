A = str(input("Enter the String "))

words = A.split()

five_char_words = [word for word in words if len(word) == 5]

print("5-character-long words:", five_char_words)

# PS D:\MCA1-2\python> python Q7-B.py
# Enter the String i am omkar        
# 5-character-long words: ['omkar']   
