class calculator():                             #class calculator
    def __init__ (self,num1,num2):              #initiate class
        self.n1=num1                            #self.n1 is num1
        self.n2=num2                            #self.n2 is num2
    def add(self):                              #function for adding
        return self.n1+self.n2

    def minus(self):                            #function for subtracting
        return self.n1-self.n2

    def multiply(self):                         #function for multiplying
        return self.n1*self.n2

    def divide(self):                           #function for dividing
        return self.n1/self.n2
num1 =int(input("Enter number 1:"))             #input the first number
num2 =int(input("Enter number 2:"))             #input the second number
calcu = calculator(num1,num2)                   #variable calcu
choice=1                                        #choice is 1
while choice !=0:                               #while choice is not 0
    print("1.Addition")                         #print addition
    print("2.Subtract")                         #print substract
    print("3.Multiply")                         #print multiply
    print("4.Divide")                           #print divide
    choice = int(input("Enter Choice: "))       #pick the choice you want for the operators
    if choice == 0:                             #if the choice is 0, exit the calculator
        print("Exiting")
    elif choice == 1:                           #if the choice is 1, add the first number with the second number
        print(calcu.add())
    elif choice == 2:                           #if the choice is 2, subtract the first number with the second number
        print(calcu.minus())
    elif choice == 3:                           #if the choice is 3, multiply the first number with the second number
        print(calcu.multiply())
    elif choice == 4:                           #if the choice is 4, divide the first number with the second number
        print(calcu.divide())
    else:
        print("ERROR!!")                        #else is an Error
print()
