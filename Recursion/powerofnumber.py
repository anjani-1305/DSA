def power(n,m):
    if m==0:
        return 1
    return n*power(n,m-1)
print(power(2,3))