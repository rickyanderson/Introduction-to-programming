class Toll():   #class Toll
    car = 6000
    bus = 8000
    truck = 10000
    def __init__(self,car, bus, truck): #initiate car, bus and truck
        self.a = car    #car is part of the class
        self.b = bus    #bus is part of the class
        self.c = truck  #truck is part of the class

x = Toll    #
restart = 'Y'
choice = 1
while restart != ('N'): #while restart is not N, it loops
    print("1. Car (RP.6000)")
    print("2. Bus (RP.8000)")
    print("3. Truck (RP.10000)")
    choice = input("Vehicle :")
    if choice == '1':   #if choice is 1
        print("Fee: RP.",x.car) #prints the price of the car
        menu = input("Is there any other vehicle (Y/N)?\n")
        if menu == 'N': #if menu is N, the program stops
            print("<Exit the program>")
            break
    elif choice == '2':
        print("Fee: RP.",x.bus) #prints out the price of the bus
        menu = input("Is there any other vehicle (Y/N)?\n")
        if menu == ('N'):   #if menu is N, the program stops
            print("<Exit the program>")
            break
    elif choice == '3':
        print("Fee: RP.",x.truck)   #prints the price of the truck
        menu = input("Is there any other vehicle (Y/N)?\n")
        if menu == ('N'):   #if menu is N, The program stops
            print("<Exit the program>")
            break
    else:
        print("Error")
        break
