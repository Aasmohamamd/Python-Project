#!/usr/bin/env python
# coding: utf-8

# In[ ]:



total_seat=40
nor_seat=20
rec_seat=10
    
rec=1
gold=2
silver=3
    
while True:
    
        if total_seat==0:
            print("House full")
            break
        print("Movie list on Screen-- Jawan,fukray and housefull")    
        print("Seat type---> Recliner,Normal")
        print("""Recliner Seat Price------->500 rs.
Normal Seat Price------>400 rs.""")
        print("Combo(frice + cold drink) price----->100 rs.")
        print("-"*60)

        movie = input("Enter Movie Name:")
        name= input("Enter customer name: ")
        choice = int(input("Which seat do you want : Press 1 for Recliner, 2 for Normal : " ))
        seat = int(input("how many seat do you want: "))
        combo=input("Do you want to add combo: ")
        
        if choice==1 and seat<rec_seat and combo=="yes":
            amount=500*seat
            rec_seat-=seat
            total_seat-=seat
            print("-" *60)
            print("Movie name:  ",movie)
            print("Customer's name: ",name)
            print("Seat type: Recliner")
            print("Combo: Yes")
            print("Payble Amount: ",amount+100)
            print("-"*60)
            
        elif choice==1 and seat<rec_seat and combo=="no":
            amount=500*seat
            rec_seat-=seat
            total_seat-=seat
            print("-" *60)
            print("Movie name:  ",movie)
            print("Customer's name: ",name)
            print("Seat type: Recliner")
            print("Comob: No")
            print("Payble Amount: ",amount)
            print("-"*60)
            
        elif choice==2 and seat<nor_seat and combo=="yes":
            amount=400*seat
            nor_seat-=seat
            total_seat-=seat
            print("-" *60)
            print("Movie name:  ",movie)
            print("Customer's name: ",name)
            print("Seat type: Normal")
            print("Combo: Yes")
            print("Payble Amount: ",amount+100)
            print("-"*60)
        elif choice==2 and seat<nor_seat and combo=="no":
            amount=400*seat
            nor_seat-=seat
            total_seat-=seat
            print("-" *60)
            print("Movie name:  ",movie)
            print("Customer's name: ",name)
            print("Seat type: Normal")
            print("Combo: No")
            print("Payble Amount: ",amount)
            print("-"*60)  
        else:
            print("choose the correct input.........try again")
            
            
        print("Seat available in::","|Recliner Seat:",rec_seat,"|Normal Seat:",nor_seat)
        nextt=input("next person? ")
        if nextt=="no":  
            break
    


# In[ ]:




