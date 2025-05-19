import csv

# Class representing a physical book
class Book:
    def __init__(self, title, author, publisher, page_count, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Pages: {self.page_count}, Price: £{self.price:.2f}"

# Subclass representing an eBook, inheriting from Book
class EBook(Book):
    def __init__(self, title, author, publisher, page_count, price, file_size, file_format):
        super().__init__(title, author, publisher, page_count, price)
        self.file_size = file_size
        self.file_format = file_format

    def __str__(self):
        return f"{super().__str__()}\nFile Size: {self.file_size} MB, Format: {self.file_format}"

# Function to load books from a CSV file
def load_books(filename='books.txt'):
    books = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)  # Skip header row
        for line in reader:
            book = Book(line[0], line[1], line[2], int(line[3]), float(line[4]))
            books.append(book)
    return books

# Function to save books to a CSV file
def save_books(books, filename='books.txt'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['Title', 'Author', 'Publisher', 'Pages', 'Price'])
        for book in books:
            writer.writerow([book.title, book.author, book.publisher, book.page_count, book.price])

# Function to add a book to the list
def add_book(books, prompt_func, cls):
    while True:
        choice = input("\n(B)ook or (E)book: ").lower()
        title = input(prompt_func("Enter book title: "))
        author = input(prompt_func("Enter book author: "))
        publisher = input(prompt_func("Enter book publisher: "))
        page_count = int(input(prompt_func("Enter number of pages: ")))
        price = float(input(prompt_func("Enter book price: ")))

        if choice == 'b':
            books.append(cls(title, author, publisher, page_count, price))

        elif choice == 'e':
            file_size = float(input(prompt_func("Enter ebook file size (MB): ")))
            file_format = input(prompt_func("Enter ebook file format: "))
            books.append(EBook(title, author, publisher, page_count, price, file_size, file_format))

        choice = input("Enter another book or (q)uit: ").lower()
        if choice == 'q':
            break

# Main function to run the program
def main():
    # Load existing books from file
    books = load_books()

    print("Current books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")

    while True:
        choice = input("\nWhat would you like to do? (A)dd, (V)iew, (S)ave, (Q)uit: ").upper()

        if choice == 'A':
            # Add a new book (either physical or eBook)
            add_book(books, lambda s: s.capitalize(), Book)
        elif choice == 'V':
            print("\nCurrent books:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        elif choice == 'S':
            save_books(books)
            print("Books saved successfully.")
        elif choice == 'Q':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program if executed directly
if __name__ == "__main__":
    main()
