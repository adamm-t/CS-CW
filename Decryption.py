from KeyGeneration import permute
from Encryption import rounds, xor_bits, IP, IP_INV

#the decrypt function is identical to the encrypt since we do the same thing but we just use the keys in reverse order
def decrypt_block(block64, subkeys):

    if len(block64) != 64:
        print("Error: ciphertext must be 64 bits")
        return
    if len(subkeys) != 16:
        print("Error: there must be 16 subkeys")
        return

    permuted = permute(block64, IP)
    left = permuted[:32]
    right = permuted[32:]

#we just change the loop so it starts from key 16 and goes backwards
    for i in range(15, -1, -1): 
        f_out = rounds(right, subkeys[i])
        new_right = xor_bits(left, f_out)
        left = right
        right = new_right

#now we make sure its called plaintext not cipher since this is decryption
    preoutput = right + left
    plaintext = permute(preoutput, IP_INV)

    return plaintext
