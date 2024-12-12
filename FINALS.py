#FINALS PROJECT FOR ITCS102
#JOHN DERICK GAVIOLA IT1C
import os
print("\nGood day! I'm John Derick Gaviola and this is the programs I created through out my 1st year/1st sem of my college year. \nHope u enjoy exploring! ")

tuloy = True
while tuloy == True:
    print("\n======================================================================================\n\nCode_Challenge1 --- 1 \tCode_Challenge11 --- 11 \tActivity1 --- 101 \nCode_Challenge2 --- 2 \tCode_Challenge12 --- 12 \tActivity2 --- 102 \nCode_Challenge3 --- 3 \tCode_Challenge13 --- 13 \tActivity3 --- 103 \nCode_Challenge4 --- 4 \tCode_Challenge14 --- 14 \tActivity4 --- 104 \nCode_Challenge5 --- 5 \tCode_Challenge15 --- 15 \tActivity5 --- 105 \nCode_Challenge6 --- 6 \tCode_Challenge16 --- 16\nCode_Challenge7 --- 7 \nCode_Challenge8 --- 8 \nCode_Challenge9 --- 9 \nCode_Challenge10 -- 10")
    a = int(input("\nCHOOSE ONLY ONE CHALLENGE U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
    if a == 1:
        os.system("cls")
        def cc1(cc1):
            print("\nTHIS IS CODE CHALLENGE 1")
            print("\t\t\t\t\t\t\t\t\b*\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b\b\b*********\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b*")
        cc1(cc1)
        continue
    if a == 2:
        os.system('cls')
        def cc2(cc2):
            name = input("Please enter a name: ")
            print("Hi"+name, "luv u")
        cc2(cc2)
        continue

    if a == 3:
        os.system('cls')
        def cc3(cc3):
            Fullname = input ("FULL NAME: ")
            Age = input ("AGE: ")
            Birthday = input ("BIRTHDAY: ")
            Birthplace = input ("BIRTH PLACE: ")
            Gender = input("GENDER: ")
            Hobbies = input("HOBBIES/INTERESTS: ")
            Religion = input ("RELIGION: ")
            Ethnicity = input ("ETHNICITY: ")
            Add = input ("CURRENT ADDRESS: ")
            Fname = input ("FATHER'S NAME: ")
            Mname = input ("MOTHER'S NAME: ")
            Contact = input ("CONTACT NUMBER: ")
            Email = input ("EMAIL ADDRESS: ")

            print ("\nMy name is " + Fullname + ", I'm " + Age + " years old, I was born on "+ Birthday +" at "+ Birthplace +" and I'm "+ Gender +". My hobbies/interests is/are "+ Hobbies +". I'm also a/an "+ Religion +" and my nationality is "+ Ethnicity +" and currently living at "+ Add +". My father's name is "+ Fname +" and my mother's name is "+ Mname +". And this is my contact No. and email: "+ Contact+" and "+ Email +" Thankyou!")
        cc3(cc3)
        continue
    
            