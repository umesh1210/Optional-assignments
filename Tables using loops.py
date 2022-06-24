# Creating a table using loops.

number=int(input("enter a number:"))
for i in range(0,11):
    result=number*i
    if number>=0:
        print(number,"*",i,"=",result)