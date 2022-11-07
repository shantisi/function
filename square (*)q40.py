# Q40. Write a function For example, if we give 9119 the function should return 811181, as the square of 9
# is 81 and square of 1 is 1.

def num(a):
    i=0
    c=[]
    while i<len(a):
        b=a[i]*a[i]
        print(b,end="")
        i=i+1
num([9,1,1,9])
