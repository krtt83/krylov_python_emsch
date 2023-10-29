a, b, c, d = map(int, input().split(','))
if a < 1 or a > 8:
    print('Wrong input')
elif b < 1 or b > 8:
    print('Wrong input')
elif c < 1 or c > 8:
    print('Wrong input')
elif d < 1 or d > 8:
    print('Wrong input')
elif a == c and b == d:
    print('NO')
elif (a + b) % 2 == 0 and (c + d) % 2 == 0:
    print('YES')
elif (a + b) % 2 != 0 and (c + d) % 2 != 0:
    print('YES')
else:
    print('NO')
