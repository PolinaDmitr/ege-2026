#(1241651≠5*x+y)∧(413184≠x+2*y)∨(A>x)∨(A>y)

def f(x, y, a):
    return (1241651 != 5 * x + y) and (413184 != x + 2 * y) or (a > x) or (a > y)


for x in range(1, 413184 // 2 + 1):
    y1 = 1241651 - 5 * x
    y2 = (413184 - x) / 2
    if y1 == y2:
        print(x, y1)