num=int(input("enter number(1-6)"))
if num==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("sum=",c)
elif num==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference=",c)
elif num==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("product=",c)
elif num==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("division=",c)
elif num==5:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a%b
    print("Percentage=",c)
elif num==6:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a//b
    print("Floor Division=",c)
else:
    print("Invalid Number")

