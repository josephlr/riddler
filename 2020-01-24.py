# Express: 13 players maximum

import sys

def win(x, y):
    if y < 0:
        raise ValueError
    if x == 0:
        return False
    if any(not win_memo(x - d, y) for d in range(1, x + 1)):
        return True
    if any(not win_memo(x, y - d) for d in range(1, y + 1)):
        return True
    m = min(x, y)
    if any(not win_memo(x - d, y - d) for d in range(1, m + 1)):
        return True
    return False

memo = {}
def win_memo(x, y):
    if x < y:
        return win_memo(y, x)
    if (x,y) not in memo:
        memo[(x,y)] = win(x, y)
    return memo[(x,y)]

def win_game(n):
    return any(not win_memo(d, n - d) for d in range(0, n + 1))

l = 101


# def x(n):
#     if n == 0:
#         return 1
#     for i in range(sys.maxsize):


print("1st player Win with the following numbers of staring coins:")
for n in range(l):
    if win_game(n):
        print(n)


# for x in range(m):
#     for y in range(m):
#         c = 'x'
#         if win_memo(x,y):
#             c = '*'
#         print(c + ' ', end='')
#     print()

# m = {0:1} # x -> y
# ys = {1} # y
# ds = {-1} # d = x - y

# def h(x):
#     if x in m:
#         return m[x]
#     for y in range(sys.maxsize):
#         d = x - y
#         if (y not in ys) and (d not in ds):
#             m[x] = y
#             ys.add(y)
#             ds.add(d)
#             return y

# for x in range(l):
#     print("h({}) = {}".format(x, h(x)))