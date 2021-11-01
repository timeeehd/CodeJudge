import sys

info = sys.stdin.readline().split(' ')
integers = int(info[0])
k = int(info[1])

numbers = []
for i in range(integers):
    entry = sys.stdin.readline()
    numbers.append(int(entry, 16))

for x in numbers:
    if (x & (1 << k)) != 0:
        print('1')
    else:
        print('0')

# for x in numbers:
#     print((x >> k) & 1)

# Suggested solution: not working?
# n, k = map(int, sys.stdin.readline().strip().split(' '))
# nums = list(map(lambda i: int(i,16) & 0xffffffff, sys.stdin.readlines()))
# assert len(nums) == n
# for x in nums:
#     print((x >> k) & 1)