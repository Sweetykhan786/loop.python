user=5
k=1
i=1
while i<=user:
    b=1
    while b<=user-i:
        print(' ',end="  ")
        b=b+1
    j=1
    while j<=k:
        print("*",end="  ")
        j=j+1
    k=k+2
    print()
    i=i+1

# user=int(input("enter number:"))
# k=1
# i=1
# while user>=5:
#     b=1
#     while b<5-i:
#         print('',end=" ")
#         b=b+1
#     j=1
#     while user>k:
#         print(k,end=" ")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1
