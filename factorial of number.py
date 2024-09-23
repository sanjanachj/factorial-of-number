# python program for calculating factorial of number.  
num=int(input("enter a number to find factorial="))
product=1
for i in range(1,num+1):
    product=product*i
print("the factorial of",num,"is",product)