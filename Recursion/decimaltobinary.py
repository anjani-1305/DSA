def dec(n):
    if n==0:
        return 0
    else:
        return n%2 + 10*dec(n//2)
print(dec(13)) # 1101