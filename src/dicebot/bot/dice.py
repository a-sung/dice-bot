import random

def roll(n=1, m=100, op='+', r=0):
    val = n * random.randint(1, m)
    if op == '+':
        return val + r
    else:
        return val - r