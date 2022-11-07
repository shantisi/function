# Q39. Your task is to make two functions, max and min (maximum and minimum in PHP and
# Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs,
# respectively, the largest and lowest number in that array/vector.
# #Examples:-
# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.

def fun(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    print("max",max)
fun([4,6,2,1,9,63,-134,566]) 

def fun(list1):
    i=0
    min=list1[0]
    while i<len(list1):
        if list1[i]<min:
            min=list1[i]
        i=i+1
    print("min",min)
fun([-52, 56, 30, 29, -54, 0, -110])




