import os
import csv
import pandas as pd

file_path = r'C:\Users\kx2le\OneDrive\桌面\BA_IA\BA_Store data.csv'

def find_user_by_id(file_path, id):
    if os.path.exists(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0] == id:
                    return row
    return None            

def write_user_id(file_path, id, ic, password):
    file_exists = os.path.isfile(file_path)
    is_empty = os.path.getsize(file_path) == 0 if file_exists else True

    with open(file_path, mode='a',newline = '')as file:
        writer = csv.writer(file)
        if is_empty:
            writer.writerow(['id', 'ic', 'password', 'income', 'tax_relief', 'tax_payable'])
        writer.writerow([str(id),str(ic).zfill(12),str(password).zfill(4), '', '', '']) 

def verify_user(ic, password):
    if len(ic) == 12 and ic.isdigit():
        return password == ic[-4:]
    else:
        return False
    
def tax_relief():
    relief = 0

    while True:
        choice = input("Are you Single? 1-Yes, 2-No: ")
        if choice == '1':
            individual = float(input("Enter your individual tax relief (Max RM9000): ") or 0)
            relief += min(individual, 9000)
            break
        elif choice == '2':
            spouse = float(input("Enter your spouse relief (Max RM4000): ") or 0)
            relief += min(spouse, 4000)

            while True:
                choice2 = input("Do you have children? 1-Yes, 2-No: ")
                if choice2 == '1':
                    children = int(input("How many children? [Max 12]: ") or 0)
                    relief += min(children, 12) * 8000
                    break
                elif choice2 == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")
            break
        else:
            print("Invalid choice. Please try again")

    medical = float(input("Medical expenses? (Max RM8000): ") or 0)
    lifestyle = float(input("Lifestyle purchases? (Max RM2500): ") or 0)
    education = float(input("Education fees? (Max RM7000): ") or 0)
    parent = float(input("Parental care relief? (Max RM5000): ") or 0)

    relief += min(medical, 8000)
    relief += min(lifestyle, 2500)
    relief += min(education, 7000)
    relief += min(parent, 5000)
    return relief

def calculate_tax(income, tax_relief):
    chargeble_income = income - tax_relief

    if (chargeble_income <=0) :
        return 0.00
    if chargeble_income <= 5000:
        rate = 0.00
    elif chargeble_income >5000 and chargeble_income <=20000:
        rate = 0.01
    elif chargeble_income >20000 and chargeble_income <=35000:
        rate = 0.03
    elif chargeble_income >35000 and chargeble_income <=50000:
        rate = 0.06       
    elif chargeble_income >50000 and chargeble_income <=70000:
        rate = 0.11
    elif chargeble_income >70000 and chargeble_income <=100000:
        rate = 0.19
    elif chargeble_income >100000 and chargeble_income <=400000:
        rate = 0.25
    elif chargeble_income >400000 and chargeble_income <=600000:
        rate = 0.26
    elif chargeble_income >600000 and chargeble_income <=2000000:
        rate = 0.28
    else:
        rate = 0.30

    tax = chargeble_income*rate
    return round(tax, 2)

def save_to_csv(id, income, tax_relief, tax_payable, file_path):
    rows = []

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == str(id):
                while len(row) < 6:
                    row.append('')
                row[3] = str(income)
                row[4] = str(tax_relief)
                row[5] = str(tax_payable)
            rows.append(row)  

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def read_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File '{file_path}' does not exist.")
        return None
    try:
        df = pd.read_csv(file_path, dtype={'password': str})  # ✅ 正确调用 pandas 的 read_csv
        return df
    except Exception as e:
        print(f"❌ Error reading the file: {e}")
        return None

