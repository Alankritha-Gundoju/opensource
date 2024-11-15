N, X, Y = map(int, input().strip().split())
total = N*X
if Y <= total and Y % X == 0:
    print("YES")
else:
    print("NO")
