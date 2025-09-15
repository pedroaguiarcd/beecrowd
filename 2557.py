import sys

for expr in sys.stdin.readlines():
    expr = expr.strip()
    left , j= expr.split('=')
    r , l = left.split('+')
    if j == "J":
        v = int(r) + int(l)
    elif r == 'R':
        v = int(j) - int(l)
    else:
        v = int(j) - int(r)
    print(v)


