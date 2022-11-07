# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]

def sum(a):
    i=0
    s=[]
    while i<len(a):
        n=a[i]%10
        f=a[i]//10
        k=n+f
        s.append(k)
        i=i+1
    print(s)
sum([12,67,98,34])

