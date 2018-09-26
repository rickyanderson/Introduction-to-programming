stars=int(input("Stars:"))  #Input the number you want

for a in range(0,stars):        #looping for a in range of 0 to stars
    for b in range(0,a+1):      #looping b from 0 to a+1
        print("*", end=" ")     #print the stars
    print()                  #left triangle
print()

for c in range(0,stars):        #looping for c in range of 0 to stars
    for d in range(0,stars-c):  #looping d from 0 to stars-c
        print(" ", end=" ")     #print spaces
    for e in range(0,c+1):      #looping for e in range of 0 to c+1
        print("*", end=" ")     #print the stars
    print()                  #right triangle
print()

for f in range(stars,0,-1):     #looping for f in range of stars to 0 in reverse
    for g in range(0,stars):    #looping for g in range of 0 to stars
        print(" ", end=" ")     #print spaces
    for h in range(f):          #looping for h in range of f
        print("*", end=" ")     #print the stars
    print()                 #reverse left triangle
print()

for i in range(stars,0,-1):     #looping for i in range of stars to 0 in reverse
    for j in range(stars-i):    #looping for j in range of stars-i
        print(" ", end=" ")     #print spaces
    for k in range(i):          #looping for k in range of i
        print("*", end=" ")     #print the stars
    print()                 #reverse right triangle
print()

for l in range(0,stars):        #looping for l in range of 0 to stars
    for m in range(0,stars-l):  #looping for m in range of 0 to stars-1
        print(" ", end=" ")     #print the spaces
    for n in range(0,l*2+1):    #looping for n in range of 0 to l*2+1
        print("*", end=" ")     #print the stars
    print()                 #pyramid shape
print()

for o in range(0,stars):        #looping for o in range of 0 to stars
    for p in range(0, stars-o): #looping for p in range of 0 to stars-o
        print(" ", end=" ")     #print the spaces
    for q in range(0,o*2+1):    #looping for q in range of 0 to 0*2+1
        print("*", end=" ")     #print the stars
    print()
for r in range(stars,-1,-1):    #looping for r in range of stars to -1 in reverse
    for s in range(0,stars-r):  #looping for s in range of 0 to stars-r
        print(" ", end=" ")     #print the spaces
    for t in range(0,r*2+1):    #looping for t in range of 0 to r*2+1
        print("*", end=" ")     #print the stars
    print()                 #diamond shape
