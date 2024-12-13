#FINALS PROJECT FOR ITCS102
#JOHN DERICK GAVIOLA IT1C
import os
print("\nGood day! I'm John Derick Gaviola and this is the programs I created through out my 1st year/1st sem of my college year. \nHope u enjoy exploring! ")

tuloy = True
while tuloy == True:
    print("\n======================================================================================\n\nCode_Challenge1 --- 1 \tCode_Challenge11 --- 11 \tActivity1 --- 101 \nCode_Challenge2 --- 2 \tCode_Challenge12 --- 12 \tActivity2 --- 102 \nCode_Challenge3 --- 3 \tCode_Challenge13 --- 13 \tActivity3 --- 103 \nCode_Challenge4 --- 4 \tCode_Challenge14 --- 14 \tActivity4 --- 104 \nCode_Challenge5 --- 5 \tCode_Challenge15 --- 15 \tActivity5 --- 105 \nCode_Challenge6 --- 6 \tCode_Challenge16 --- 16\nCode_Challenge7 --- 7 \nCode_Challenge8 --- 8 \nCode_Challenge9 --- 9 \nCode_Challenge10 -- 10")
    a = int(input("\nCHOOSE ONLY ONE CHALLENGE OR ACTIVITY U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
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
            print("Hi "+name, "luv u")
        cc2(cc2)
        continue

    elif a == 3:
        os.system('cls')
        def cc3(cc3):
            print("THIS IS CODE CHALLENGE 3")
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
            print("THIS IS CODE CHALLENGE 4")
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
            print("THIS IS CODE CHALLENGE 5")
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
            print("THIS IS CODE CHALLENGE 6")
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

    elif a == 7:
        os.system('cls')
        def cc7(cc7):
            print("THIS IS CODE CHALLENGE 7")
            name = input("Your name: ")
            grocery = input("Do you want to buy? (yes or no): ")
            if grocery.lower() == 'yes':
                print("\nTHIS IS OUR PRODUCTS: \nHOT DOG - $100 \nCORN DOG - $120 \nCHEESY DOG - $150")

                quanti = eval(input("\nHow many HOT DOG you want to buy? "))
                prc = (quanti * 100)
                
                quanti2 = eval(input("\nHow many CORN DOG you want to buy? "))
                prc2 = (quanti2 * 120)
                
                quanti3 = eval(input("\nHow many CHEESY DOG you want to buy? "))
                prc3 = (quanti3 * 150)
                
                total = prc + prc2 + prc3
                tax = round(total * 0.123)
                ttax = round(total + tax)

                id = input("\nDo you have Senior/Student/PWD ID? (yes or no): ")
                if id.lower() == 'yes': 
                    discount = round(ttax * 0.052)
                else: 	
                    discount = 0

                print(f"\nGood day {name}!, you ordered {quanti}pcs of HOT DOG, {quanti2}pcs of CORN DOG and {quanti3}pcs of CHEESY DOG with a price of ${total} with 12.3% of tax with a total of ${ttax}.")
                        
                money = eval(input("\nPlease type the amount you'll give: $"))
                if money >= ttax:
                    change = round(money - ttax + discount)
                    print(f"\n\t\t\t==RECEIPT== \nQty.     Description           Amount\n{quanti}x  ---- HOT DOG ($100) ------ ${prc} \n{quanti2}x  ---- CORN DOG ($120) ----- ${prc2} \n{quanti3}x  ---- CHEESY DOG ($150) --- ${prc3} \n\t SUBTOTAL ------------ ${total} \n\t SALES TAX (12.3%) --- ${tax} \n\t TOTAL --------------- ${ttax} \n\t AMOUNT OF PAY ------- ${money}\n\t DISCOUNT (5.2%) ----- ${discount} \n\t CHANGE -------------- ${change} \n\t\t ==THANK YOU FOR SHOPPING!==")
                else:
                    money<= ttax
                    print("\ninsufficient amount, please try again.\n")

                    
            else: 
                print("\nokay!")	
        cc7(cc7)
        continue
    
    elif a == 8:
        os.system('cls')
        def cc8(cc8):
            print("THIS IS CODE CHALLENGE 8")
            #collect/fetch 10 numbers from the user
            odd = 0
            even = 0
            sum = 0

            for x in range (1, 11):
                #sum = 0
                num = int(input(f"\nEnter #{x}: "))
                sum += num
                if (num % 2) == 0:
                    num += sum == even
                    print("even")
                else:
                    num += sum == odd
                    print("odd")

            print(f"\nThe sum of all given numbers is {sum}\n")
        cc8(cc8)
        continue

    elif a == 9:
        os.system('cls')
        def cc9(cc9):
            print("THIS IS CODE CHALLENGE 9")
            for a in range (11, 0 , -1):
                for b in range (11, a, -1):
                    print(" ",end="")
                print("*" *a)
        cc9(cc9)
        continue

    elif a == 10:
        os.system('cls')
        def cc10(cc10):
            print("THIS IS CODE CHALLENGE 10")
            for a in range (6,1,-1):
                for b in range (a,1,-1):
                    print(" ", end=" ")
                for c in range (a,7,1):
                    print("*",end=" ")
                for d in range (a,6,1):
                    print("^", end=" ")
                print()

            for a in range (1,7):
                for b in range (1,a,1):
                    print(" ", end=" ")
                for c in range (7, a, -1):
                    print("*",end=" ")
                for d in range (6, a, -1):
                    print("^", end=" ")
                print()
        cc10(cc10)
        continue

    elif a == 11:
        os.system('cls')
        def cc11(cc11):
            print("THIS IS CODE CHALLENGE 11")
            for a in range (7,1,-1):
                for b in range (1, a + 1):
                    print(" ", end=" ")
                for c in range (7, a, -1):
                    print("*",end=" ")
                for d in range (6, a, -1):
                    print("*", end=" ")
                print()

            for a in range (1,7):
                for b in range (1, a +1):
                    print(" ", end=" ")
                for c in range (4, a, -1):
                    print("*",end=" ")
                for d in range (6, a, -1):
                    print("*", end=" ")
                print()
        cc11(cc11)
        continue

    elif a == 12:
        os.system('cls')
        print("THIS IS CODE CHALLENGE 12")
        def cc12(cc12):
            for j in range (1,5):
                for z in range (5, j, -1):
                    print(" ", end=" ")
                for y in range (1, j + 1):
                    print("*",end=" ")
                for x in range (1, j+1):
                    print("*", end=" ")
                print() 

            for c in range (0,4):
                for b in range (4, 0, -1):
                    print(" ", end=" ")
                for d in range (2,4):
                    print("*",end=" ")
                for a in range (4,0,-1):
                    print("  ",end=" ")
                print()
        cc12(cc12)
        continue

    elif a == 13:
        os.system('cls')
        def cc13(cc13):
            print("THIS IS CODE CHALLENGE 13")
            for x in range (1,7):
                for y in range (6, x, -1):
                    print(" ", end=" ")
                for z in range (x, 1, -1):
                    print(z, end=" ")
                for a in range(1, x + 1):
                    print(a, end=" ")
                print()

            for x in range (5,0,-1):
                for y in range (6, x, -1):
                    print(" ", end=" ")
                for z in range (x, 1, -1):
                    print(z, end=" ")
                for a in range(1, x + 1):
                    print(a, end=" ")
                print()
        cc13(cc13)
        continue

    elif a == 14:
        os.system('cls')
        def cc14(cc14):
            print("THIS IS CODE CHALLENGE 14")
            #loop has terminated
            #the sum of all the numbers given is it

            tuloy = True
            total = 0

            while tuloy == True:
                num = eval(input("\nenter a number: "))

                if num ==0:
                    print("\n\tProgram Terminated")
                    print(f"\nThe total of your numbers are {total}")
                    break

                else:
                    total += num
                    continue
        cc14(cc14)
        continue

    elif a == 15:
        os.system('cls')
        def cc15(cc15):
            print("THIS IS CODE CHALLENGE 15")
            import os
            isContinue = True
            no = 0
            while isContinue == True:
                ask = input("\ndo u want triangle? (yes/no): ")

                if ask.lower()== "no":
                    os.system("cls")
                    print("\tProgram Terminated")
                    break
                    isContinue = False

                elif ask.lower()== "yes":
                    os.system('cls')
                    no += 1
                    for a in range (1,6):
                        for d in range (1,no + 1):
                            for b in range (1, a + 1):
                                print ("*", end=" ")

                            for c in range ( 6, a, -1):
                                print(" ", end=" ")
                        print()
                    continue
                else:
                    os.system("cls")
                    print("invalid input, please try again!")
                    continue
        cc15(cc15)
        continue

    elif a == 16:
        os.system('cls')
        def cc16(cc16):
            print("THIS IS CODE CHALLENGE 16")
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
  