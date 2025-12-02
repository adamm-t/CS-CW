Permutation_1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

Permutation_2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]


import random


def generate_random_64bit_key():
    key = []                  # start with an empty list
    for i in range(64):       # loop 64 times
        bit = random.randint(0, 1)   # generate 0 or 1
        key.append(bit)              # add the bit to the list
    return key



#Here we make the function that does the permutations for us, it uses the index of the permuation and applies it to the block of bits we give it and the result goes into an empty list
def permute(block, table):
    result = []
    for index in table:
        result.append(block[index - 1])
    return result




