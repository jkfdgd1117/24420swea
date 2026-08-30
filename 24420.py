T = int(input())
for _ in range(T):
    Asize, Bsize = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    if A == B:
        print('=')
    elif A.issubset(B):
        print('<')
    elif B.issubset(A):
        print('>')
    else:
        print('?')