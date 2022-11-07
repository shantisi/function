# Q24.What is the output of the following code snippet?
# def test(x = 1, y = 2):
# x = x + y
# y += 1
# print(x, y)
# test(2, 1)
# A. 1 3
# B. 2 3
# C. The program has a runtime error because x and y are not defined.
# D. 3 2
# E. 3 3
# Answer :- D

def test(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)
test(2, 1)