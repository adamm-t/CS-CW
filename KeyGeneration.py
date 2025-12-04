perm_1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

perm_2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

shift_schedule = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


import random

#This function will generate 64 numbers either 0 or 1 and add them to an empty list
def generate_key():
    key = []                  
    for i in range(64):       
        bit = random.randint(0, 1)   
        key.append(bit)              
    return key

#Here we make the function that does the permutations for us, it uses the index of the permuation and applies it to the block of bits we give it and the result goes into an empty list
def permute(block, table):
    result = []
    for index in table:
        result.append(block[index - 1])
    return result

#this function shifts the bits that we have depending on the shift schedule of the round
def left_shift(block, n):
     return block[n:] + block[:n]

#we are gonna generate a list of our keys using this function
def generate_subkeys(key64):
    #apply PC-1 to the key bits which removes 8 bits so we have 56 bits
    key56 = permute(key64, perm_1) 

#we split the bits to 2 sides
    right = key56[28:]
    left = key56[:28]
    
#here we make an empty list and we loop through the shift schedule and shift each side 
    subkeys = []
    for shift in shift_schedule:
        right = left_shift(right, shift)
        left = left_shift(left, shift)
        
#now we combine the left and right side so we have 56 bits again, then we use the 2nd permutation to get our key and add it to our list    
        combined = left + right 
        subkey = permute(combined, perm_2) 
        subkeys.append(subkey)
    return subkeys

