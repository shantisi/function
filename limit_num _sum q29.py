# Q29. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit
# (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18,


def num(a):
    i=1
    sum=0
    while i<=a:
        if i%3==0 or i%5==0:
            sum=sum+i
            print(sum)
        i=i+1
num(20)

