def sum(n):
    assert n>=0 and int(n) == n , "Enter a positive number"
    if n == 0:
        return 0
    else:
        s = int(n%10) + sum(int(n//10))
    return s
print(sum(1234)) # 10