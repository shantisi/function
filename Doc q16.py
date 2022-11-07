# Q16.Print multiplication table of 12 using function.

def num ():
    a=int(input("enter no"))
    i=0
    while i<=10:
        print(a,"*",i,"=",a*i)
        i=i+1
num()

n=int(input("enter no"))
i=1
while i<=n:
    j=1
    while j<=10:
        print(j*i,end=" ")
        j=j+1
    print()    
    i=i+1
    


    
