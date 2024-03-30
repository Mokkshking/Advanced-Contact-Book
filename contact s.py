import pyttsx3
import pickle
## To do imp ##
# Add password level security (multiple passwords to make serure leveling like: boss,admin,clear,public)
# add cases in search (like search by city and others)
# correct the modify : it cause error (from program 12)
# correct the delete : works inefficiently (from program 10)
# add use of multiple files to choose processes (use if and while or make entire program an built in function)
# make more user friendly : add more freindly features and change voice

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

print("BELOW ARE THE OPTIONS YOU CAN DO HERE")
print("~" * 60)
speaker.say("BELOW ARE THE OPTIONS YOU CAN DO HERE")
speaker.runAndWait()

if want.upper() == "YES":
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
            
            def update():
                
                x[z]= new
                f.seek(pos)
                pickle.dump(x,f)
            
            speaker.say('You choose to modify a contact')
            speaker.runAndWait()
            speaker.say('ENTER THE CONTACT NUMBER TO MODIFY')
            speaker.runAndWait()
            ph = input("ENTER THE CONTACT NUMBER TO MODIFY ")
            
            f = open(r'Addressbook.dat',"rb+")
            try:
                while True:
                    x = pickle.load(f)
                    print(x)
            except EOFError:
                print()
                
            if x['Phone no'] == ph:
                
                pos=f.tell()
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

                speaker.say('Please Enter Your opinion')
                speaker.runAndWait()
                option = int(input('ENTER YOU OPTION :-'))

                if option == 1:
                    stu={}
                    speaker.say('YOU HAVE CHOOSE TO CHANGE THE FIRST NAME')
                    speaker.runAndWait()
                    speaker.say("ENTER THE NEW FIRST NAME")
                    speaker.runAndWait()
                    new = input("ENTER THE FIRST NAME")
                    found=False
                    x['First name'] = new
                    f = open(r"addressbook.dat", "rb+")
                    z='First name'
                    y=update()
                    print('FIRST NAME UPDATED')
                    
                    print("~" * 60)

                elif option == 2:
                    speaker.say("YOU HAVE CHOOSE TO CHANGE THE  NAME")
                    speaker.runAndWait()
                    speaker.say("ENTER THE NEW LAST NAME")
                    speaker.runAndWait()
                    new = input("ENTER THE NEW LAST NAME")
                    found=False
                    x['Last name'] = new
                    f = open(r"addressbook.dat", "rb+")
                    z='Last name'
                    y=update()
                    print('LAST NAME UPDATED')
                    
                    print("~" * 60)

                elif option == 3:
                    speaker.say("YOU HAVE CHOOSE TO CHANGE THE ADDRESS")
                    speaker.runAndWait()
                    speaker.say("ENTER THE NEW ADDRESS")
                    speaker.runAndWait()
                    new = input("ENTER THE NEW ADDRESS")
                    found=False
                    x['Address'] = new
                    f = open(r"addressbook.dat", "rb+")
                    z='Address'
                    y=update()
                    print('ADDRESS UPDATED')
                    
                    print("~" * 60)

                elif option == 4:
                    speaker.say("YOU HAVE CHOOSE TO CHANGE THE CITY")
                    speaker.runAndWait()
                    speaker.say("ENTER THE NEW CITY")
                    speaker.runAndWait()
                    new = input("ENTER THE NEW CITY")
                    found=False
                    x['city'] = new
                    f = open(r"addressbook.dat", "rb+")
                    z='city'
                    y=update()
                    print('CITY UPDATED')
                    
                    print("~" * 60)

                else:
                    speaker.say(" YOUR OPTION IS INVALID")
                    speaker.runAndWait()
                    print("INVALID OPTION!!!!")
                    f.close()
       # plz reffer program 10 to make it correct              
        elif choice == 3:
            speaker.say(" YOU CHOOSE TO REMOVE A CONTACT")
            speaker.runAndWait()
            speaker.say("enter the phone number that u want to remove")
            speaker.runAndWait()
            ph = input("ENTER PHONE NUMBER TO BE REMOVED")
            
            if x['Phone no'] == ph:
                x = None
                
                speaker.say("entered phone number has been removed successfully")
                speaker.runAndWait()
                print("PHONE NUMBER REMOVED SUCCESSFULLY")
                print("~" * 60)
            else:
                speaker.say("the phone number you entered is not present in your directory")
                speaker.runAndWait()
                print("THE PHONE NUMBER YOU ENTERED IS NOT PRESENT IN YOUR DIRECTORY ")
            
        elif choice == 4:
            f = open(r'Addressbook.dat',"rb+")
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
            
            
