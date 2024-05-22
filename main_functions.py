from avl_tree import*
from Library_data import*
from user_raw_data import*
from datetime import datetime,timedelta
import unittest

def main(): #sets up homepage
    print ("Welcome to Library Nijaat! Press 1 if you are an admin, press 2 if you are a user.")
    task=str(input())
    while task!='1' and  task!='2':
        task=input("Invalid input. Please enter 1 or 2\n")
    if task=='1':
        admin_main()
    elif task=='2':
        user_main(users_database)


def admin_main(): #login for admin
    password=str(input("Please enter the admin password: "))
    correct_password=search(users_database,'admin')['Password']
    while password!=correct_password and password!='0':
            password=str(input("Oops, that's not the correct password! Please reenter or type 0 to exit."))
    if password=='0':
        main()
        return
    admin_task_selection()


def user_main(tree): #main interface for user
    task=(input(("\nHello! Please choose the appropriate option.\n1. Create new account\n2. Login\n3. Return to main\n")))
    while task!='1' and  task!='2':
        task=input("Invalid input. Please enter 1 or 2\n")

    if task=='1':
        create_new_account(tree)
    elif task=='2':
        login(tree)
    elif task=='3':
        main()


def admin_task_selection(): #main interface for admin
    print ("\nWhat would you like to do?\n1. See a user account\n2. Delete a user account\n3. Add a book\n4. Remove a book\n5. Update a book's details\n6. Erase a user's fines\n7. Update fine amount\n8. Log out")
    task=input()
    valid_tasks=['1','2','3','4','5','6','7','8']
    while task not in valid_tasks:
        task=input("Oops! That's not a valid input. Please input a number listed above: ")
    if task=='1':
        see_user_account()
    elif task=='2':
        delete_user_account()
    elif task=='3':
        add_book(books_database)
    elif task=='4':
        remove_book()
    elif task=='5':
        update_book(books_database,None)
    elif task=='6':
        remove_fines()
    elif task=='7':
        global daily_fine
        daily_fine=int(input("Enter the new fine amount: "))
        admin_task_selection()
    elif task=='8':
        main()


def see_user_account():
    username=input("\nWhich user's data do you want to see?\n")
    while search(users_database,username)==None and username!='0': #checks user exists
        username=input("Oops, that user doesn't seem to exist. Please reenter the username correctly or type 0 to exit.\n")
    if username=='0':
        admin_task_selection()
        return
    
    fine_updater(username)
    user=(search(users_database,username))
    print ("Username:",user['Username'])
    print ("Password:",user['Password'])
    print ("Fines Due: Rs.",user['Fines Due'])
    print ('Books borrowed, along with due dates:',user['Books Borrowed'])
    admin_task_selection()


def delete_user_account():
    username=input("\nWhich user do you want to delete?\n")
    while search(users_database,username)==None and username!='0': #checks user exists
        username=input("Oops, that user doesn't seem to exist. Please reenter the username correctly or type 0 to exit.\n")
    if username=='0':
        admin_task_selection()
        return
    delete(users_database,username)
    print ("User account deleted")
    admin_task_selection() 


def add_book(tree):
    title=input("Enter the title of the book you wish to add\n")
    while search(tree,title)!=None and title!='0' and title!='1': #checks if book exists
        title=input("That book already exists in the database. Reenter the title if you wish to add another book, press 1 if you want to update the existing book's data, and press 0 if you wish to exit\n")
    
    if title=='0':
        admin_task_selection()
        return
    elif title=='1':
        update_book(title)
        return
    #takes in data of new book
    isbn=input("Enter the ISBN of the book you wish to add\n")
    isbn1 = ""
    for i in isbn: 
        if i.isnumeric():
            isbn1 += i
        else: 
            print ("Not an appropriate input. Please reinput the book's data") 
            add_book(tree) 
        
    genre=input("Enter the genre of the book you wish to add\n")
    genre1 = ''
    for i in genre: 
        if i.isalpha():
            genre1 += i
        else: 
            print ("Not an appropriate input. Please reinput the book's data") 
            add_book(tree)
    author=input("Who is the author?\n")
    copies=input("How many copies do you wish to add?")
    copies1 = ''
    for i in copies: 
        if i.isnumeric():
            copies1 += i
        else: 
            print ("Not an appropriate input. Please reinput the book's data") 
            add_book(tree)
    
    data={'Title': title, 'ISBN':isbn,'Genre':genre,'Author':author,'Copies':int(copies)}
    tree=insert(tree,title,data)
    admin_task_selection()
    tree=insert(tree,title,data)
    admin_task_selection()


def update_book(tree,title=None):
    if title==None:
        title=str(input("\nWhat book do you wish to update?\n"))
    while search(tree,title)==None and title!='0': #checks book exists
        title=input("That book doesn't exist in the base. Reenter the title correctly or type 0 to exit\n")
    if title=='0':
        admin_task_selection()
        return
    
    field=input("What field do you wish to update?")
    valid_fields=['Title','ISBN','Genre','Author','Copies']
    while field not in valid_fields and field!='0': #checks field is valid
        field=input("Oops, that field doesn't seem to exist. Please reenter the field correctly or type 0 to exit.\n")
    if field=='0':
        admin_task_selection()
        return
    
    new_data=input("Enter the new data you wish to update\n")
    if field=='Copies':
        update(tree,title,field,int(new_data))
    else:
        update(tree,title,field,new_data)
    admin_task_selection()


def remove_book():
    title=str(input("\nWhat book do you wish to delete?\n"))
    while search(books_database,title)==None and title!='0': #checks book exists
        title=input("That book doesn't exist in the base. Reenter the title correctly or type 0 to exit\n")
    if title=='0':
        admin_task_selection()
        return
    delete(books_database,title)
    admin_task_selection()


def remove_fines(): #allows admin to remvoe someone's fines
    username=str(input("\nWhich user's fines do you want to remove?\n"))
    while search(users_database,username)==None and username!='0':
        username=input("Oops, that user doesn't seem to exist. Please reenter the username correctly or type 0 to exit.\n")
    if username=='0':
        admin_task_selection()
        return
    fine_updater(username) #ensures fines are up to date
    update(users_database,username,'Fines Due',0)
    admin_task_selection()



def login(tree): #allows user to login
    username=str(input("\nPlease enter your username: "))
    while search(tree,username)==None and username!='1' and username!='0': #checks if user exists
        username=str(input("Oops! That doesn't appear to be correct. Please try again or enter 1 if you wish to create a new account. Type 0 to exit: "))
    
    if username=='0':
        user_main(tree)
        return
    elif username=='1':
        tree=create_new_account(tree)
        return
    correct_password=search(tree,username)['Password']
    password=str(input("Enter your password: "))

    while password!=correct_password and password!='0':
        password=str(input("Oops! That doesn't appear to be correct. Please try again or contact the administration if you have forgotten your password. Type 0 to exit\n "))
    if password=='0':
        user_main(tree)
    welcome(tree,username)



def create_new_account(tree): #allows users to create new accounts
    username=str(input("\nEnter your username. Type 1 to return to main: "))
    while search(tree,username)!=None and username!='1': #checks whether user already exists
        username=str(input("Oops! That username is already taken. Please try another one or type 1 if you already have an account: "))
    if username=='1':
        login(tree)
        return
    
    password=str(input("Enter your password: "))
    new_data={"Username":username, "Password":password, "Books Borrowed":[],"Fines Due":0}
    tree=insert(tree,username,new_data)
    welcome(tree,username)



def welcome(tree,username): #welcome for user
    print("\nWelcome",username,"! Please select what you wish to do today. \n1. Change my password\n2. Issue a book\n3. Return a book.\n4. See my fines\n5. Search for a book\n6. Log out")
    task=input()
    user_task_selection(tree,task,username)



def user_task_selection(tree,task,username): #main interface for user
    if task=='0':
        task=input("\nWhat would you like to do? \n1. Change my password\n2. Issue a book\n3. Return a book.\n4. See my fines\n5. Search for a book\n6. Log out\n")
    valid_tasks=['1','2','3','4','5','6']
    while task not in valid_tasks:
        task=input("Oops! That's not a valid input. Please input a number listed above: ")
    task=int(task)
    if task==1:
        update_password(tree,username)
    elif task==2:
        issue_book(tree,username)
    elif task==3:
        return_book(tree,username)
    elif task==4:
        see_fines(tree,username)
    elif task==5:
        book_search(username)
    elif task==6:
        main()



def update_password(tree,username): #allows users to update password
    new_password=str(input("\nEnter your new password: "))
    update(tree,username,"Password",new_password)
    print ("Your password has been succesfully updated. Please select what you wish to do next")
    print ("1. Change my password\n2. Issue a book\n3. Return a book.\n4. See my fines\n5. Search for a book\n6. Log out")
    task=input()
    user_task_selection(tree,task,username)



def issue_book(tree,username): #allows user to issue books
    book=str(input("Enter the title of the book you want to issue today: "))
    book_data=search(books_database,book)

    while book_data==None and book!='0': #checks if book exists
        book=input("We don't have that book in our collection. Is there another book you'd like? Type 0 to exit\n")
        book_data=search(books_database,book)
    
    if book=='0':
        user_task_selection(tree,book,username)

    elif book_data['Copies']==0: #checks if copies available
        print ("Oops! There are no available copies of the book available currently.")
        user_task_selection(tree,'0',username)

    else:
        update(books_database,book,'Copies',book_data['Copies']-1) #updates number of copies in database
        user_data=search(tree,username) #updating user's borrowed books
        borrowed=user_data['Books Borrowed']
        borrowed.append([book,datetime.now().date()+timedelta(days=7)])
        update(tree,username,'Books Borrowed',borrowed)
        print ("Your borrowal has been approved!")
        user_task_selection(tree,'0',username)



def return_book(tree,username): #allows user to return books
    book=str(input("\nEnter the title of the book you want to return today: "))
    user_data=search(tree,username)
    borrowed_books=[]
    for i in user_data['Books Borrowed']: #creates list of books borrowed by user
        borrowed_books.append(i[0])
    while book not in borrowed_books and book!='0': #checks if user has books
        book=str(input(("Oops! You don't have that book currently. Please reenter the title correctly or type 0 if you would like to do something else.\n")))
    
    if book=='0':
        user_task_selection(tree,book,username)

    else:
        book_data=search(books_database,book) #updates books_database
        update(books_database,book,'Copies',book_data['Copies']+1) 
        borrowed=user_data['Books Borrowed'] #updates user_database
        for i in borrowed:
            if i[0]==book:
                borrowed.remove(i)
        update(tree,username,'Books Borrowed',borrowed)
        print ("Your return has been processed!")
        user_task_selection(tree,'0',username)



def see_fines(tree,username):
    fine_updater(username)
    fines=search(tree,username)['Fines Due']
    print ("\nYou have Rs."+str(fines),'due in fines')
    user_task_selection(tree,'0',username)



def book_search(username):
    book=str(input("\nWhat book do you want to search for today?"))
    
    while search(books_database,book)==None and book!='0':
        print ("Unfortunately, we don't have that book. You can search for another book or type 0 to exit.")
        book=str(input())
    
    if book=='0':
        user_task_selection(users_database,book,username)
    elif search(books_database,book)!=None:
        print("Yes, we have that book in our collection!")
        user_task_selection(users_database,'0',username)


daily_fine=20
def fine_updater(username):
    user_fine=0
    current_date=datetime.now().date()
    for i in search(users_database,username)['Books Borrowed']:
        date_difference=current_date-i[1] #finds difference between today and date due
        if date_difference.days>0:
            user_fine+=date_difference.days *daily_fine #calculates fine
            i[1]=current_date #updates due date to today
    old_fine=search(users_database,username)['Fines Due']
    user_fine+=old_fine
    update(users_database,username,'Fines Due',user_fine)

    

main()