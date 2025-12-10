from KeyGeneration import generate_key
from Encryption import encrypt_block
from Decryption import decrypt_block


#this function will convert any string into bits and store them into a list
def text_to_bits(text):
    bits = ""
    for char in text:
        bits += format(ord(char), "08b")
    return bits

def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        chars.append(chr(int(byte, 2)))
    return "".join(chars)

def pad(bits):
    # pad with zeros to make length multiple of 64
    while len(bits) % 64 != 0:
        bits += "0"
    return bits

#this function will convert our bits into hexadecimal for readability of ciphertext
def bits_to_hex(bits):
    # pad bits so length is multiple of 4
    while len(bits) % 4 != 0:
        bits += "0"

    hex_string = ""

    # convert each 4-bit nibble to hex
    for i in range(0, len(bits), 4):
        nibble = bits[i:i+4]

        nibble_str = ""
        for b in nibble:
            nibble_str += str(b)

        nibble_int = int(nibble_str, 2)
        hex_char = format(nibble_int, "X")
        hex_string += hex_char

    return hex_string

#this function will convert our hexdecimal into bits again when decrypting
def hex_to_bits(hex_string):
    bits = ""

    #convert each hex character to 4-bit binary
    for hex_char in hex_string:
        hex_int = int(hex_char, 16)
        bin_str = format(hex_int, "04b")
        bits += bin_str

    return bits





