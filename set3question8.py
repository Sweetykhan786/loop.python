i=1
while i<6:
    number=int(input("enter number:"))
    if number<5:
        print("number enter is smaller")
    elif number==5:
        print("wow you guess the correct number")
    else:
        print("number entered is greater")
        break
    i=i+1
    print(i)
    

