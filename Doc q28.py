# Q28. Write a function called showNumbers that takes a parameter called limit. It should print
# all the numbers between 0 and limit with a label to identify the even and odd numbers. For
# example, if the limit is 3, it should print: - 0 even,1 odd, 2 even, 3 odd .

def even(list):
    i=0
    b=[]
    d=[]
    c=0
    c1=0
    while i<len(list):
        if list[i]%2==0:
            b.append(list[i])
            c=c+1
        else:
            d.append(list[i])
            c1=c1+1
        i=i+1
    print(b,"even",c)
    print(d,"odd",c1)
even([22,3,4,5,6,7,8,9,10,12])