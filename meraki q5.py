# Apko sum function ka use karke di hue list ke elements ka sum print karwana hai.
def sum(n):
    i=0
    sum=0
    while i<len(n):
        sum=sum+n[i]
        i=i+1
    print("sum number =",sum)
sum([1,2,3,4,5,6])


