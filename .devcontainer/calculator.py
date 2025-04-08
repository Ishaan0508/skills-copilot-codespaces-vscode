print("enter your name")
x=input()
print("hello "+x)
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("enter 4 for Division")
f=input()
print("Enter two numbers")
n1=int(input())
n2=int(input())
if f == "1":
    result=n1+n2
elif f == "2":
    result=n1-n2
elif f == "3":
     result=n1*n2
elif f == "4":
    result=n1/n2
else :
    print("invalid input")
print(result)
