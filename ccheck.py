import pyttsx3
import pickle
import os
## To do imp ##
# Add password level security (multiple passwords to make serure leveling like: boss,admin,clear,public)
# add cases in search (like search by city and others)
# correct the modify : it cause error (from program 12)
# correct the delete : works inefficiently (from program 10)
# add use of multiple files to choose processes (use if and while or make entire program an built in function)
# make more user friendly : add more freindly features and change voice
def update(pos):
   
    f.seek(pos)
    pickle.dump(x,f)
   
speaker = pyttsx3.init()
print("~" * 60)
print('HELLO BOSS')

print("WELCOME YOU TO THE WORLD'S MOST ADVANCE CONTACT SYSTEM")

print("I AM YOUR PERSONAL ASSISTANT")

print("~" * 60)

want = input("DO YOU WANT TO HAVE VOICE OR NOT (YES/NO) :")
ct = {}

print("BELOW ARE THE OPTIONS YOU CAN DO HERE")
print("~" * 60)

if want.upper() == "NO":
    while True:
        print("ENTER-1 :- CREATE A NEW CONTACT")     

        print("ENTER-2 :- MODIFY A CONTACT")
        
        print("ENTER-3 :- REMOVE A CONTACT")
        
        print("ENTER-4 :- SEARCH A CONTACT")
        
        print("ENTER-5 :- EXIT")

        choice = int(input('ENTER YOU CHOICE :-'))

        if choice == 1:
            print('You choose to add a new contact')
            print('Provide details of new contact')

            ph = input("ENTER THE CONTACT NUMBER ")

            while len(ph) != 10:
                print('THE ENTERED NUMBER SHOULD BE OF 10 DIGITS')

                ph = input("ENTER THE CONTACT NUMBER ")
            
            FName = input('ENTER THE FIRST NAME :-')
            FName = FName.capitalize()
            LName = input('ENTER THE LAST NAME :-')
            LName = LName.capitalize()
            Address = input('ENTER THE ADDRESS :-')
            Address =Address.capitalize()
            city = input('ENTER YOUR CITY :-')
            city = city.capitalize()
            
            print("THAT'S ALL THE INFORMATION WE NEEDED")
            
            print("PLEASE WAIT WHILE THE CONTACT IS ADDED")
            

            ct = {'Phone no':ph, 'First name': FName,'Last name': LName,'Address': Address, 'city':city}
            f = open(r'addressbook.dat', "ab")
            pickle.dump(ct, f)
            f.close()

            print('THE CONTACT IS ADDED SUCCESSFULLY')
           
            print('~' * 60)

        elif choice == 2:
            
                        
            print('You choose to modify a contact')

            ph = input("ENTER THE CONTACT NUMBER TO MODIFY ")
            
            f = open(r'addressbook.dat',"rb+")
            try:
                while True:
                    pos=f.tell()
                    x = pickle.load(f)
                    print(x)
                    if x['Phone no'] == ph:

                        print("PRESS 1 TO CHANGE THE FIRST NAME")

                        print("PRESS 2 TO CHANGE THE LAST NAME")
                        
                        print("PRESS 3 TO CHANGE THE ADDRESS")
                        
                        print("PRESS 4 TO CHANGE THE CITY")
                        
                        print("PRESS 5 TO EXIT")

                        option = int(input('PLEASE ENTER YOU OPTION :-'))
                        if option == 1:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE FIRST NAME')
                            
                            new = input("ENTER THE NEW FIRST NAME")
                            found=False
                            x['First name'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                            f.seek(0)
                    
                            print("~" * 60)

                

                        if option == 2:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE LAST NAME')
                            
                            new = input("ENTER THE NEW LAST NAME")
                            found=False
                            x['Last name'] = new
                            update(pos)
                            print('LAST NAME UPDATED')
                            f.seek(0)
                    
                            print("~" * 60)

                        if option == 3:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE ADDRESS')
                            
                            new = input("ENTER THE ADDRESS")
                            found=False
                            x['Address'] = new
                            update(pos)
                            print('ADDRESS UPDATED')
                            f.seek(0)
                    
                            print("~" * 60)

                        if option == 4:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE CITY')
                            
                            new = input("ENTER THE NEW CITY")
                            found=False
                            x['city'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                            f.seek(0)
                    
                            print("~" * 60)

                        elif option==5:
                            
                            print("YOU CHOOSE TO EXIT")
                            f.close()
                            break

            except EOFError:
                f.close()
        elif choice == 3:
            
            f = open(r"addressbook.dat", "rb")
            
            f1 = open(r"newaddressbook.dat", "wb")
            print(" YOU CHOOSE TO REMOVE A CONTACT")
            
            ph = input("ENTER PHONE NUMBER TO BE REMOVED")

            try:
                while True:
                    x = pickle.load(f)
                    
                
                    if x['Phone no'] == ph:
                        found= True
                        
                        print("ENTERED PHONE NUMBER HAS BEEN REMOVED SUCCESSFULLY")
                        print("~" * 60)
                    else:
                        pickle.dump(x,f1)
            except EOFError:
                f.close()
                f1.close()
            if found==True:
                os.remove("addressbook.dat")
                os.rename("newaddressbook.dat","addressbook.dat")
            else:           
                
                print("THE PHONE NUMBER YOU ENTERED IS NOT PRESENT IN YOUR DIRECTORY ")
    
        elif choice == 4:
            f = open(r'addressbook.dat',"rb+")
            try:
                while True:
                    x = pickle.load(f)
                    
            except EOFError:
                print()

            print("YOU CHOOSE TO SEARCH A CONTACT")
            
            ph = input("ENTER THE PHONE NUMBER THAT YOU WANT TO SEARCH")
            
            if x['Phone no'] == ph:
                print(x)
                print("~" * 60)
            else:
                ("PHONE NUMBER NOT FOUND")
                
                print("PHONE NUMBER NOT FOUND")
                
        elif choice == 5:
            break
    print("~" * 60)
   
    print("THE CONTACT LIST IS HERE")
    f = open("addressbook.dat", "rb")
    try:
        while True:
            ct = pickle.load(f)
            print(ct)
    except:
        f.close()
    print("~" * 60)
    
    rating = int(input("PLEASE RATE US (OUT OF 5)"))
    if rating == 1:
        print("SORRY FOR THE INCONVENIENCE")
    elif rating == 2:
        print('SORRY FOR DISAPPOINTING YOU')
    elif rating == 3:
        print('WE WILL TRY TO MAKE YOUR EXPERIENCE MORE SMOOTHER')
    elif rating == 4:
        print('WE WILL TRY OUR BEST TO MAKE YOU RATE 5')
    elif rating == 5:
        print('THANK YOU WE APPRECIATE YOUR TIME')
    else:
        print("YOU ENTER THE INCORRECT RATING !!!")

        
