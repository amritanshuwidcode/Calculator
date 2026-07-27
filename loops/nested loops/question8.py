
# print("Astrologer's Stars")
# print("Enter the number of rows")
# n=int(input())
# print("Enter the 1 or 0 to print desired pattern ")
# b=bool(int(input()))
# if(b== True):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("* ", end="")

#         print()
# else:
#     for i in range(n,0,-1):
#          for j in range(0, i ):
#            print("* ", end="")

#          print()


print("Draw a star pattern for right angle triangle")
num = int(input("Enter number of rows: "))
print("Enter boolean operator 0 or 1")
a = int(input())
b = bool(a)
if b==1:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif b==0:
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()