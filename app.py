import pandas as pd

books={
     'Name':[],
     'Author':[],
     'Remarks':[]
}

#create html file
def make_html():
    df=pd.read_csv('books.csv')
    html_table=df.to_html(index=False)
    with open('template.html','r') as file:
        html_content=file.read()
        html_content=html_content.replace("{{html_table}}",html_table)
    with open('index.html','w') as file:
        file.write(html_content)

#add new book
def add_books():
  while True:
    name=input('Name of the book : ')
    author=input('Name of the author : ')
    remarks=input('Remarks : ')
    print(f"\n name :{name}\tauthor:{author}\tremarks:{remarks}")
    save_book=input('Save ? (y/n): ')
    if save_book.lower()=='y':
            books["Name"].append(name)
            books['Author'].append(author)
            books["Remarks"].append(remarks)
    else:
        print('SHRADHIKKANDE AMBANEE ')
        pass

    try:
        df=pd.DataFrame(books)
        df.to_csv('books.csv', mode='a',index=False,header=False)
        print('book saved successfully !')
        break  
    except Exception as err:
        print(err)

#view books
def view_books():
    try:
      existing_books=pd.read_csv('books.csv')
      print(existing_books)
    except Exception as e :
        print(f'No books found !: {e}')
        
#start app
def start():
    while True:
        print('FaisBook')
        choice=input('1.View books \n2.Add new books\n\t')
        if choice=="1":
            view_books()
            
        elif choice=="2":
            add_books()

        else:
            print('Enter 1 or 2 only bro!!')
            pass
        finish=input('continue? (y/n): ')
        if finish.lower()=='y':
            pass
        else:
            print('Program terminated')
            break



start()
make_html()