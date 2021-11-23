number=int(input("enter number:-"))
sum=0
num=number
while number>0:
    digit=number%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    number=number//10
if sum==number:
    print(number,"Strong number")
else:
    print(number,"Not strong number")
