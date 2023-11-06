a, b = map(int, input().split())
for c in range(b, a + 1, -1):
    if a > b:
        print(c, end=',')
for i in range(a, b + 1):
    if a < b:
        print(i, end=',')
