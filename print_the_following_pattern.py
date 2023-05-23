n=int(input())
for i in range(n):
    for j in range(i):
        print('x',end='')
    for j in range(1):
        print('0',end='')
    for j in range(i,n-1):
        print('x',end='')
    print()
        