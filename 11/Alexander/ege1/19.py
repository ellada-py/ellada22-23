def f(s, c, m):
    if s >= 300:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)
for s in range(1, 300):
    for m in range(1, 2):
        if f(s, 0, m) == 1:
            print(s, m)
            break