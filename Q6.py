
class Library:
    def __init__(self, acc_number, title, author, publisher):
        self.acc_number = acc_number
        self.title = title
        self.author = author
        self.publisher = publisher

    def read(self):
        print(f"Accession Number: {self.acc_number}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")

    def compute(self, days_late):
        fine = lambda days: days * 5 
        total_fine = fine(days_late)
        print(f"Number of Days Late: {days_late}")
        print(f"Fine Charged: Rupees {total_fine}")

    def display(self):
        print("Book Details:")
        print(f"Accession Number: {self.acc_number}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")



if __name__ == "__main__":
   
    book = Library("A123", "Python Programming", "Abhijeet", "TechBooks Inc.")
    print("Reading Book Details:")
    book.read()  

    print("\nCalculating Fine for 7 Days Late:")
    book.compute(7)  
    print("\nDisplaying Book Details Again:")
    book.display()  


# output
# Reading Book Details:
# Accession Number: A123
# Title: Python Programming
# Author: Abhijeet
# Publisher: TechBooks Inc.

# Calculating Fine for 7 Days Late:     
# Number of Days Late: 7
# Fine Charged: Rupees 35

# Displaying Book Details Again:        
# Book Details:
# Accession Number: A123
# Title: Python Programming
# Author: Abhijeet
# Publisher: TechBooks Inc.
# PS D:\MCA1-2\python>