# Q2.Write a Python function to find the Max of three numbers.


def num(list):
    i=0
    max=0
    max1=0
    max2=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        elif list[i]>max1 and max1!=list[i]:
            max1=list[i]
        elif list[i]>max2 and max2!=list[i] and max!=list[i]:
            max2=list[i]
        i=i+1
    print("max number",max)
    print("max1 number",max1)
    print("max2 number",max2)
num([1,2,3,7,6,4])


