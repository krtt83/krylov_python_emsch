a, b, c = map(int, input().split())
if a != b != c and a != c:
    print(0)
elif a == b == c:
    print(3)
else:
    print(2)
