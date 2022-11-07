# Apko min function ka use karke di huye list me se sabse choti value print karwao.

def min(n):
    i=0
    min=n[0]
    while i<len(n):
        if n[i]<min:
            min=n[i]
        i=i+1
    print("min number=",min)
min([7,8,6,5,11,4,2,3,1])
