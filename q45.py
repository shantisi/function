# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from
#  the user and update
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1
# Sample Input:
# 23
# 42
# 41
# 1
# Sample Output:
# -23b[]


n=int(input("enter the no:"))
i=0
d=[]
e=[]
while i<n:
    b=int(input("enter the no:"))
    if b%2==0:
        a=(b*100)
        d.append(a)
    else:
        c=(b*-1)
        e.append(c)
    i=i+1
i=0
while i<len(d):
    print(d[i])
    i=i+1
i=0
while i<len(e):
    print(e[i])
    i=i+1
