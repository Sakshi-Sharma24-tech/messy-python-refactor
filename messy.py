# original messy code from colab before refactoring
import sys, os, math

def f(s):
    t = 0
    for i in range(1, len(s)+1):
        t = t + s[i-1]
    a = t / len(s)
    return a

st = [85, 90, 78, 92, 88, 76, 95, 89]
print("Avg is " + str(f(st)))

t2 = 0
for x in st:
    t2 += x
avg2 = t2 / len(st)

c = 0
for m in st:
    if m >= 80:
        c = c + 1
print("Count: " + str(c))
