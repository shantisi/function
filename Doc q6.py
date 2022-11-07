# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].


def even(list):
    i=0
    b=[]
    while i<len(list):
        if list[i]%2==0:
            b.append(list[i])
        i=i+1
    print("even",b)
even([1,2,3,4,5,6,7,8,9])