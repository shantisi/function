# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).


def square():
    i=1
    b=[]
    c=[]
    e=[]
    while i<=30:
        if i<=5:
            d=i**2
            b.append(d) 
        if i>=25 and i<=30:
            d=i**2
            c.append(d)   
        i=i+1
    e.append(b)
    e.append(c)
    f=tuple(e)
    print(f)
square()
