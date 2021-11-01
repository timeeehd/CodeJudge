import sys


def jenkins_one_at_a_time_hash(key, length):
    hash1 = 0
    for i in range(length):
        hash1 += key[i]
        hash1 &= 0xFFFFFFFF
        hash1 += hash1 << 10
        hash1 &= 0xFFFFFFFF
        hash1 ^= hash1 >> 6
        hash1 &= 0xFFFFFFFF
    hash1 += hash1 << 3
    hash1 &= 0xFFFFFFFF
    hash1 ^= hash1 >> 11
    hash1 &= 0xFFFFFFFF
    hash1 += hash1 << 15
    hash1 &= 0xFFFFFFFF
    return hash1


string = sys.stdin.readlines()
# string = string[:-1]
ascii_values = []
length = 0
for sentence in string:
    # sentence = sentence[:-1]
    length += len(sentence)
    for character in sentence:
        ascii_values.append(ord(character))

result = jenkins_one_at_a_time_hash(ascii_values, length)

print('{:x}'.format(result))


# Suggested solution
# h = 0
# for c in sys.stdin.read():
#     h += ord(c)
#     h &= 0xffffffff
#     h += h << 10
#     h &= 0xffffffff
#     h ^= h >> 6
# h += h << 3
# h &= 0xffffffff
# h ^= h >> 11
# h += h << 15
# h &= 0xffffffff
# print(f'{h:08x}')
