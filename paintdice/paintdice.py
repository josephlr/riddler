#!/usr/bin/env python3

import random

N = 1_000_000

def avg(n):
    s = sum((run(n) for _ in range(N)))
    return s / N

def run(n):
    v = list(range(n))
    count = 0
    while not all_same(v):
        v = rand_select(v)
        count += 1
    return count

def rand_select(v):
    return [random.choice(v) for _ in v]

def all_same(v):
    fst = v[0]
    return all(map(lambda x: x == fst, v[1:]))

print(avg(6))