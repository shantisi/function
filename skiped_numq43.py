# Q43. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’].
#  Print the last ‘N’ elements of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q
# Sample Input:
# 3
# Sample Output:
# 5
# b
# q


def num(n):
    a=int(input("enter num"))
    i=a
    b=[]
    while i>=1:
        c=n[-i]
        b.append(c)
        i=i-1
    print(b)
num(["a",1,"2",5,"b","q"])

    

                                                    
                                                    


