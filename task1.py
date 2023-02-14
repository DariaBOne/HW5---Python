def degree(a,b):
    if b==0:
        return 1
    return a*a**(b-1)
A = int(input("введите основание: "))
B = int(input("введите степень: "))
print(degree(A,B))

