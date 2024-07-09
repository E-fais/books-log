import pandas as pd

books={'Name':[],'Author':[],'Type':[],'Notes':[]}

def start_app():
    while True:
         print('BOOK OF BOOKS\n----------')
         choice=input('Reply with 1 or 2 \n 1.Get books data\n 2.Add new book')
         if choice=='1':
            try:
               books= pd.read_csv('books.csv',sep='\t')
               print(books)
            except FileNotFoundError:
                  print('No books found!')           

         elif choice=='2':
            name=input('name of the book : ')
            author=input('name of the author : ')
            type=input('type : ')
            notes=input('notes : ')
            add_book(name,author,type,notes)
            books_data=pd.DataFrame(books)
            # print(books_data)
            books_data.to_csv('books.csv',sep='\t',index=False)
            
         else:
              print('\n enter a valid input \n')
         exit=input('continue program..? (y/n)')
         if exit.lower()=='y':
                pass

         else:
               ('program terminated')
               break
       
    
def add_book(name,author,type,notes):
    books['Name'].append(name)
    books['Author'].append(author)
    books['Type'].append(type)
    books['Notes'].append(notes)

start_app()