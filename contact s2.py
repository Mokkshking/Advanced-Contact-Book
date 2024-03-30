import pyttsx3
import pickle
import os
# Add password level security (multiple passwords to make serure leveling like: boss,admin,clear,public)
# make more user friendly : add more freindly features and change voice
def update(pos):
   
    f.seek(pos)
    pickle.dump(x,f)
   
speaker = pyttsx3.init()
print("~" * 60)
print('HELLO BOSS')
speaker.say('Hello Boss')
speaker.runAndWait()

print("WELCOME YOU TO THE WORLD'S MOST ADVANCE CONTACT SYSTEM")
speaker.say("Welcome you are with world's most advance contact system")
speaker.runAndWait()

print("I AM YOUR PERSONAL ASSISTANT")
speaker.say("I AM YOUR PERSONAL ASSISTANT")
speaker.runAndWait()
print("~" * 60)

want = input("DO YOU WANT TO HAVE VOICE OR NOT (YES/NO) :")
ct = {}

if want.upper() == "YES":
    print("BELOW ARE THE OPTIONS YOU CAN DO HERE")
    print("~" * 60)
    speaker.say("BELOW ARE THE OPTIONS YOU CAN DO HERE")
    speaker.runAndWait()
    while True:
        print("ENTER-1 :- CREATE A NEW CONTACT")
        speaker.say("ENTER-1 :- CREATE A NEW CONTACT")
        speaker.runAndWait()

        print("ENTER-2 :- MODIFY A CONTACT")
        speaker.say("ENTER-2 :- MODIFY A CONTACT")
        speaker.runAndWait()

        print("ENTER-3 :- REMOVE A CONTACT")
        speaker.say("ENTER-3 :- REMOVE A CONTACT")
        speaker.runAndWait()

        print("ENTER-4 :- SEARCH A CONTACT")
        speaker.say("ENTER-4 :- SEARCH A CONTACT")
        speaker.runAndWait()

        print("ENTER-5 :- EXIT")
        speaker.say("ENTER-5 :- EXIT")
        speaker.runAndWait()

        speaker.say('Please Enter Your choice')
        speaker.runAndWait()
        choice = int(input('ENTER YOU CHOICE :-'))

        if choice == 1:
            speaker.say('You choose to add a new contact')
            speaker.runAndWait()
            speaker.say('Provide details of new contact')
            speaker.runAndWait()

            speaker.say('ENTER THE CONTACT NUMBER')
            speaker.runAndWait()
            ph = input("ENTER THE CONTACT NUMBER ")

            while len(ph) != 10:
                print('THE ENTERED NUMBER SHOULD BE OF 10 DIGITS')
                speaker.say('THE ENTERED NUMBER SHOULD BE OF 10 DIGITS')
                speaker.runAndWait()
                speaker.say('ENTER THE CONTACT NUMBER')
                speaker.runAndWait()
                ph = input("ENTER THE CONTACT NUMBER ")
            speaker.say('ENTER THE FIRST NAME :-')
            speaker.runAndWait()
            FName = input('ENTER THE FIRST NAME :-')
            speaker.say('ENTER THE LAST NAME :-')
            speaker.runAndWait()
            LName = input('ENTER THE LAST NAME :-')
            speaker.say('ENTER THE ADDRESS :-')
            speaker.runAndWait()
            Address = input('ENTER THE ADDRESS :-')
            speaker.say('ENTER YOUR CITY :-')
            speaker.runAndWait()
            city = input('ENTER YOUR CITY :-')
            speaker.say("THAT'S ALL THE INFORMATION WE NEEDED")
            speaker.runAndWait()
            speaker.say("PLEASE WAIT WHILE THE CONTACT IS ADDED")
            speaker.runAndWait()

            ct = {'Phone no':ph, 'First name': FName,'Last name': LName,'Address': Address, 'city':city}
            f = open(r'addressbook.dat', "ab")
            pickle.dump(ct, f)
            f.close()

            print('THE CONTACT IS ADDED SUCCESSFULLY')
            speaker.say("THE CONTACT IS ADDED SUCCESSFULLY")
            speaker.runAndWait()
            print('~' * 60)

        elif choice == 2:
            
                        
            speaker.say('You choose to modify a contact')
            speaker.runAndWait()
            speaker.say('ENTER THE CONTACT NUMBER TO MODIFY')
            speaker.runAndWait()
            ph = input("ENTER THE CONTACT NUMBER TO MODIFY ")
            f=open(r'addressbook.dat',"rb+")
            try:
                while True:
                    f=open(r'addressbook.dat',"rb+")
                    pos=f.tell()
                    x = pickle.load(f)
                    if x['Phone no'] == ph:
                        
                        speaker.say("PRESS 1 TO CHANGE THE FIRST NAME")
                        speaker.runAndWait()
                        print("PRESS 1 TO CHANGE THE FIRST NAME")
                        speaker.say("PRESS 2 TO CHANGE THE LAST NAME")
                        speaker.runAndWait()
                        print("PRESS 2 TO CHANGE THE LAST NAME")
                        speaker.say("PRESS 3 TO CHANGE THE ADDRESS")
                        speaker.runAndWait()
                        print("PRESS 3 TO CHANGE THE ADDRESS")
                        speaker.say("PRESS 4 TO CHANGE THE CITY")
                        speaker.runAndWait()
                        print("PRESS 4 TO CHANGE THE CITY")
                        speaker.say("PRESS 5 TO EXIT")
                        speaker.runAndWait()
                        print("PRESS 5 TO EXIT")

                        speaker.say('Please Enter Your opinion')
                        speaker.runAndWait()
                        option = int(input('ENTER YOU OPTION :-'))
                        if option == 1:
                            stu={}
                            speaker.say('YOU HAVE CHOOSE TO CHANGE THE FIRST NAME')
                            speaker.runAndWait()
                            speaker.say("ENTER THE NEW FIRST NAME")
                            speaker.runAndWait()
                            new = input("ENTER THE NEW FIRST NAME")
                            found=False
                            x['First name'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                    
                            print("~" * 60)

                

                        elif option == 2:
                            stu={}
                            speaker.say('YOU HAVE CHOOSE TO CHANGE THE LAST NAME')
                            speaker.runAndWait()
                            speaker.say("ENTER THE NEW LAST NAME")
                            speaker.runAndWait()
                            new = input("ENTER THE NEW LAST NAME")
                            found=False
                            x['Last name'] = new
                            update(pos)
                            print('Last NAME UPDATED')
                    
                            print("~" * 60)

                        elif option == 3:
                            stu={}
                            speaker.say('YOU HAVE CHOOSE TO CHANGE THE ADDRESS')
                            speaker.runAndWait()
                            speaker.say("ENTER THE NEW ADDRESS")
                            speaker.runAndWait()
                            new = input("ENTER THE NEW ADDRESS")
                            found=False
                            x['Address'] = new
                            update(pos)
                            print('ADDRESS UPDATED')
                    
                            print("~" * 60)

                        elif option == 4:
                            stu={}
                            speaker.say('YOU HAVE CHOOSE TO CHANGE THE CITY')
                            speaker.runAndWait()
                            speaker.say("ENTER THE NEW CITY")
                            speaker.runAndWait()
                            new = input("ENTER THE NEW CITY")
                            found=False
                            x['city'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                    
                            print("~" * 60)

                        elif option == 5 :
                            speaker.say("THANKYOU FOR MODIFICATION")
                            speaker.runAndWait()
                            print("THANKYOU FOR MODIFICATION")
                            break

            except EOFError:
                f.close()
        elif choice == 3:
            
            f = open(r"addressbook.dat", "rb")
            
            f1 = open(r"newaddressbook.dat", "wb")
            speaker.say(" YOU CHOOSE TO REMOVE A CONTACT")
            speaker.runAndWait()
            speaker.say("enter the phone number that u want to remove")
            speaker.runAndWait()
            ph = input("ENTER PHONE NUMBER TO BE REMOVED")

            try:
                while True:
                    if x['Phone no'] == ph:
                        found= True
                        speaker.say("entered phone number has been removed successfully")
                        speaker.runAndWait()
                        print("PHONE NUMBER REMOVED SUCCESSFULLY")
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
                speaker.say("the phone number you entered is not present in your directory")
                speaker.runAndWait()
                print("THE PHONE NUMBER YOU ENTERED IS NOT PRESENT IN YOUR DIRECTORY ")
    
        elif choice == 4:
            f = open(r'addressbook.dat',"rb+")
            try:
                while True:
                    x = pickle.load(f)
                    
            except EOFError:
                print()

            speaker.say("YOU CHOOSE TO SEARCH A CONTACT")
            speaker.runAndWait()
            speaker.say("ENTER THE PHONE NUMBER THAT YOU WANT TO SEARCH")
            speaker.runAndWait()
            ph = input("ENTER THE PHONE NUMBER THAT YOU WANT TO SEARCH")
            
            if x['Phone no'] == ph:
                speaker.say("DETAILS ARE AS FOLLOWS")
                speaker.runAndWait()
                print(x)
                print("~" * 60)
            else:
                speaker.say("PHONE NUMBER NOT FOUND")
                speaker.runAndWait()
                print("PHONE NUMBER NOT FOUND")
                
        elif choice == 5:
            break
    print("~" * 60)
    speaker.say("THE CONTACT LIST IS HERE")
    speaker.runAndWait()
    print("THE CONTACT LIST IS HERE")
    f = open("addressbook.dat", "rb")
    try:
        while True:
            ct = pickle.load(f)
            print(ct)
    except:
        f.close()
    print("~" * 60)
    speaker.say("PLEASE RATE US OUT OF 5 ")
    speaker.runAndWait()
    rating = int(input("PLEASE RATE US (OUT OF 5)"))
    if rating == 1:
        speaker.say(" SORRY FOR THE INCONVENIENCE")
        speaker.runAndWait()
        print("SORRY FOR THE INCONVENIENCE")
    elif rating == 2:
        speaker.say("SORRY FOR DISAPPOINTING YOU")
        speaker.runAndWait()
        print('SORRY FOR DISAPPOINTING YOU')
    elif rating == 3:
        speaker.say("WE WILL TRY TO MAKE YOUR EXPERIENCE MORE SMOOTHER")
        speaker.runAndWait()
        print('WE WILL TRY TO MAKE YOUR EXPERIENCE MORE SMOOTHER')
    elif rating == 4:
        speaker.say("WE WILL TRY OUR BEST TO MAKE YOU RATE 5")
        speaker.runAndWait()
        print('WE WILL TRY OUR BEST TO MAKE YOU RATE 5')
    elif rating == 5:
        speaker.say("THANK YOU WE APPRECIATE YOUR TIME")
        speaker.runAndWait()
        print('THANK YOU WE APPRECIATE YOUR TIME')
    else:
        print("YOU ENTER THE INCORRECT RATING !!!")

elif want.upper() == "NO":
    while True:
        print("ENTER-1 :- CREATE A NEW CONTACT")
        print("ENTER-2 :- MODIFY A CONTACT")
        print("ENTER-3 :- REMOVE A CONTACT")
        print("ENTER-4 :- SEARCH A CONTACT")
        print("ENTER-5 :- EXIT")
        choice = int(input('ENTER YOU CHOICE :-'))

        if choice == 1:
            
            print('YOU CHOOSE TO ADD A NEW CONTACT')
            print('PROVIDE THE DETAILS OF NEW CONTACT')
            ph = input("ENTER THE CONTACT NUMBER ")
            while len(ph) != 10:
                print('THE ENTERED NUMBER SHOULD BE OF 10 DIGITS')
                ph = input("ENTER THE CONTACT NUMBER")
            
            FName = input('ENTER THE FIRST NAME :-')
            LName = input('ENTER THE LAST NAME :-')
            Address = input('ENTER THE ADDRESS :-')
            city = input('ENTER YOUR CITY :-')
            print("THAT'S ALL THE INFORMATION WE NEEDED")
            ct = {'Phone no':ph, 'First name': FName,'Last name': LName,'Address': Address, 'city':city}
            f = open(r'addressbook.dat', "ab")
            pickle.dump(ct, f)
            f.close()

            print('THE CONTACT IS ADDED SUCCESSFULLY')
            print('~' * 60)

        elif choice == 2:
            
                        
            print('YOU CHOOSE TO MODIFY THE CONTACT')
            ph = input("ENTER THE CONTACT NUMBER TO MODIFY ")
            
            f = open(r'addressbook.dat',"rb+")
            try:
                while True:
                    f=open(r'addressbook.dat',"rb+")
                    pos=f.tell()
                    x = pickle.load(f)
                    print(x)
                    if x['Phone no'] == ph:
                        
                        print("PRESS 1 TO CHANGE THE FIRST NAME")
                        print("PRESS 2 TO CHANGE THE LAST NAME")
                        print("PRESS 3 TO CHANGE THE ADDRESS")
                        print("PRESS 4 TO CHANGE THE CITY")
                        print("PRESS 5 TO EXIT")

                        option = int(input('ENTER YOU OPTION :-'))
                        if option == 1:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE FIRST NAME')
                            new = input("ENTER THE NEW FIRST NAME")
                            found=False
                            x['First name'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                            print("~" * 60)

                        elif option == 2:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE LAST NAME')
                            new = input("ENTER THE NEW LAST NAME")
                            found=False
                            x['Last name'] = new
                            update(pos)
                            print('Last NAME UPDATED')
                            print("~" * 60)

                        elif option == 3:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE ADDRESS')
                            new = input("ENTER THE NEW ADDRESS")
                            found=False
                            x['Address'] = new
                            update(pos)
                            print('ADDRESS UPDATED')
                            print("~" * 60)

                        elif option == 4:
                            stu={}
                            print('YOU HAVE CHOOSE TO CHANGE THE CITY')
                            new = input("ENTER THE NEW CITY")
                            found=False
                            x['city'] = new
                            update(pos)
                            print('FIRST NAME UPDATED')
                            print("~" * 60)

                        elif option == 5 :
                            print("THANKYOU FOR MODIFICATION")
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
                    if x['Phone no'] == ph:
                        found= True
                        print("PHONE NUMBER REMOVED SUCCESSFULLY")
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
                print("DETAILS ARE AS FOLLOWS")
                print(x)
                print("~" * 60)
            else:
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
            

