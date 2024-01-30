import datetime

class Account:
    def __init__(self):
        self.bank_record_list = [[],[],[]] #first list is for current accounts,2nd is for salary accounts, 3rd is for saving accounts

    def create_account(self,obj, account_type):
        dict = {}
        dict["name"] = input("Enter your name : ")
        dict["number"] = input("Enter your phone number : ")
        dict["creation_date"] = datetime.date.today()
        balance = int(input("You have to deposite some money for creating this account.Money value must be grater than 10 dolar.Enter the value : "))
        dict["balance"] = balance

        if account_type == "current":
            global Current_Account_number
            Current_Account_number+=1
            dict["Account Number"] = Current_Account_number
            obj.bank_record_list[0].append(dict)
        elif account_type == "salary":
            global Salary_Account_number
            Salary_Account_number+=1
            dict["Account Number"] = Salary_Account_number
            obj.bank_record_list[1].append(dict)
        else:
            global Saving_Account_number
            Saving_Account_number+=1
            dict["Account Number"] = Saving_Account_number
            obj.bank_record_list[2].append(dict)

class Current_Account(Account):
    pass

class Salary_Account(Account):
    pass

class Saving_Account(Account):
    pass


if __name__ == "__main__":
    Current_Account_number, Salary_Account_number, Saving_Account_number = 0, 0, 0
    objAccount = Account()
    objCurrentAccount = Current_Account()
    objSalaryAccount = Salary_Account()
    objSavingAccount = Saving_Account()

    while True:
        print("For creating an account enter 1\nFor displaying all accounts enter 2\nFor updating an account enter 3\nFor deleting an account enter 4\nFor deposit an amount into your account enter 5\nFor withdraw an amount from your account enter 6\nSearch for account enter 7\nFor exit enter 8\n")
        operation = int(input("Please enter : "))
        if operation == 8:
            break
        elif operation == 1:
            print("What type of account do you want to create\nFor creating Current Account enter 1\nFor creating Salary Account enter 2\nFor creating Saving Account enter 3\n")
            account_type = int(input("Please Enter : "))
            if account_type == 1:
                objCurrentAccount.create_account(objAccount, "current")
            elif account_type == 2:
                check = input("Are you an employ?Type YES or NO :")
                if check.lower() == 'yes':
                    objSalaryAccount.create_account(objAccount, "salary")
                else:
                    print("Sorrt!You have no permission to create a salary account")
            else:
                objSavingAccount.create_account(objAccount, "saving")
        
        print()
    print(objAccount.bank_record_list)

            