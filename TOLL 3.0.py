class Car:  #class car
    def __init__(self,car): #initiate the class
        self.c = car

    def getcar (self):#make a function called getcar
        return self.c   #return to self.car

class Bus:  #class Bus
    def __init__(self,bus): #initiate the class
        self.bus = bus

    def getbus(self):   #make a function called getbus
        return self.bus #return to self.bus

class Truck:    #class Truck
    def __init__(self,truck):   #initiate the class
        self.truck = truck

    def gettruck(self): #make a function called gettruck
        return self.truck   #return to self.truck

def view(): #view function to print the layout
    print("--- Welcome to ver.2 Toll ---")
    print("=============================")
    print("Category of vehicle\n","1. Car (RP 6000)\n","2. Bus (RP 8000)\n","3. Truck (RP 10000)")
    print("=============================")
def view2():
    print("--- Welcome to ver.2 Toll ---")
    print("=============================")
    print("Category of vehicle\n","1. Car (RP 18000)\n","2. Bus (RP 20000)\n","3. Truck (RP 25000)")
    print("=============================")

class Toll2(Car, Bus,Truck):
    def carPrice2(self):
        Car.getcar = 18000
        return Car.getcar
    def busPrice2(self):
        Bus.getbus = 20000
        return Bus.getbus
    def truckPrice2(self):
        Truck.gettruck = 25000
        return Truck.gettruck

class Toll(Car, Bus, Truck):    #class Toll
    def __init__(self,type):    #initiate type
       super().__init__(type)   #make a super class


    def carPrice(self): #make a function called carprice to declare car.getcar is 6000
        Car.getcar = 6000
        return Car.getcar
    def busPrice(self):#make a function called busprice to declare bus.getbus is 8000
        Bus.getbus = 8000
        return Bus.getbus
    def truckPrice(self):   #make a function called truckprice to declare truck.gettruck is 10000
        Truck.gettruck = 10000
        return Truck.gettruck

restart = 'Y'

def toll_op():  #function toll operation
    listcar = 0
    listbus = 0
    listtruck = 0
    listcar2 = 0
    listbus2= 0
    listtruck2 = 0

    while restart != 'N':   #while loop, loops if restart is not 'N'
        print("==Toll Locations==>> Sunter / Bekasi <<==")
        location = input("Location : ").lower()
        if location == "sunter":
            view()
            menu = input("Vehicle :").lower() #input the vehicle and lowers the characters to not confuse the program
            TC = Toll(menu)
            if menu == 'car':
                print("")
                print("Fee : RP {}".format(TC.carPrice()))  #print the carprice
                print("")
                listcar += 1
                next = input("Is there any other vehicle? (Y/N)").upper()

                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))    #the total revenue of all the vehicle
                    print("Toll Sunter")
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints out the number of car, bus and truck
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))    #the total revenue of all the vehicle
                    print("Toll Bekasi")
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints out the number of car, bus and truck
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
            elif menu == 'bus':
                print("")
                print("Fee : RP {}".format(TC.busPrice()))  #prints the busprice
                print("")
                listbus += 1
                next = input("Is there any other vehicle? (Y/N)").upper()   #input Y/N, upper makes the character in caps to avoid confusion

                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))
                    print("Toll Sunter")
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints the number of cars, bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))    #the total revenue of all the vehicle
                    print("Toll Bekasi")
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints out the number of car, bus and truck
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
            elif menu == 'truck':
                print("")
                print("Fee : RP {}".format(TC.truckPrice()))
                print("")
                listtruck += 1
                next = input("Is there any other vehicle? (Y/N)").upper()

                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints the number of cars,bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)   #prints out the total revenue of all the vehicles
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))    #the total revenue of all the vehicle
                    print("Toll Bekasi")
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints out the number of car, bus and truck
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
                else:
                    print("Error")
                    break

        elif location == "bekasi":
            view2()  #calls the function view
            menu = input("Vehicle :").lower() #input the vehicle and lowers the characters to not confuse the program
            TC2 = Toll2(menu)
            if menu == 'car':
                print("")
                print("Fee : RP {}".format(TC2.carPrice2()))  #print the carprice
                print("")
                listcar2 += 1
                next = input("Is there any other vehicle? (Y/N)").upper()
                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints the number of cars,bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)   #prints out the total revenue of all the vehicles
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))    #the total revenue of all the vehicle
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints out the number of car, bus and truck
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
            elif menu == 'bus':
                print("")
                print("Fee : RP {}".format(TC2.busPrice2()))  #prints the busprice
                print("")
                listbus2 += 1
                next = input("Is there any other vehicle? (Y/N)").upper()   #input Y/N, upper makes the character in caps to avoid confusion

                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints the number of cars,bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)   #prints out the total revenue of all the vehicles
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints the number of cars, bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
            elif menu == 'truck':
                print("")
                print("Fee : RP {}".format(TC2.truckPrice2()))
                print("")
                listtruck2 += 1
                next = input("Is there any other vehicle? (Y/N)").upper()

                if next == 'N':
                    totalfee = ((TC.carPrice()) * (listcar) + (TC.busPrice()) * (listbus) + (TC.truckPrice()) * (listtruck))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar,"           ",listbus,"           ",listtruck,"             ")    #prints the number of cars,bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee)   #prints out the total revenue of all the vehicles
                    totalfee2 = ((TC2.carPrice2()) * (listcar2) + (TC2.busPrice2()) * (listbus2) + (TC2.truckPrice2()) * (listtruck2))
                    print("===============================")
                    print("Car","        ","Bus","        ","Truck")
                    print("-------------------------------")
                    print(listcar2,"           ",listbus2,"           ",listtruck2,"             ")    #prints the number of cars,bus and trucks
                    print("===============================")
                    print("Total Revenue : RP.",totalfee2)   #prints out the total revenue of all the vehicles
                    print("Have a nice day")
                    totalrev = totalfee + totalfee2
                    print("Total Revenue of both Toll : RP.",totalrev)
                    break
                else:
                    print("Error")
        else:
            print("error")
toll_op()


