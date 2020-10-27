import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    
    
    def createAccount(self):
        self.name = input("Input Fullname : ")
        self.accNo= int(input("Please input a pin of your choice :"))
        self.deposit = int(input("Please input a value to deposit to start an account :"))
        print("\n\n\nAccount Created")
    
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        print('\n''Accout Number||','Customer Name','|| Account Balance')
        print('=================================================')
        for item in mylist :
            print(item.accNo,"           ", item.name, "        ",item.deposit )
        infile.close()
    else :
        print("No records to display")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0

while ch != 5:
    
    print('=================================================''\n'
   '           ----Welcome to Times Bank----            ''\n'
      '*************************************************''\n')
    print(
      '=<< 1. Open a new account                     >>=''\n'
      '=<< 2. Withdraw Money                         >>=''\n'
      '=<< 3. Deposit Money                          >>=''\n'
      '=<< 4. Check Customers &  Balance             >>=''\n'
      '=<< 5. Exit/Quit                              >>=''\n'
      '*************************************************''\n')
    print('Select your choice number from the above menu :')   
    ch = input()
    print('Choice number',ch,'is selected by the customer')
    
    # call
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '4':
        displayAll()
    elif ch == '5':
        print("\tThanks for using banking system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    
    
    
    
    
    
    
    
    
    
