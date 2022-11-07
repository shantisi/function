# Q1.Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
# result= 2.

def num():
    list=["abc","xyz","aba","1221"]
    i=0
    c=0
    b=[]
    while i<len(list):
        d=(list[i][::-1])
        if list[i]==d:
            b.append(d)
            c=c+1
        i=i+1
    print("number=",b,c)
num()
