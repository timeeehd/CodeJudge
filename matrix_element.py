import sys

info = sys.stdin.readline().split(' ')
n = int(info[0])
m = int(info[1])
major = info[2].strip()

array = sys.stdin.readline().split(' ')

for line in sys.stdin.readlines():
    elements = line.split(' ')
    if major == 'C':
        element = int(elements[0])*m + int(elements[1])
        print(array[element])
    else:
        print(array[int(elements[1])*n + int(elements[0])])


# Suggested solution
#!/usr/bin/env python3
#
# import sys
#
# if __name__ == '__main__':
#     n, m, order = sys.stdin.readline().strip().split()
#     n = int(n)
#     m = int(m)
#
#     A = list()
#     for i in range(n):
#         A.append([0]*m)
#
#     array = sys.stdin.readline().split()
#     assert len(array) == n*m
#     assert order in ['C','F']
#
#     k = 0
#     for elem in array:
#         a = int(elem)
#         if order == 'C':
#             A[k//m][k%m] = a
#         elif order == 'F':
#             A[k%n][k//n] = a
#         k += 1
#
#     for line in sys.stdin:
#         i,j = map(int,line.split())
#         print(A[i][j])

