i=int(input("Enter any number:-"))
temp=i
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem
    temp=int(temp//10)
if i%sum==0:
    print(i,"Harshad Number")
else:
    print(i,"Not Harshad")