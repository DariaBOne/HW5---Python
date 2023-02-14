def summ(a,b):
    if (a==1 and b==0) or (a==0 and b==1):
        return 1
    return 1+(a-1)+1+(b-1)
A = int(input("введите число: "))
B = int(input("введите второе число: "))
print(summ(A,B))