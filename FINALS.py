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
        def cc1():
            print("\nTHIS IS CODE CHALLENGE 1")
            print("\t\t\t\t\t\t\t\t\b*\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b\b\b*********\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b*")
        cc1()
        continue
        pass
    elif a == 2:
        os.system('cls')
        def cc2(cc2):
            print("THIS IS CODE CHALLENGE 2")
            name = input("Please enter a name: ")
            print("Hi"+name, "luv u")
        cc2(cc2)
        continue

    elif a == 3:
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
    elif a == 4:
        os.system('cls')
        def cc4(cc4):
            number1 = eval(input("Put a digit here: "))

            number2 = eval(input("Put a digit here: "))

            answer1 = number1 + number2

            answer2 = number1 - number2

            answer3 = number1 * number2

            answer4 = number1 / number2

            answer5 = number1 % number2

            answer6 = number1 ** number2

            answer7 = number1 // number2

            print("\nThe sum of ", number1 ," and ", number2 ," is " , answer1)
            print("The difference of ", number1 ," and ", number2 ," is " , answer2)
            print("The product of ", number1 ," and ", number2 ," is ", answer3)
            print("The qoutient of ", number1 ," and ", number2 ," is ", answer4)
            print("The remainder of ", number1 ," and ", number2 ," is ", answer5)
            print("The exponent of ", number1 ," and ", number2 ," is ", answer6)
            print("The floor division of ", number1 ," and ", number2 ," is ", answer7)
        cc4(cc4)
        continue

    elif a == 5:
        os.system('cls')
        def cc5(cc5):
            name = input("ENTER YOUR NAME: ")
            number1 = eval(input("ENTER AMOUNT TO DEPOSIT: "))
            answer1 = number1 // 1000
            ans1 = number1 % 1000
            answer2 = ans1 // 500
            ans2 = ans1 % 500
            answer3 = ans2 // 200
            ans3 = ans2 % 200
            answer4 = ans3 // 100
            ans4 = ans3 % 100
            answer5 = ans4 // 50
            ans5 = ans4 % 50
            answer6 = ans5 // 20
            ans6 = ans5 % 20
            answer7 = ans6 // 10
            ans7 = ans6 % 10
            answer8 = ans7 // 5
            ans8 = ans7 % 5
            answer9 = ans8 // 1
            ans9 = ans8 % 1

            print("\nHi ",name," the breakdown of your deposit is: ")
            print(answer1,"-1000")
            print(answer2,"-500")
            print(answer3,"-200")
            print(answer4,"-100")
            print(answer5,"-50")
            print(answer6,"-20")
            print(answer7,"-10")
            print(answer8,"-5")
            print(answer9,"-1")
        cc5(cc5)
        continue

    elif a == 6:
        os.system('cls')
        def cc6(cc6):
            #Grading system
            #75 and above is considered PASS 
            #74 and below FAILED

            prelim = eval(input("\nEnter your grade for Prelims: "))
            mid = eval(input("Enter your grade for Midterms: "))
            semifinals = eval(input("Enter your grade for Semifinals: "))
            final = eval(input("Enter your grade for Finals: "))
            quiz = eval(input("Enter your grade for Quizzes: "))
            proj = eval(input("Enter your grade for Projects: "))

            grade = (prelim * .15) + (mid * .15) + (semifinals * .15) + (final * .15) + (quiz * .15) + (proj * .15)

            if grade > 100:
                    print("\nYour grade has exceeded maximum value")

            elif grade >= 75:
                print(f"\nYour grade is {grade}")
                print("Congrats! You Passed!")

            else: 	
                print(f"\nYour Grade is {grade}")
                print("Sorry, You failed.")

            print("\nThank you!")
        cc6(cc6)
        continue
  