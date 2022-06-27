import random

def roll(n=1, m=100, r=0, op='+'):
    val = n * random.randint(1, m)
    if op == '+':
        return val + r
    else:
        return val - r