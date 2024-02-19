class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move the file pointer to the beginning
        lines = self.file.read().splitlines()
        if not lines:
            print("No books available.")
            return
        for line in lines:
            book_info = line.strip().split(',')
            book_name = book_info[0]
            author = book_info[1]
            release_year = book_info[2]
            pages = book_info[3]

            print(f"Book Name: {book_name}, Author: {author}, Release Year: {release_year}, Pages: {pages}")

    def add_book(self):
        book_title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{book_title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)  # Move the file pointer to the beginning
        lines = self.file.read().splitlines()
        updated_books = []
        removed = False
        for line in lines:
            book_info = line.strip().split(',')
            if book_info[0] != title_to_remove:
                updated_books.append(line)
            else:
                removed = True
        if not removed:
            print("Book not found.")
            return
        self.file.seek(0)  # Move the file pointer to the beginning
        self.file.truncate(0)  # Clear the file contents
        for book in updated_books:
            self.file.write(book + '\n')
        print("Book removed successfully.")

# Creating object "lib" with Library class
lib = Library("books.txt")
while True:
    # Menu
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    # User input
    choice = input("Enter your choice (1-4): ")

    # Handling user input
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        del lib  # Nesneyi silerek dosyayı kapat
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")