
#account refernce is name not account number
#this bank manegement system has the options of 
# 1.adding account
# 2. deposit money
# 3. withdraw money
#      also tell that how money will be returned
# transfer money 
# 4. show details of both bank accounts  after transferring money
 
details=[341042078372,5000,893899389] #list contains following order [cnic, balance, account_no]
dictionary={"noor":details}

#add account option

choice_to_add=input("do you wan to add account: ").capitalize() 
if choice_to_add == "Yes":
    lst=[]
    name=input("enter name: ")
    CNIC=input("enter cnic: ")
    balance=input("enter balance: ")
    account_no=input("enter account no: ")
    lst.append(CNIC)
    lst.append(balance)
    lst.append(account_no)
    dictionary.update({name:lst})
    print(dictionary)

#code for depositing money

choice_to_deposit=input("do you want to deposit money: ").capitalize()
if choice_to_deposit == "Yes":
    bank=input("enter your name: ")
    for i in dictionary.keys():
        print(i)
        if i==bank:
            deposit=int(input("how much money do you want to deposit"))
            details[1]=details[1]+deposit
            #account details after depositing 
            print("------")
            print("your account details are: ")
            print(dictionary)
            print("------")
            print("thank you for depositing money!")

#code for withdrawing money            

choice_to_withdraw=input("do you want to withdraw money: ").capitalize()
if choice_to_withdraw == "Yes":
    bank=input("enter your name: ")
    coins=[5000,1000,500,100,50,10,5,2,1]
    for i in dictionary.keys():
        print(i)
        if i==bank:
            withdraw=int(input("how much money do you want to withdraw"))
            details[1]=details[1]-withdraw

#the amount of money you are going to get back is in form

            for k in coins:
                """this will tell that how user will get money after withdrawing """
                if withdraw >= k:
                    print(f"{k} : {withdraw//k}")
                    withdraw=withdraw%k

#account details after with drwaing money 

            print("------")
            print("your account details are: ")
            print(dictionary)
            print("------")
            print("thank you for withdrawing money!") 

#code for transferring money to another account 

choice_to_transfer=input("do you want to transfer money to another account: ").capitalize()
if choice_to_transfer=="Yes":
    your_name=input("enter your name:")
    to_which=input("enter name to which money is to transfer: ")
    money=input("enter amount of money: ")
    for i in dictionary.keys():
        if i==your_name:
            withdraw=int(input("how much money do you want to deposit"))
            details[1]=details[1]-withdraw
    for i in dictionary.keys():
        if i==to_which:
            deposit=int(input("how much money do you want to deposit"))
            details[1]=details[1]+deposit 

#details of both accounts after transferring money

    print("------")
    print("your account details are: ")
    print(dictionary)
    print("------")
    print("thank you for depositing money!")





        


