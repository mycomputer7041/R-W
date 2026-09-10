def factoriyal(n):
    if n==1:
        return 1
    return n * factoriyal(n - 1)

n=5
print(factoriyal(n))