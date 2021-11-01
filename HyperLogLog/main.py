import sys
import math
import matplotlib.pyplot as plt


def hashing(x):
    hash_info = [0x21ae4036,
                 0x32435171,
                 0xac3338cf,
                 0xea97b40c,
                 0x0e504b22,
                 0x9ff9a4ef,
                 0x111d014d,
                 0x934f3787,
                 0x6cd079bf,
                 0x69db5c31,
                 0xdf3c28ed,
                 0x40daf2ad,
                 0x82a5891c,
                 0x4659c7b0,
                 0x73dc0ca8,
                 0xdad3aca2,
                 0x00c74c7e,
                 0x9a2521e2,
                 0xf38eb6aa,
                 0x64711ab6,
                 0x5823150a,
                 0xd13a3a9a,
                 0x30a5aa04,
                 0x0fb9a1da,
                 0xef785119,
                 0xc9f0b067,
                 0x1e7dde42,
                 0xdda4a7b2,
                 0x1a1c2640,
                 0x297c0633,
                 0x744edb48,
                 0x19adce93]

    x = x & 0xffffffff

    solution = []

    for row in hash_info:
        sol = row & x
        pc = 0
        while sol != 0:
            pc += sol & 1
            sol >>= 1
        solution.append(pc % 2)

    solution.reverse()
    solution_string = ''.join(str(b) for b in solution)
    sol_hex = hex(int(solution_string, 2))
    return sol_hex[2:].zfill(8)


def rho(n):
    for i in range(1, 33):
        if ((n >> (32 - i)) & 1) == 1:
            return i
    return None


def setBitNumber(n):
    if (n == 0):
        return 0;

    msb = 0;
    n = int(n / 2);

    while (n > 0):
        n = int(n / 2)
        msb += 1

    return (1 << msb)


def f(x):
    return ((x * 0xbc164501) & 0x7fffffff) >> 21


if __name__ == '__main__':
    m = 1024
    alpha_m = 0.7213 / (1 + 1.079 / m)
    # Y = sys.stdin.readlines()
    # threshold = int(sys.stdin.readline())
    M = [0 for j in range(m)]
    distribution = [0 for j in range(32)]
    x_axis = [x + 1 for x in range(32)]
    for i in range(1, 10 ** 6 + 1):
        i = i & 0xffffffff
        x = hashing(i)
        bin = rho(int(x, 16))
        distribution[bin - 1] += 1
    distribution = [distribution[x]/(10**6) for x in range(32)]
    prob = [2**(-x) for x in range(1,33)]
    print('test')
    fig, ax = plt.subplots()
    ax.plot(x_axis, distribution, label='Our distribution')
    ax.plot(x_axis, prob, 'ro', label='expected distribution')
    plt.legend()
    plt.show()
    # for x in range(32):
    #     if distribution[x] != 0:
    #         distribution[x] = 1/distribution[x]

    #
    # for y in sys.stdin:
    #     y = int(y, 16)
    #     y = y & 0xffffffff
    #     j = f(y)
    #     x = hashing(y)
    #     M[j] = max(M[j], rho(int(x, 16)))
    # # for i in range(m):
    # #     print(M[i])
    # sum = 0
    # V = 0
    # for j in range(m):
    #     sum += math.pow(2, -M[j])
    #     if M[j] == 0:
    #         V += 1
    # n_estimate = (alpha_m * (m ** 2)) * (1 / sum)
    #
    # if (n_estimate <= 5 / 2 * m) & (V > 0):
    #     n_estimate = m * math.log(m / V)
    # elif n_estimate > 1 / 30 * math.pow(2, 32):
    #     n_estimate = -math.pow(2, 32) * math.log(1 - (n_estimate / math.pow(2, 32)))
    #
    # if n_estimate > threshold:
    #     print('above')
    # else:
    #     print('below')
