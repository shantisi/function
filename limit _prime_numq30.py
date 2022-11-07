# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter.

def num(a):
    i=1
    while i<=a:
        if i%2!=0 and i%3!=0 and i%5!=0:
            print(i,"prime")
        elif i==2 or i==3 or i==5:
            print(i,"prime")   
        else:
            print(i,"not prime")
        i=i+1
a=44
b=8
print