import pyttsx3
import pickle

speaker = pyttsx3.init()
print("~"*60)
print('HELLO BOSS')
speaker.say('Hello Boss')
speaker.runAndWait()

print("WELCOME YOU TO THE WORLD'S MOST ADVANCE CONTACT SYSTEM")
speaker.say("Welcome you are with world's most advance contact system")
speaker.runAndWait()

print("I AM YOUR PERSONAL ASSISTANT")
speaker.say("I AM YOUR PERSONAL ASSISTANT")
speaker.runAndWait()
print("~"*60)

want = input("DO YOU WANT TO HAVE VOICE OR NOT (YES/NO) :")
ct={}

print("BELOW ARE THE OPTIONS YOU CAN DO HERE")
print("~"*60)
speaker.say("BELOW ARE THE OPTIONS YOU CAN DO HERE")
speaker.runAndWait()

if want.upper() == "YES":
    while True:
        print("ENTER-1 :- CTEATE A NEW CONTACT")
        speaker.say("ENTER-1 :- CTEATE A NEW CONTACT")
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

        if choice==1:
            speaker.say('You choose to add a new contact')
            speaker.runAndWait
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
            Fname = input('ENTER THE FIRST NAME :-')
            speaker.say('ENTER THE LAST NAME :-')
            speaker.runAndWait()
            Lname = input('ENTER THE LAST NAME :-')
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

            ct=[ph,Fname,Lname,Address,city]
            f = open(r'Address.dat',"ab")
            pickle.dump(ct,f)
            f.close()
            
            print('THE CONACT IS ADDED SUCCESSFULLY')
            speaker.say("THE CONACT IS ADDED SUCCESSFULLY")
            speaker.runAndWait()
            print('~'*60)
            
            






            

