
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(title, author):
    
    new_book = (title, author)
    
    if new_book in library:
        print(f"The book '{title}' by {author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added to the library.")
        
add_book("To Kill a Mockingbird", "Harper Lee")
add_book("1984", "George Orwell")  # This should not be added as a duplicate put it just for example
add_book("The Great Gatsby", "F. Scott Fitzgerald")

print("Current library contents:")
for book in library:
    print(f"{book[0]} by {book[1]}")
