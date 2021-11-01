// import sys

// def jenkins_one_at_a_time_hash(key, length):
//     hash1 = 0
//     for i in range(length):
//         hash1 += key[i]
//         hash1 &= 0xFFFFFFFF
//         hash1 += hash1 << 10
//         hash1 &= 0xFFFFFFFF
//         hash1 ^= hash1 >> 6
//         hash1 &= 0xFFFFFFFF
//     hash1 += hash1 << 3
//     hash1 &= 0xFFFFFFFF
//     hash1 ^= hash1 >> 11
//     hash1 &= 0xFFFFFFFF
//     hash1 += hash1 << 15
//     hash1 &= 0xFFFFFFFF
//     return hash1


// str = sys.stdin.readline()
// str = str[:-1]
// ascii_values = []
// for character in str:
//     ascii_values.append(ord(character))
// hello = jenkins_one_at_a_time_hash(ascii_values, len(str))

// print('{:x}'.format(hello))
console.log('test')
