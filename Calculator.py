#program to build a calculator
def add(a,b) :
     return a+b
def sub(a,b) :
     return a-b
def mul(a,b) :
     return a*b
def div(a,b) :
     return a/b
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
n = int(input("Enter 1 for addition , 2 for subtraction , 3 for multiplication and 4 for division : "))
if n==1 :
    print ("Addition of given numbers :",add(a,b))
elif n==2 :
     print ("Subtraction of given numbers :",sub(a,b))
elif n==3 :
     print ("Multiplication of given numbers :",mul(a,b))
elif n==4 :
      print ("Division of given numbers :",div(a,b))
else :
     print ("Wrong Input!!")