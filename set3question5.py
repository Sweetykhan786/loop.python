i=1
sum=0
while (i<=11):
    num=int(input("enter number:"))
    sum=sum+num
    i=i+1
    average=float(sum)/11
print(sum)
print(average)
if average%5==0:
    print("divided by", 5)
else:
    print("not divided by",5)


