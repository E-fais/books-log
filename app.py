import pandas as pd

books = {'Name': [], 'Author': [], 'Type': [], 'Notes': []}

def start_app():
    while True:
        print('BOOK OF BOOKS\n----------')
        choice = input('Reply with 1 or 2 \n 1.View books \n 2.Add new book:\n')
        if choice == '1':
            try:
                books_df = pd.read_csv('books.csv', sep='\t')  # Debug: Changed 'books' to 'books_df'
                print(books_df)
            except FileNotFoundError:
                print('No books found!')           

        elif choice == '2':
            name = input('name of the book : ')
            author = input('name of the author : ')
            book_type = input('type : ')  # Debug: Changed 'type' to 'book_type' to avoid conflict with built-in type
            notes = input('notes : ')
            add_book(name, author, book_type, notes)  # Debug: Changed 'type' to 'book_type'
            books_data = pd.DataFrame(books)
            books_data.to_csv('books.csv', sep='\t', index=False)
            print('book saved successfully!')
            
        else:
            print('\n enter a valid input \n')
        
        exit = input('continue program..? (y/n)')
        if exit.lower() == 'y':
            pass
        else:
            print('program terminated')  # Debug: Added 'print' to show termination message
            break

def add_book(name, author, book_type, notes):  # Debug: Changed 'type' to 'book_type'
    books['Name'].append(name)
    books['Author'].append(author)
    books['Type'].append(book_type)  # Debug: Changed 'type' to 'book_type'
    books['Notes'].append(notes)

start_app()
