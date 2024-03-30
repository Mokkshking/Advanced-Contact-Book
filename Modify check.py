import pickle
import pyttsx3

speaker = pyttsx3.init()

speaker.say('You choose to modify a contact')
speaker.runAndWait()
speaker.say('ENTER THE CONTACT NUMBER TO MODIFY')
speaker.runAndWait()
ph = input("ENTER THE CONTACT NUMBER TO MODIFY ")

fin = open(r'Addressbook.dat',"rb+")
try:
    while True:
        x = pickle.load(fin)
        print(x)
except EOFError:
    print()

if x['Phone no'] == ph:

    pos=fin.tell()
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
        
        def update():
            try:
                while True:
                    pos=fin.tell()
                    stu=pickle.load(fin)
                    stu[1]= new
                    fin.seek(pos)
                    pickle.dump(stu,fin)
                    found = True
            except EOFError:
                if found == False:
                    print('Record not found')
                else:
                    print('success')
                fin.close()
        
        stu={}
        fin.seek(0)
        speaker.say('YOU HAVE CHOOSE TO CHANGE THE FIRST NAME')
        speaker.runAndWait()
        speaker.say("ENTER THE NEW FIRST NAME")
        speaker.runAndWait()
        new = input("ENTER THE FIRST NAME")
        found = False
        
        y=update()
        
        print('FIRST NAME UPDATED')
        print("~" * 60)

