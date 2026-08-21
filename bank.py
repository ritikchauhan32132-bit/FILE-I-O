import random


account = {}

while True:

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")
    print()

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number!")
        continue
    
    print("_"*30)
    
    
    match choice:
        
        case 1:
            print("_"*30)
            print("=== Create Account ===")
            ac_number = random.randint(101,10001)
            name = input("Enter Name: ")
                        
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Please Enter the age in Number: ")
                continue
                
            mobile = input("Enter Mobile Number: ")
            account[ac_number] = {
                "name":name,
                "account":ac_number,
                "mobile":mobile,
                "age":age,
                "Balance":500
            }
            
            
            with open("customer.txt", "a") as f:
                f.write(
                    f"Name: {name}\n"
                    f"Age: {age}\n"
                    f"Mobile: {mobile}\n"
                    f"Account: {ac_number}\n"
                    f"Balance: {account[ac_number]["Balance"]}\n"
                    f"{'-'*30}\n"
                )
                print("_"*30)
            print("Account Created sucessfully! ")
            print(f"Account Number is: {ac_number}")
            print(f"You have: {account[ac_number]["Balance"]}")
            print("_"*30)
            
        case 2:
            print("=== Deposite Balance ===")
            check_ac = int(input("Enter Account Number: "))
            
            if(check_ac in account):
                deposite = float(input("How Many Ammount Deposite In Account: "))
                if deposite > 0:
                    account[check_ac]["Balance"] += deposite
                else:
                    print("Amount must be greater than 0!")
                            
                print(f"Your Balance is: {account[check_ac]["Balance"]}")
                print("_"*30)
            
                with open("transtion.txt","a") as f:
                    f.write(
                        f"Account Number : {check_ac} \n"
                        f"Before Deposite Balance: {account[check_ac]["Balance"]}\n"
                        f"Deposit Balance : {deposite} \n"
                        f"Total Balance: {account[check_ac]["Balance"]}\n"
                        f"{"_"*30}\n"
                    )
                    
                
            else:
                print("Invailed Account!")
                
                
        case 3:
            # Withdrow
            check_ac = int(input("Enter Account Number: "))
            if(check_ac in account):
                withrow = int(input("Enter Withrowal Moner: "))
                if withrow <= account[check_ac]["Balance"]:
                    account[check_ac]["Balance"] -= withrow
                else:
                    print("Insufficient Balance!")
                    
                print("Withrow Seccussfully: ",withrow)
                print("Avlable Balance: ",account[check_ac]["Balance"])
                print("_"*30)
                before_withdraw = account[check_ac]["Balance"]

                account[check_ac]["Balance"] -= withrow

                after_withdraw = account[check_ac]["Balance"]
                
                with open("transtion.txt","a") as f:
                    f.write(
                        f"Account Number: {check_ac}\n"
                        f"Before Withdraw: {before_withdraw}\n"
                        f"Withdrawal Amount: {withrow}\n"
                        f"Current Balance: {after_withdraw}\n"
                        f"{"_"*30}\n"
                    )
            else:
                print("Invailed Account!")
                
        case 4:
            # Check Balance
            print("_"*30)
            print("=== Check Balance ===")
            check_ac = int(input("Enter Account Number: "))
            
            if(check_ac in account):
                print(f"Hello {account[check_ac]["name"]} \nBalance: {account[check_ac]["Balance"]}")
            else:
                print("Invailed Account Number!")
                
                
                
            print("_"*30)
                
        case 5:
            print("_"*30)
            print("=== Transation History ===")
            check_ac = int(input("Enter Account Number: "))
            
            with open("transtion.txt","r") as f:
                lines = f.readlines()
                
                transation = []
                for line in lines:
                    if f"Account Number: {check_ac}" in line:
                        transation.append(line)
                    elif transation:
                        transation.append(line)
                if "_"*30 in line:
                    print("".join(transation))
                    transation = []
                    
        case 6:
            print("Exit!")
            break
        
        case _:
            print("Invailed Choice!")
