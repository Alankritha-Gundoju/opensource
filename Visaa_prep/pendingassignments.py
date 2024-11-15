X, Y, Z = map(int, input().split())
total = X * Y
available = Z * 1440
if total <= available:
    print("YES")
else:
    print("NO")
