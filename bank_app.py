import datetime

class Account:
    def __init__(self):
        self.bank_record_list = [[],[],[]] #Inside a list,first list is for current accounts,2nd is for salary accounts, 3rd is for saving accounts

    def create_account(self,obj, account_type):
        dict = {}
        dict["name"] = input("Enter your name : ")
        dict["gender"] = input("Enter your gender : ")
        dict["birth_date"] = input("Enter your date of birth : ")
        dict["number"] = input("Enter your phone number : ")
        dict["address"] = input("Enter your address : ")
        dict["creation_date"] = datetime.date.today()
        balance = int(input("You have to deposite some money for creating this account.Money value must be greater than 10 dollar.Enter the value : "))
        dict["balance"] = balance
        print()

        if account_type == "current":
            global Current_Account_number
            Current_Account_number+=1
            dict["Account Number"] = Current_Account_number
            print("Your Current account number is : ",Current_Account_number)
            obj.bank_record_list[0].append(dict)
        elif account_type == "salary":
            global Salary_Account_number
            Salary_Account_number+=1
            dict["Account Number"] = Salary_Account_number
            print("Your Salary account number is : ", Salary_Account_number)
            obj.bank_record_list[1].append(dict)
        else:
            global Saving_Account_number
            Saving_Account_number+=1
            dict["Account Number"] = Saving_Account_number
            print("Your Saving account number is : ", Saving_Account_number)
            obj.bank_record_list[2].append(dict)

    def __display_all_accounts(self, account_numbers):
        def individual(type,number, name):
            size = len(self.bank_record_list[type])
            for i in range(size):
                if self.bank_record_list[type][i]["Account Number"] == number:
                    print(name, "Details : ")
                    print(self.bank_record_list[type][i])
                    break
        if account_numbers[0]!=-1:
            individual(0, account_numbers[0], "Current_Account")
        if account_numbers[1]!=-1:
            individual(1, account_numbers[1], "Salary_Account")
        if account_numbers[2]!=-1:
            individual(2, account_numbers[2], "Saving_Account")

    def __update_account(self, account_numbers, key, value):
        def individual(type,number):
            size = len(self.bank_record_list[type])
            for i in range(size):
                if self.bank_record_list[type][i]["Account Number"] == number:
                    self.bank_record_list[type][i][key] = value
                    break
        if account_numbers[0]!=-1:
            individual(0, account_numbers[0])
        if account_numbers[1]!=-1:
            individual(1, account_numbers[1])
        if account_numbers[2]!=-1:
            individual(2, account_numbers[2])

    def __delete_account(self, account_type, account_number):
        if account_type == "current":
            type = 0
        elif account_type == "salary":
            type = 1
        else:
            type = 2
        size = len(self.bank_record_list[type])
        for i in range(size):
            if self.bank_record_list[type][i]["Account Number"] == account_number:
                del self.bank_record_list[type][i]
                break

    def __deposit(self, value, account_type, account_number):
        if account_type == "current":
            type = 0
        elif account_type == "salary":
            type = 1
        else:
            type = 2

        size = len(self.bank_record_list[type])
        for i in range(size):
            if self.bank_record_list[type][i]["Account Number"] == account_number:
                self.bank_record_list[type][i]["balance"]+=value
                break 



        

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
                check = input("Are you an employ?Type YES or NO : ")
                if check.lower() == 'yes':
                    objSalaryAccount.create_account(objAccount, "salary")
                else:
                    print("Sorry!You have no permission to create a salary account")
            else:
                objSavingAccount.create_account(objAccount, "saving")
        
        elif operation == 2:
            account_numbers = list(map(int, input("Please enter your Current account,Salary account and Saving account number respectively(if you don't have any account one of them enter -1 in that position): ").split())) # enter 2(if account id is 2 then space) -1 -1(-1 no account)u have to enter three digit one after another with space 2 1 2 or 1 -1 -1
            objAccount._Account__display_all_accounts(account_numbers)

        elif operation == 3:
            print("Before")
            print(objAccount.bank_record_list)
            print()
            account_numbers = list(map(int, input("Please enter your Current account,Salary account and Saving account number respectively(if you don't have any account one of them enter -1 in that position(Ex 2 -1 -1)): ").split())) # enter 2(if account id is 2 then space) -1 -1(-1 no account)u have to enter three digit one after another with space 2 1 2 or 1 -1 -1
            while True:
                key = input("Enter what do you change (name or address or phone number)(if you are not interested to change enter 0) : ")
                if key == '0':
                    break
                elif key.lower() == "name":
                    value = input("Enter the new name : ")

                elif key.lower() == "number":
                    value = input("Enter the new number : ")

                elif key.lower() == "address":
                    value = input("Enter the new address : ")
                else:
                    print("This is not valid.Try another")
                    continue

                objAccount._Account__update_account(account_numbers, key.lower(), value)
                print("After")
                print(objAccount.bank_record_list)
                print()
        
        elif operation == 4:
            print("Before Delete")
            print(objAccount.bank_record_list)
            print()
            account_type = input("Enter the account type which you want to delete(Type : Current/Salay/Saving) : ")
            account_number = int(input("Enter the account number you want to delete : "))
            objAccount._Account__delete_account(account_type.lower(), account_number)
            print("After Delete")
            print(objAccount.bank_record_list)
        
        elif operation == 5:
            value = int(input("How much money you want to deposit : "))
            account_type = input("In which account you want to deposit(Type Current/Saving/Salary) : ")
            account_number = int(input("Enter your account number : "))
            objAccount._Account__deposit(value, account_type.lower(), account_number)


        
        print()

            