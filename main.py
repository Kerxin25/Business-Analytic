import csv
import os
import function

file_path = r'C:\Users\kx2le\OneDrive\桌面\BA_IA\BA_Store data.csv'

print("WELCOME TO TAX CALCULATOR")
print("Do you already register as a user? \nYes-1 \nNo-2")
choice = input()

if choice == '1':
    while True:
        id = input("Please enter your user ID: ")
        user = function.find_user_by_id(file_path, id)
        if user:
            break  # 找到用户，跳出循环
        else:
            print("❌ Incorrect user ID! Please try again or type 'exit' to quit.")
            if id.lower() == 'exit':
                exit()

    ic = user[1]

    while True:
        password = input("Please enter your password (Last 4 digits of your IC): ").strip()
        if function.verify_user(ic, password):
            print("✅ Login successful!")
            print("User id:", user[0])
            print("IC number:", ic)
            print("Password:", user[2])

            print("-----WELCOME TO TAX CALCULATOR-----")
            income = float(input("Please enter your annual income(RM): "))
            tax_relief = function.tax_relief()
            tax_payable = function.calculate_tax(income, tax_relief)

            print("💰 Your annual income is: RM" + str(income))
            print("💰 Your tax relief is: RM" + str(tax_relief))            
            print("💰 Your tax payable is: RM" + str(tax_payable))

            function.save_to_csv(user[0], income, tax_relief, tax_payable, file_path)
            print("📁 Your income, tax relief, and tax payable have been saved.")

            choice2 = input("Do you want to display all the data? 1-Yes, 2-No").strip()
            while True:
                if choice2 == '1':
                    password = input("Please enter the password: ")
                    if password == '1234':
                        df = function.read_from_csv(file_path) 
                        if df is not None:
                            print("📊 Data loaded successfully:")
                            print(df.head())
                        else:
                            print("❌ Failed to load data.")
                        print("That's all, Thank you for using this calculator")
                        break
                    else:
                        print("Incorrect password.")
                elif choice2 == '2':
                    print("-----That's all, Thank you for using this calculator-----")
                    break
                else:
                    choice2 = input("Please enter a valid number! (1-Yes, 2-No): ").strip()
            break
        else:
            print("Incorrect password! Please try again or type 'exit' to quit.")
            if password.lower() == 'exit':
                print("Exiting login process.")
                break

elif choice == '2':
    while True:
        id = input("Please enter your user id: ")
        user = function.find_user_by_id(file_path,id)
        if user:
            print("Sorry, this user id already exists!")
        else:
             break
            
    while True: 
        ic = input("please enter your password(your 12-digit IC number):")
        if len(ic) == 12 and ic.isdigit():
            password = ic[8:]
            print("Your user id is: " + id + "\nYour password is: " + password)
            break
        else:
            print("Please enter proper digit of your IC number (12 digits)")

    function.write_user_id(file_path, id, ic, password)
    print("Your data has already stored successfully!")
    
    # Login after registration
    while True:
        id = input("Enter your user ID: ")
        user = function.find_user_by_id(file_path, id)
        if user:
            break
        else:
            print("Id invalid! please make sure you have input correct id.")

    ic = user[1]

    while True:
        password = input("Please enter your password (Last 4 digits of your IC): ").strip()
        if function.verify_user(ic, password):
            print("✅ Login successful!")
            print("User id:", user[0])
            print("IC number:", ic)
            print("Password:", user[2])

            print("-----WELCOME TO TAX CALCULATOR-----")
            income = float(input("Please enter your annual income(RM): "))
            tax_relief = function.tax_relief()
            tax_payable = function.calculate_tax(income, tax_relief)

            print("💰 Your annual income is: RM" + str(income))
            print("💰 Your tax relief is: RM" + str(tax_relief))            
            print("💰 Your tax payable is: RM" + str(tax_payable))

            function.save_to_csv(user[0], income, tax_relief, tax_payable, file_path)
            print("📁 Your income, tax relief, and tax payable have been saved.")

            choice2 = input("Do you want to display all the data? 1-Yes, 2-No").strip()
            while True:
                if choice2 == '1':
                    password = input("Please enter the password: ")
                    if password == '1234':
                        df = function.read_from_csv(file_path) 
                        if df is not None:
                            print("📊 Data loaded successfully:")
                            print(df.head())
                        else:
                            print("❌ Failed to load data.")
                        print("That's all, Thank you for using this calculator")
                        break
                    else:
                        print("Incorrect password.")
                elif choice2 == '2':
                    print("-----That's all, Thank you for using this calculator-----")
                    break
                else:
                    choice2 = input("Please enter a valid number! (1-Yes, 2-No): ").strip()
            break
        else:
            print("Incorrect password! Please try again or type 'exit' to quit.")
            if password.lower() == 'exit':
                print("Exiting login process.")
                break
else:
        print("Error! Automatic exit the system. Please try again.")    
