# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

def function(list):
    i=0
    max=0
    min=len(list[i])
    a=list[i]
    while i<len(list):
        if len(list[i])>max:
            max=len(list[i])
            n=list[i]
        elif len(list[i])<min:
            min=len(list[i])
            min=list[i]
        i=i+1
    print("max",max,n)
    print("min",min,a)
function([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])