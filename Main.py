from KeyGeneration import generate_key
from Encryption import encrypt_block
from Decryption import decrypt_block


# --- Helper functions ---
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
    while len(bits) % 64 != 0:
        bits += "0"
    return bits


def bits_to_hex(bits):
    while len(bits) % 4 != 0:
        bits += "0"

    hex_string = ""
    for i in range(0, len(bits), 4):
        nibble = bits[i:i+4]
        nibble_str = ""
        for b in nibble:
            nibble_str += str(b)
        nibble_int = int(nibble_str, 2)
        hex_char = format(nibble_int, "X")
        hex_string += hex_char

    return hex_string


def hex_to_bits(hex_string):
    bits = ""
    for hex_char in hex_string:
        hex_int = int(hex_char, 16)
        bin_str = format(hex_int, "04b")
        bits += bin_str
    return bits


#To run the program we make the main function where we do all the processes
def main():
    print("===================================")
    print("        SIMPLE DES ENCRYPTION       ")
    print("===================================\n")

    #we store the ciphertext here so the user can decrypt from it
    last_ciphertext = ""

    #we generate our 16 keys and store them 
    subkeys = generate_key() 

    #this is our menu loop where the user can choose to input or decrypt or exit
    while True:
        print("\nDES MENU:")
        print("1. Encrypt message")
        print("2. Decrypt last ciphertext")
        print("3. Exit")
        choice = input("Choose an option: ")

        #if they choose 1 then we start encrypting the input taken from the user
        if choice == "1":
            plaintext = input("Enter message: ")

            #we pad the message bits so that they are a multiple of 64 since DES works in blocks of 64
            bits = pad(text_to_bits(plaintext))

            last_ciphertext_bits = ""

            #we loop over the bits and encrypt each block of 64 and store it in last_cyphertext in hexadecimal
            for i in range(0, len(bits), 64):
                block = bits[i:i+64]
                last_ciphertext_bits += encrypt_block(block, subkeys)                
            last_ciphertext = bits_to_hex(last_ciphertext_bits)

            #we display to the user the ciphertext
            print("\nCiphertext (HEX):")
            print(last_ciphertext)


        #if the choice was 2 then we decrypt from the ciphertext that we stored
        elif choice == "2":

            #check if there is anything stored to decrypt from
            if last_ciphertext != "":

                #we convert our ciphertext back to bits
                bits = hex_to_bits(last_ciphertext)
                decrypted_bits = ""

                #we loop over all the bits and decrypt each block of 64 back into text and store it
                for i in range(0, len(bits), 64):
                    block = bits[i:i+64]
                    decrypted_bits += decrypt_block(block, subkeys)
                decrypted_text = bits_to_text(decrypted_bits)

                #display the plaintext which should match the input
                print("\nDecrypted plaintext:")
                print(decrypted_text)
            else:
                print("\nNo ciphertext available to decrypt!")

        elif choice == "3":
            print("\nExiting...")
            exit()

        else:
            print("\nInvalid choice!")


# --- Run the program ---
main()
