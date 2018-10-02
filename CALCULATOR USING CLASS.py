class calculator():
    def __init__ (self,num1,num2):
        self.n1=num1
        self.n2=num2
    def add(self):
        return self.n1+self.n2

    def minus(self):
        return self.n1-self.n2

    def multiply(self):
        return self.n1*self.n2

    def divide(self):
        return self.n1/self.n2
num1 =int(input("Enter number 1:"))
num2 =int(input("Enter number 2:"))
calcu = calculator(num1,num2)
choice=1
while choice !=0:
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = int(input("Enter Choice: "))
    if choice == 0:
        print("Exiting")
    elif choice == 1:
        print(calcu.add())
    elif choice == 2:
        print(calcu.minus())
    elif choice == 3:
        print(calcu.multiply())
    elif choice == 4:
        print(calcu.divide())
    else:
        print("ERROR!!")
print()
