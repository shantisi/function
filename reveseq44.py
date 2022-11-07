# Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]
# Sample Input:
# 2
# Sample Output:
# q
# b
# Sample Input:
# 3
# Sample Output:
# q
# b
# 5


def reverse(n):
    a=int(input("enter num"))
    i=1
    b=[]
    while i<=(a):
        b.append(n[-i])
        i=i+1
    print(b)
reverse(["a",1,"2",5,"b","q"])