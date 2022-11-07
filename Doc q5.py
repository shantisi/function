# Q5.Write a Python function that takes a list and returns a new list with unique elements of the
# first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def unique(list):
    i=0
    b=[]
    while i<len(list):
        if list [i] not in b:
            b.append(list[i])
        i=i+1
    print(b)
unique([1,2,3,3,3,3,4,5])
    