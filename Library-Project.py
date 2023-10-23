#!/usr/bin/env python
# coding: utf-8

# In[94]:



books={"Physics":10,"Chemistry":10,"Maths":10}
br={}

print("***********Welcome to Library**************")
username = "AAS MOHAMMAD"
password =12345    
while True:
    un=input("Enter Username:").upper()
    if un==username:
        ps=int(input("Enter Password:"))
        if ps==password:
            print("Login sucessfully:")
            break
        else:
            print("Incorrect Password")

    else:
        print("Incorrect Username")
            
            
while True:
    c=int(input("""press 1 for borrow a book and press 2 for return a book
press 3 for display the available books.  
                          """))

    if c ==1:
        b = input("Enter the book name: ").title()
        n = input("Enter borrower name: ").title()
        if b in books:
            books[b]-=1
            br[b]=n
            print("-"*60)
            print("Borrower name: ",n)
            print("Borrow book name:",b)
            print("-"*60)
            print("Availabe books :",books)
        else:
            print("this book is not available library.Please enter the another books")
    elif c==2:
        b=input("Enter the book name: ").title()
        n=input("Enter the borrower name: ").title()
        if b in br:
            books[b]+=1
            del br[b]
            print("-"*60)
            print("Borrower name: ",n)
            print("return book name:",b)
            print("-"*60)
            print("Availabe books :",books)
        else:
            print("this book was not issued form this library.please returned the correct book")
    else:
        for i,j in br.items():
            print(i,"-",j)
            break
    nexxt = input("borrow/return for next person").lower()
    if nexxt == "no":
        break
    

