# Q15.Write a function to calculate power of a number raised to other ( ab )

def num(list):
    i=1
    b=[]
    c=0
    while i<len(list):
        d=i**2
        b.append(d)
        c=c+1
        i=i+1
    print(b)
    print("count=",c)
num([1,2,3,4,5,6,7,8,9])

n="priya"
i=0
b=[]
s=5
while i<len(n):
    b.append(n[i])
    b.append(s)
    s=s+5
    i=i+1
print(b)
