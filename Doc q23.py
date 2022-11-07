# Q23.What is the output of the following code snippet?
# def test(x = 1, y = 2):
# x = x + y
# y += 1
# print(x, y)
# test()
# A. 1 3
# B. 3 1
# C. The program has a runtime error because x and y are not defined.
# D. 1 1
# E. 3 3
# Answer :- E


def test(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y,end=" ")
test() 

