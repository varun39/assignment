# q-1 Calculate Area of a Sphere
import math
def area(radius):
    sa=4*math.pi*radius*radius
    print("The surface area of sphere =%.2f"%sa)
radius=float(input("Enter radius : "))
area(radius)
# q-2 Prints All the Perfect Numbers Between 1 and 1000
def perfect(num):
    s=0
    for i in range(1,int(num/2)+1):
        if(num%i==0):
            s=s+i
    if(s==num):
        print(num)
a=1000
for j in range(1,a):
    perfect(j)
# q-3 Print Multiplication Table of a User Defined Number
def table(n):
    for i in range(1,11):
        b=n*i
        print(b)
m=int(input("Enter which multiplication table you want - "))
table(m)            
# q-4 Calculate Power of a Number Using Recursion
def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return(base*power(base,exp-1))
base=int(input("Enter base = "))
exp=int(input("Enter exponental = "))
print(power(base,exp))
