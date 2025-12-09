from KeyGeneration import generate_key, generate_subkeys
from Encryption import encrypt_block
from Decryption import decrypt_block


#this function will convert any string into bits and store them into a list
def text_to_bits(text):
    bits = []
    for char in text:
        bin_str = format(ord(char), "08b")
        for b in bin_str:
            bits.append(int(b))
    return bits

#this function will split all the bits into blocks of 64 bits for the DES program to run
def split_into_blocks(bits):
    blocks = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        if len(block) < 64:
            block += [0]*(64-len(block)) 
        blocks.append(block)
    return blocks

#this function will convert our bits into hexadecimal for readability of ciphertext
def bits_to_hex(bits):
    hex_string = ""
    for i in range(0, len(bits), 4):
        nibble = bits[i:i+4]               
        nibble_str = "".join(str(b) for b in nibble)  
        nibble_int = int(nibble_str, 2)   
        hex_string += format(nibble_int, "x") 
    return hex_string

#this function will convert our hexdecimal into bits again when decrypting
def hex_to_bits(hex_string):
    bits = []
    for h in hex_string:
        b = f"{int(h,16):04b}"
        for bit in b:
            bits.append(int(bit))
    return bits

#Here we start the main program and take an input from the user for the plaintext
print("Enter your message:")
message = input("--> ")

#Generate random 64-bit key and all the subkeys
key64 = generate_key()
subkeys = generate_subkeys(key64)

#display the key in hexadecimal  so its readable
print("\nGenerated Key (HEX):")
print(bits_to_hex(key64))

#convert the message into bits and then split the bits into blocks of 64 bits
message_bits = text_to_bits(message)
blocks = split_into_blocks(message_bits)

#we make the empty strings that will store the ciphertext and the actual text
encrypted_hex_total = ""
decrypted_text = ""

#make an empty list that will store all the encrypted blocks so we can convert them
print("\nEncrypting...\n")
encrypted_blocks = []

#here we loop through all the message bits blocks and encrypt them
for block in blocks:
    encrypted_bits = encrypt_block(block, subkeys)

#we convert the bits to hexa decimal and keep appending them to the variable we made 
    encrypted_hex = bits_to_hex(encrypted_bits)
    encrypted_hex_total += encrypted_hex

#here we add the hexadecimal block into the list of blocks and print it 
    encrypted_blocks.append(encrypted_hex)
    print("Block →", encrypted_hex)

#display the ciphertext in hexadecimal
print("\nFinal Ciphertext (HEX):")
print(encrypted_hex_total)



