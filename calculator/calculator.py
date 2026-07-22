ope=input("enter the operation")
a=int(input("enter first number"))
b=int(input("enter the second number"))

if ope=="*" and a==56 and b==3:
    print(555)
elif ope=="+" and a==56 and b==9:
    print(77)
elif ope=="/" and a==56 and b==6:
    print(4)

elif ope=="*":
    print(a,"*",b,"=",a*b)
elif ope=="+":
    print(a,"+",b,"=",a+b)
elif ope=="-":
    print(a,"-",b,"=",a-b)
elif ope=="/":
    print(a,"/",b,"=",a/b)
else:
    print("abe chutiye operations matlab +-*/")
