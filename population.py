import sys
n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    entry = sys.stdin.readline()
    numbers.append(int(entry, 16))

for x in numbers:
    count = 0
    for i in range(0,65):
        if (x & (1 << i)) != 0:
            count += 1
    print(count)


#Suggested Solution
    # n = int(sys.stdin.readline())
    # for i in range(n):
    #     x = int(sys.stdin.readline(),16) & 0xffffffffffffffff
    #     pc = 0
    #     while x != 0:
    #         pc += x & 1
    #         x >>= 1
    #     print(pc)