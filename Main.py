from KeyGeneration import generate_key, generate_subkeys
from Encryption import encrypt_block
from Decryption import decrypt_block

def text_to_bits(text):
    bits = []
    for char in text:
        bin_str = format(ord(char), "08b")
        for b in bin_str:
            bits.append(int(b))
    return bits

def split_into_blocks(bits):
    blocks = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        if len(block) < 64:
            block += [0]*(64-len(block)) 
        blocks.append(block)
    return blocks



