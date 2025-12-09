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

def bits_to_hex(bits):
    hex_string = ""
    for i in range(0, len(bits), 4):
        nibble = bits[i:i+4]               
        nibble_str = "".join(str(b) for b in nibble)  
        nibble_int = int(nibble_str, 2)   
        hex_string += format(nibble_int, "x") 
    return hex_string

def hex_to_bits(hex_string):
    bits = []
    for h in hex_string:
        b = f"{int(h,16):04b}"
        for bit in b:
            bits.append(int(bit))
    return bits



