from Encryption import encrypt_block

#the decrypt function is identical to the encrypt since we do the same thing but we just use the keys in reverse order
def decrypt_block(block64, subkeys):
    return encrypt_block(block64, list(reversed(subkeys)))
