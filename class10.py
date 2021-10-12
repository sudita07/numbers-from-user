# x=input("enter your first number")
# y=input("enter your second number")
# z=x+y
# print(z)
# .......................
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=x+y
# print(z)
# .....................................
# ch=input("enter a character")[4]
# print(ch)
# r=eval(input("enter an expression"))
# print(r)

rows =1
for row in range(rows,-5,-1):
    for col in range(-5,row-1):
        print(col,end = '')
    print()
