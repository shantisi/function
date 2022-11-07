# Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using
# function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

def text(list):
    i=0
    poss=0
    neg=0
    while i<len(list):
        if list[i]>0:
            poss=poss+1
        else: 
            neg=neg+1
        i=i+1
    print("possitive",poss)
    print("negetive",neg)
text([2, -7, 5, -64, -14])
            