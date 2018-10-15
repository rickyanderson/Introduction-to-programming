class Single:   #class Single
    def __init__(self,single):  #initiate the single
        self.single = single
    def getsingle(self):        #function to get self.single
        return self.single
class Double:    #class Double
    def __init__(self,double):  #initiate the double
        self.double = double
    def getdouble(self):
        return self.double      #function to get self.double
class Hotel(Single,Double):
    def __init__(self,room):
        super().__init__(room)
    def singleprice(self):      #price for singlebed
        self.single = 100
        return self.single
    def doubleprice(self):      #price for doublebed
        self.double = 200
        return self.double

def view():     #function view to print this thing
    print("1. Single room\n2. Double room")
restart = 'Y'
def operator():
    single = 0      #single integer starts at 0
    double = 0      #double integer starts at 0
    checkintimessingle = 0      #number of checks in for single
    checkintimesdouble = 0      #number of checks in for double
    while restart != 'N':
        todo=input("Check in/ check out(in/out)")
        if todo == 'in':
            view()
            menu = input("What room :")
            x = Hotel(menu)
            if menu == 'single':
                if single == 0:
                    single+=1                   #adds 1 to the integer of single
                    checkintimessingle += 1     #adds 1 check in, everytime you check in
                    print("The room is yours")
                    if single ==1:
                        print("Room is occupied")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)        #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
                else:
                    print("No more room")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)        #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
            elif menu =='double':
                if double == 0:
                    double += 1
                    checkintimesdouble += 1
                    print("The room is yours")
                    if double == 1:
                        print("Room is occupied")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)       #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
                else:
                    print("Room is full")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)        #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
            else:
                print("Invalid")
                print("Try again")
        if todo == 'out':
            view()
            menu = input("What room :")
            x = Hotel(menu)
            if menu == 'single':
                if single == 1:
                    single -=1              #minus 1 the integer for single
                    print("Room is now available")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)    #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
                else:
                    print("Room is empty")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)    #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
            elif menu =='double':
                if double == 1:
                    double -=1              #minus 1 the integer for double
                    print("Room is now available")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)    #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
                else:
                    print("Room is empty")
                    next = input("Y to continue, N to quit")
                    if next == 'N':
                        totalfee = (x.singleprice()*checkintimessingle)+(x.doubleprice()*checkintimesdouble)    #calculate the totalfee
                        print("Total Revenue :$",totalfee)
                        print("Good bye")
                        break
            else:
                print("Invalid")
                print("Try again")
operator()

