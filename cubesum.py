i=int(input("Enter number:-"))
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("Sum of cube=",sum)