# Q31. Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50.


n=int(input("enter the no"))
i=1
while i<=n:
    j=1
    while j<=10:
        print(i*j)
        j=j+1
    i=i+1

def num():
    a=int(input("enter the number"))
    i=1
    while i<=10:
        print(a,"*",i,"=",a*i)
        i=i+1
num()