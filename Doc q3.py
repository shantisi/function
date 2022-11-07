# Q3.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20

def num(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    print(sum)
num([1,2,3,4,5,6])