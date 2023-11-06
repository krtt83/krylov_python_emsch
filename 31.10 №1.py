n = int(input())
s = 0
s2 = 0
for i in range(n):
    a = int(input())
    s += a
    s2 += (1 / a)
g = n / (s2)
f = round(g, 3)
print(s / n, f)
