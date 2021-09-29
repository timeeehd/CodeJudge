# import sys
#
# args = []
#
# for idx,line in enumerate(sys.stdin):
#     args.append(line[:len(line) - 1])
#     if(idx == 2):
#         break
#
# size = args[0]
# v = args[1].split()
# w = args[2].split()
#
# value = 0
# for i in range(int(size)):
#     value += int(v[i])*int(w[i])
#
# print(value)
#

#TODO: their solution

# !/usr/bin/env python3
#
import sys

n = int(sys.stdin.readline())

v = [int(entry) for entry in sys.stdin.readline().split(' ')]
w = [int(entry) for entry in sys.stdin.readline().split(' ')]

assert(n==len(v) and n==len(w))

print(sum(v[i] * w[i] for i in range(n)))