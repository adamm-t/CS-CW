import random

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Left shifts round schedule
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

#Here we make the function that does the permutations for us, it uses the index of the permuation and applies it to the block of bits we give it and the result of bits 
def permute(block, table):
    permuted_block = ""

    #we loop over each index in the table that tells us which bits to select
    for index in table:
        #convert the integer bit to string and add it, also we do -1 since in python we start from 0
        bit = str(block[index - 1])
        permuted_block += bit

    return permuted_block



#this function shifts the bits that we have depending on the shift schedule of the round
def left_shift(block, n):
     return block[n:] + block[:n]

#we are gonna generate a list of our keys using the random function
def generate_key():
    key = []                  
    for i in range(64):                
        bit = random.randint(0, 1)
        key.append(bit)
    key64 = key

#then apply PC1 which removes parity bits so we have 56 bits
    key56 = permute(key64, PC1)

#we split the bits into 2 halves
    left = key56[:28]
    right = key56[28:]

    subkeys = []

#here we make the 16 subkeys
    for shift in shift_schedule:

        #we left shift and depending on the round either shift by 1 or 2
        left = left_shift(left, shift)
        right = left_shift(right, shift)

        #combine the halves so we have 56 again
        combined = left + right

        #lastly we apply PC2 to remove another 8 bits which gives us the round key which is 48 bits and gets stored in our list
        subkey = permute(combined, PC2)
        subkeys.append(subkey)
    return subkeys

