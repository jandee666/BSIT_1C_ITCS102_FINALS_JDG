#FINALS PROJECT FOR ITCS102
#JOHN DERICK GAVIOLA IT1C
#John Derick Gaviola on Github ^-^
import os
import datetime
print("\nGood day! I'm John Derick Gaviola and this is the programs I created through out my 1st year/1st sem of my college year.\nHope u enjoy exploring! :D\n")

tuloy = True
while tuloy == True:
    date = datetime.date.today()
    print(date)
#THIS IS THE MENU
#I MAKE IT SIMPLE SO ITS EASY TO ACCESS
    print("=======================================================")
    print("||     CODE CHALLENGE       |          ACTIVITY      ||")
    print("=======================================================")
    print("|| CODE CHALLENGE1 == 1     |      ACTIVITY1 == 101  ||")
    print("|| CODE CHALLENGE2 == 2     |      ACTIVITY2 == 102  ||")
    print("|| CODE CHALLENGE3 == 3     |      ACTIVITY3 == 103  ||")
    print("|| CODE CHALLENGE4 == 4     |      ACTIVITY4 == 104  ||")
    print("|| CODE CHALLENGE5 == 5     |      ACTIVITY5 == 105  ||")
    print("|| CODE CHALLENGE6 == 6     |      ACTIVITY6 == 106  ||")
    print("|| CODE CHALLENGE7 == 7     |      ACTIVITY7 == 107  ||")
    print("|| CODE CHALLENGE8 == 8     |      ACTIVITY8 == 108  ||")
    print("|| CODE CHALLENGE9 == 9     |      ACTIVITY9 == 109  ||")
    print("|| CODE CHALLENGE10 = 10    |      ACTIVITY10 = 110  ||")
    print("|| CODE CHALLENGE11 = 11    |      ACTIVITY11 = 111  ||")
    print("|| CODE CHALLENGE12 = 12    |      ACTIVITY12 = 112  ||")
    print("|| CODE CHALLENGE13 = 13    |      ACTIVITY13 = 113  ||")
    print("|| CODE CHALLENGE14 = 14    |      ACTIVITY14 = 114  ||")
    print("|| CODE CHALLENGE15 = 15    |      ACTIVITY15 = 115  ||")
    print("|| CODE CHALLENGE16 = 16    |      ACTIVITY16 = 116  ||")
    print("||                          |      ACTIVITY17 = 117  ||")
    print("||                          |      ACTIVITY18 = 118  ||")
    print("||                          |      ACTIVITY19 = 119  ||")
    print("||                          |      ACTIVITY20 = 120  ||")
    print("||                          |      ACTIVITY21 = 121  ||")
    print("||                          |      ACTIVITY22 = 122  ||")
    print("||                          |      ACTIVITY23 = 123  ||")
    print("||                          |      ACTIVITY24 = 124  ||")
    print("||                          |      ACTIVITY25 = 125  ||")
    print("=======================================================")
    print("||             TERMINATE THE PROGRAM == 0            ||")
    print("=======================================================")
    print("                  ᴶᵒʰⁿ ᴰᵉʳᶦᶜᵏ ᴳᵃᵛᶦᵒˡᵃ                  ")

    a = input("\nCHOOSE ONLY ONE CHALLENGE OR ACTIVITY U WANT TO OPEN (TYPE ONLY THE NUMBER): ")

# CODE CHALLENGE 1
    if a == "1":
        os.system("cls") 
        def cc1(cc1):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 1")
            print("\t\t\t\t\t\t\t\t\b*\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b\b\b*********\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b*")
        cc1(cc1)
        continue

#CODE CHALLENGE 2
    elif a == "2":
        os.system('cls')
        def cc2(cc2):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 2")
            name = input ("Your name: ")
            print(" \t\t\t\t\t\t\t\t\b*\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b\b\b*"+name+"*\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b*")
        cc2(cc2)
        continue

#CODE CHALLENGE 3
    elif a == "3":
        os.system('cls')
        def cc3(cc3):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 3")
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

#CODE CHALLENGE 4
    elif a == "4":
        os.system('cls')
        def cc4(cc4):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 4")
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

#CODE CHALLENGE 5
    elif a == "5":
        os.system('cls')
        def cc5(cc5):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 5")
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

#CODE CHALLENGE 6
    elif a == "6":
        os.system('cls')
        def cc6(cc6):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 6")
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

#CODE CHALLENGE 7
    elif a == "7":
        os.system('cls')
        def cc7(cc7):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 7")
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
    
#CODE CHALLENGE 8
    elif a == "8":
        os.system('cls')
        def cc8(cc8):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 8")
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

#CODE CHALLENGE 9
    elif a == "9":
        os.system('cls')
        def cc9(cc9):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 9")
            for a in range (11, 0 , -1):
                for b in range (11, a, -1):
                    print(" ",end="")
                print("*" *a)
        cc9(cc9)
        continue

#CODE CHALLENGE 10
    elif a == "10":
        os.system('cls')
        def cc10(cc10):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 10")
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
#CODE CHALLENGE 11
    elif a == "11":
        os.system('cls')
        def cc11(cc11):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 11")
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

#CODE CHALLENGE 12
    elif a == "12":
        os.system('cls')
        print("\n\t\t\tTHIS IS CODE CHALLENGE 12")
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

#CODE CHALLENGE 13
    elif a == "13":
        os.system('cls')
        def cc13(cc13):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 13")
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

#CODE CHALLENGE 14
    elif a == "14":
        os.system('cls')
        def cc14(cc14):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 14")
            #loop has terminated
            #the sum of all the numbers given is it

            tuloy = True
            total = 0

            while tuloy == True:
                num = eval(input("\nenter a number: "))

                if num == 0:
                    print("\n\tProgram Terminated")
                    print(f"\nThe total of your numbers are {total}")
                    break

                else:
                    total += num
                    continue
        cc14(cc14)
        continue

#CODE CHALLENGE 15
    elif a == "15":
        os.system('cls')
        def cc15(cc15):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 15")
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
                    print("\n\t\t\tTHIS IS CODE CHALLENGE 15")
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
                    print("\n\t\t\tTHIS IS CODE CHALLENGE 15")
                    print("invalid input, please try again!")
                    continue
        cc15(cc15)
        continue

#CODE CHALLENGE 16
    elif a == "16":
        os.system('cls')
        def cc16(cc16):
            print("\n\t\t\tTHIS IS CODE CHALLENGE 16")
            def breakdown_denomination(amount):
                print("Denomination Breakdown:")
                denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
                for denom in denominations:
                    if amount >= denom:
                        count = amount // denom
                        print("PHP", denom, ":", count)
                        amount = amount % denom


            def create_account():
                account_name = input("Enter your name: ")
                initial_deposit = eval(input("Enter initial deposit: "))
                if initial_deposit >= 0:
                    print("Account created for", account_name, "with balance PHP", initial_deposit)
                    return account_name, initial_deposit
                else:
                    print("Initial deposit must be 0 or more.")
                    return None, 0


            def deposit(account_name, account_balance):
                if account_name == None:  
                    print("No account found. Please create an account first.")
                else:
                    amount = eval(input("Enter amount to deposit: "))
                    if amount > 0:
                        account_balance += amount
                        print("Deposited PHP", amount, ". Current balance: PHP", account_balance)
                        breakdown_denomination(amount)
                    else:
                        print("Deposit amount must be greater than 0.")
                return account_balance


            def withdraw(account_name, account_balance):
                if account_name == None:
                    print("No account found. Please create an account first.")
                else:
                    amount = eval(input("Enter amount to withdraw: "))
                    if amount > account_balance:
                        print("Insufficient balance!")
                    elif amount > 0:
                        account_balance -= amount
                        print("Withdrew PHP", amount, ". Current balance: PHP", account_balance)
                    else:
                        print("Withdrawal amount must be greater than 0.")
                return account_balance


            def check_balance(account_name, account_balance):
                if account_name == None:
                    print("No account found. Please create an account first.")
                else:
                    print("Your current balance is PHP", account_balance)


            def main():
                account_name = None
                account_balance = 0

                while True:
                    print("\n=== Welcome to MYBank ===")
                    print("1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Balance")
                    print("5. Exit")
                    choice = input("Choose an option (1-5): ")

                    if choice == "1":
                        account_name, account_balance = create_account()
                    elif choice == "2":
                        account_balance = deposit(account_name, account_balance)
                    elif choice == "3":
                        account_balance = withdraw(account_name, account_balance)
                    elif choice == "4":
                        check_balance(account_name, account_balance)
                    elif choice == "5":
                        print("Thank you for using the banking system!")
                        break
                    else:
                        print("Invalid option. Please try again.")

            main()

        cc16(cc16)
        continue

#ACTIVITY 1
    elif a == "101":
        os.system('cls')
        def act1(act1):
            print("\n\t\t\tTHIS IS ACTIVITY 1")
            print("\nHello World!")
        act1(act1)
        continue

#ACTIVITY 2
    elif a == "102": 
        os.system('cls')
        def act2(act2):
            print("\n\t\t\tTHIS IS ACTIVITY 2")
            name = input("Please enter a name: ")
            print("\nHi "+name, "luv u")
        act2(act2)
        continue

#ACTIVITY3
    elif a == "103":
        os.system('cls')
        def act3(act3):
            print("\n\t\t\tTHIS IS ACTIVITY 3\n")
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
        act3(act3)
        continue

#ACTIVITY 4
    elif a == "104":
        os.system('cls')
        def act4(act4):
            print("\n\t\t\tTHIS IS ACTIVITY 4\n")
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
        act4(act4)
        continue

#ACTIVITY 5
    elif a == "105":
        os.system('cls')
        def act5(act5):
            print("\n\t\t\tTHIS IS ACTIVITY 5\n")
            print("FAHRENHEIT TO CELSIUS CONVERTER ")
            temp = eval(input("\nEnter Temperature in Fahrenheit: "))
            
            celsius = (temp - 32) * 5 / 9 

            print ("\nThe Conversion of",temp,"degrees Fahrenheit is", celsius, "degrees celsius. ")
            
            print(f"\nThe Conversion of {temp} degrees Fahrenheit is {celsius} degrees celsius.\n")

            print(round(celsius, 2))

            print(f"\nThis Conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees celsius.")
        act5(act5)
        continue
    
#ACTIVITY 6
    elif a == "106":
        os.system('cls')
        def act6(act6):
            print("\n\t\t\tTHIS IS ACTIVITY 6\n")
            x = 5
            print(x)

            x = 10
            print(x)

            x = 15
            print(x)

            x = 20 
            print(x)

            x += 25
            print(x)
            
            x -= 30
            print(x)
        act6(act6)
        continue

#ACTIVITY 7
    elif a == "107":
        os.system('cls')
        def act7(act7):
            print("\n\t\t\tTHIS IS ACTIVITY 7\n")
            gold = 0 

            miner = input("Hi, please enter your name: ")

            hasMine = input("Did you mine gold today? ")

            if hasMine.lower() == "yes":	  
                gold += 1
                print(f"\nHi {miner}, Today you have a total of {gold} gold")
            else:
                print(f"\nHi {miner}, Today you have a total of {gold} gold")
        act7(act7)
        continue

#ACTIVITY 8
    elif a == "108":
        os.system('cls')
        def act8(act8):
            print("\n\t\t\tTHIS IS ACTIVITY 8\n")
            password = input("Enter your password: ")

            if password.lower() == "secret":
                print("Access Granted!")
                print("Welcome!")

            elif password.lower() == "hidden":
                print("Access Granted, Master!")
                print("Welcome, Master!")

            else: 
                print("Wrong password, try again!")

            print("Thankyou for using the system!")

        act8(act8)
        continue

#ACTIVITY 9
    elif a == "109":
        os.system('cls')
        def act9(act9):
            print("\n\t\t\tTHIS IS ACTIVITY 9\n")
            #age
            age = eval(input("Enter your age: "))

            if age > 100:
                print("\nyou are an Ancient One")

            elif age >= 60:
                print("\nyou are a Senior Citizen")

            elif age >= 46:	
                print("\nyou are in a Post Adulthood")

            elif age >= 32:
                print("\nyou are in a Mid Adulthood")

            elif age >= 19:
                print("\nyou are in a Early Adulthood")

            elif age >= 14:
                print("\nyou are a Teenager")

            elif age >= 8:
                print("\nyou are a Pre teen")

            elif age >= 1:
                print("\nyou are a Toddler")

            elif age < 1:
                print("\nCondolence :(")
        act9(act9)
        continue

#ACTIVITY 10
    elif a == "110":
        os.system('cls')
        def act10(act10):
            print("\n\t\t\tTHIS IS ACTIVITY 10")
            isDLL = input("Are you a current student of DLL? (yes or no) ")

            if isDLL.lower() == 'yes':
                print("\nWelcome to DLL!")
                level = input("\nWhat is your current year level right now in DLL? \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior \nPlease type your answer: ")

                if level.lower() == 'f':
                    print("\nHi Freshmen!")
                elif level.lower() == 's':
                    print("\nHi Sophomore!")
                elif level.lower() == 'j':
                    print("\nHi Junior!")
                elif level.lower() == 'r':
                    print("\nHi Senior!")
                else:
                    print("\nInvalid Choice")

            else:	
                print("oki")
        act10(act10)
        continue

#ACTIVITY 11
    elif a == "111":
        os.system('cls')
        def act11(act11):
            print("\n\t\t\tTHIS IS ACTIVITY 11")
            #print Hello World 10 times
            for x in range (1, 11):
                print("\nHello World")
                print("Welcome!")
                name = input("enter your name: ")
                print(f"Hello {name}")
        act11(act11)
        continue

#ACTIVITY 12
    elif a == "112":
        os.system('cls')
        def act12(act12):
            print("\n\t\t\tTHIS IS ACTIVITY 12")
            # 10 to 1
            for x in range (10, 0, -1):
                print(x)
        act12(act12)
        continue

#ACTIVITY 13
    elif a == "113":
        os.system('cls')
        def act13(act13):
            print("\n\t\t\tTHIS IS ACTIVITY 13")
            #factorial
            num = eval(input("enter a number: "))

            f = 1

            for x in range(num, 0, -1):
                f *= x

            print(f"The factorial of {num} is {f}")
        act13(act13)
        continue

#ACTIVITY 14
    elif a == "114":
        os.system('cls')
        def act14(act14):
            print("\n\t\t\tTHIS IS ACTIVITY 14")
            # washing machine
            # settings
            for x in range (0, 10):
                for y in range (0, 10):
                    print("", end = "")
                print("labyu") #laundry

        act14(act14)
        continue

#ACTIVITY 15
    elif a == "115":
        os.system("cls")
        def act15(act15):
            print("\n\t\t\tTHIS IS ACTIVITY 15")
            for i in range (11, 0, -1):
                print(end="")
                for y in range ( 11, i, -1):
                    print("*", end="")
                print()
        act15(act15)
        continue

#ACTIVITY 16
    elif a == "116":
        os.system('cls')
        def act16(act16):
            print('\n\t\t\tTHIS IS ACTIVITY 16')
            for a in range (1,6):
                for b in range (1, a+1):
                    print(" ", end=" ")
                for c in range (6, a, -1):
                    print(" * ",end=" ")
                print()
        act16(act16)
        continue

#ACTIVITY 17
    elif a == "117":
        os.system("cls")
        def act17(act17):
            print("\n\t\t\tTHIS IS ACTIVITY 17")
            #multiplication table
            a = eval(input("Enter a column:  "))
            for b in range (1,11):
                for c in range (1, a +1):
                    print(f"{b} x {c} = {a*b}", end = "\t")
                print( )
        act17(act17)
        continue

#ACTIVITY 18
    elif a == "118":
        os.system('cls')
        def act18(act18):
            print("\n\t\t\tTHIS IS ACTIVITY 18")
            import os

            col = eval(input("how many do u want to make? "))
            for a in range (1,6):
                for d in range (1,col + 1):
                    for b in range (1, a + 1):
                        print ("*", end=" ")

                    for c in range ( 6, a, -1):
                        print(" ", end=" ")
                print()
        act18(act18)
        continue

#ACTIVITY 19
    elif a == "119":
        os.system('cls')
        def act19(act19):
            print("\n\t\t\tTHIS IS ACTIVITY 19")
            print("\n(type STOP to terminate the program) ")
            #requirements and syntax of a while loop
            #sceario, ask user to give a name, and say hi to that name until user types the word 'stop'

            #boolean variable / trigger
            tuloy = True

            #keyword while

            while tuloy == True:
                name = input("name: ")

                #stopping point
                if name.lower()== "stop":
                    print("\tProgram Terminated")
                    break
                    #tuloy = False
                else:
                    continue
        act19(act19)
        continue

#ACTIVITY 20
    elif a == "120":
        os.system('cls')
        def act20(act20):
            print("\n\t\t\tTHIS IS ACTIVITY 20")
            #HYBRID LOOP
            import os
            isContinue = True
            no = 0
            while isContinue == True:
                ask = input("\ndo u want triangle? (yes/no): ")

                if ask.lower()== "no":
                    print("\tProgram Terminated")
                    break
                    # isContinue = False
                elif ask.lower() == "yes":
                    os.system('cls')
                    print("\n\t\t\tTHIS IS ACTIVITY 20")
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
                    os.system('cls')
                    print("\n\t\t\tTHIS IS ACTIVITY 20")
                    print("WRONG INPUT! PLS TRY AGAIN!")
                    continue
        act20(act20)
        continue
    
#ACTIVITY 21
    elif a == "121":
        os.system('cls')
        def act21(act21):
            print("\n\t\t\tTHIS IS ACTIVITY 21")
            import os
            def pang_hello():
                print("helloooo")

            #function with parameter
            def pang_hello_v2(name):
                print(f"Hello {name}")

            def activity2():
                num1 = eval(input("enter any number: "))
                num2 = eval(input("enter any number: "))
                answer = num1 + num2
                print(num1, "plus",num2, "=", answer)

            tuloy = True
            while tuloy == True:
                ask = input("enter a name: ")

                if ask.lower() != 'stop':
                    os.system("cls")
                    pang_hello_v2(ask)
                    if ask == '2':
                        activity2()
                        continue
                else:
                    os.system("cls")
                    break
        act21(act21)
        continue

#ACTIVITY 22
    elif a == "122":
        os.system('cls')
        def act22(act22):
            print("\n\t\t\tTHIS IS ACTIVITY 22")
            def activity22():
                def activity1():
                    print("Hello World")
                activity1()
            activity22()

        act22(act22)
        continue

#ACTIVITY 23
    elif a == "123":
        os.system('cls')
        def act23(act23):
            print("\n\t\t\tTHIS IS ACTIVITY 23")
            def factorial(number):
                # This function's purpose is to compute/calculate the factorial of any number given 
                fact = 1
                for x in range(number, 0, -1):
                    fact *= x

                return fact

            print(f"the factorial of 13 is {factorial(13)}")
        act23(act23)
        continue

#ACTIVITY 24
    elif a == "124":
        os.system('cls')
        def act24(act24):
            print("\n\t\t\tTHIS IS ACTIVITY 24")
            from Activity23_sample import factorial

            print(f"the factorial of 7 is {factorial(7)} ")
        act24(act24)
        continue

#ACTIVITY 25
    elif a == "125":
        os.system('cls')
        def act25(act25):
            print("\n\t\t\tTHIS IS ACTIVITY 25")
            courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

            courses.remove("Delete w/o index")
            courses.pop()
            courses.append("DHRS")
            courses.insert(0, "ABELS")

            print(courses)

        act25(act25)
        continue

#EXIT OR TERMINATE THE PROGRAM
    elif a == "0":
        os.system('cls')
        def exit(exit):
            print("\nAND THATS THE PROGRAMS I'VE CREATED THROUGH OUT MY 1ST SEM/YEAR OF COLLEGE AT DALUBHASAAN NG LUNGSOD NG LUCENA(DLL). \nHOPE YOU ENJOY EXPLORING FROM MY CODES!! THANK YOU!! THIS IS JOHN DERICK GAVIOLA SIGNING OFF, ADIOS!\n")
        exit(exit)
        break

#FOR WRONG OR RANDOM INPUTS
    else:
        os.system('cls')
        def wrong(wrong):
            print("\n\t\t\twrong input! please try again!")
        wrong(wrong)
        continue

#THANK YOU