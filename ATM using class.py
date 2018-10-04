restart = ('Yes')
class Account():                                                                                                  #class account
    def __init__(self,balance):                                                                                   #use class so we can type in balance
        self.balance = balance

    def get_balance(self):                                                                                        #function to get balance
        return self.balance
    def inwithdraw(self,money):                                                                                   #function to do withdraw
        self.balance -= money                                                                                     #decrease amount from balance
        return print(self.balance)
    def deposit(self,money):                                                                                      #function to deposit money
        self.balance += money                                                                                     #adds amount to balance
        return print(self.balance)

x = Account(1000)                                                                                                 #make an object, the balance is 1000
chances = 3                                                                                                      #variable chances = 3
while chances>=0:                                                                                                 #if chances is above 0
    pin = int(input("Enter your PIN : "))                                                                         #input the pin
    if pin == 123:                                                                                              #if the pin is 12345, do while loop
        while restart != ('No'):                                                                                  #while restart is not No
            if restart != ('No'):                                                                                 #print the following
                print("1. Check your balance")
                print("2. Withdraw")
                print("3. Deposit\n")
                menu = int(input("What do you want to do? : "))                                                 #input what do you want to do
            if menu == 1:                                                                                         #if the input is 1, get the balance (1000)
                print(x.get_balance())
                restart = input("Press Yes to do another transaction, No to quit : ")                           #type Yes to do another transaction, No to quit
                if restart == ('No'):
                    print("Thank you")
                    break
            elif menu == 2:                                                                                       #if input is 2, withdraw
                withdraw = int(input("Withdraw :"))                                                               #withdraw the amount you want, must be integer
                if withdraw > (x.get_balance()):                                                                  #if the balance is lower than the withdraw, print not enough money
                    print("Not enough money")                                                                     #prints Not enough money
                else:
                    x.inwithdraw(withdraw)
                    print(">>>",withdraw, "was taken")                                                                 #if it have enough money, print the new value
                 
                    restart = input("Press Yes to do another transaction, No to quit : ")
                    if restart == ("No"):
                        print("Thank you")
                        break
            elif menu == 3:
                deposit = int(input("Deposit :"))                                                                 #deposit the amount you want
                x.deposit(deposit)                                                                           #prints the new value
                print(">>>",deposit, "was added")
                restart = input("Press Yes to do another transaction, No to quit : ")
                if restart == ('No'):
                        print("Thank you")
                        break
            else:                                                                                                 #if your input not in the choices, prints error
                print("Error")
                break

    if pin != 123:                                                                                              #if pin is not 12345
        print("Incorrect PIN")                                                                                    #print incorrect PIN
        print("Closing...")
    break

                                                                    #CORRECT PIN IS 12345
