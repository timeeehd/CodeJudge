import sys
import time

n = 0
k = 0
dimensions = sys.stdin.readline().split(' ')
n = int(dimensions[0])
k = int(dimensions[1])

vs = []
for i in range(k):
    vs.append([int(entry) for entry in sys.stdin.readline().split(' ')])
empty_line = sys.stdin.readline().split(' ')
ws = []
for i in range(k):
    ws.append([int(entry) for entry in sys.stdin.readline().split(' ')])


def inner(vector, wector):
    for v in vector:
        for w in wector:
            value = sum(v[i] * w[i] for i in range(n))
            if value == 0:
                return 'yes'
    return 'no'


start = time.time()
print(inner(vs, ws))
print(time.time() - start)
