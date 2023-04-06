import random
import sys

prefix = sys.argv[1]
gennum = int(sys.argv[2])

random.seed(2023)
def rand_16b():
    bit_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    res = ""
    for i in range(4):
        res += bit_code[random.randint(0, 15)]
    return res

# now only consider prefix mask that can be divided exactly by 16
def genone_from_prefix(pfx):
    mask = int(pfx[-2:]) // 16
    non_zero_prefix = prefix[:-3].strip("::")
    nzpfxes = non_zero_prefix.split(':')
    non_zero_prefix_len = len(nzpfxes)
    result = ""
    assert(mask < 128)
    for i in range(mask):
        if i < non_zero_prefix_len:
            result += nzpfxes[i] + ":"
        else:
            result += "0:"
    for i in range(8-mask):
        result += rand_16b() + ":"
    return result[:-1]

for i in range(gennum):
    print(genone_from_prefix(prefix))