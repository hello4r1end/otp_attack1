import itertools

def xor_binaries(binary1, binary2):
    #Perform a  XOR operation between two binary strings.
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)
    result = ''
    for b1, b2 in zip(binary1, binary2):
        xor_bit = '1' if b1 != b2 else '0'
        result += xor_bit
    return result

def string_to_binary(text):
    #Convert a string to its binary representation (ASCII encoding)."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_string(binary_text):
    #Convert a binary string back to ASCII text."""
    return ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))

def xor_binary_strings(bin1, bin2):
    #Perform  XOR operation between two binary strings."""
    max_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_length)
    bin2 = bin2.zfill(max_length)
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(bin1, bin2))

def find_key_part(ciphertext_binary, known_plaintext_bin):
    #Find a part of the key by XORing a known plaintext (in binary) with a part of the ciphertext."""
    key_part = xor_binary_strings(ciphertext_binary[:len(known_plaintext_bin)], known_plaintext_bin)
    return key_part

def main_key_recovery_process():
   #Execute the main key recovery process for one-time pad with key reuse."""
    ciphertext1_binary = input("Enter the first ciphertext in binary: ")
    ciphertext2_binary = input("Enter the second ciphertext in binary: ")
    known_plaintext_decimal = input("Enter the known piece of plaintext in decimal (e.g., '104 101' for 'he'): ")

    known_plaintext = decimal_to_text(known_plaintext_decimal)
    known_plaintext_bin = string_to_binary(known_plaintext)

    key_part_from_c1 = binary_to_string(find_key_part(ciphertext1_binary, known_plaintext_bin))
    key_part_from_c2 = binary_to_string(find_key_part(ciphertext2_binary, known_plaintext_bin))

    print(f"Possible key part from C1: {key_part_from_c1}")
    print(f"Possible key part from C2: {key_part_from_c2}")

def decimal_to_text(decimal_values):
   #Convert space-separated decimal values to text (ASCII characters)."""
    return ''.join(chr(int(value)) for value in decimal_values.split())

def brute_force_segment(ciphertext_segment, key_length):
   #Brute force a segment of the ciphertext."""
    for key_candidate in itertools.product('01', repeat=key_length):
        key_binary = ''.join(key_candidate)
        decrypted_segment = binary_to_string(xor_binary_strings(ciphertext_segment, key_binary))
        print(f"Trying key: {key_binary}, Result: {decrypted_segment}")

def brute_force_option():
    #Brute force method on ciphertexts with known plaintext."""
    ciphertext1_binary = input("Enter the first ciphertext in binary: ")
    ciphertext2_binary = input("Enter the second ciphertext in binary: ")
    known_plaintext = input("Enter the known plaintext: ")
    brute_force_length = int(input("Enter the number of bits to brute force: "))

    known_plaintext_binary = string_to_binary(known_plaintext)
    known_length = len(known_plaintext_binary)

    segment_to_brute_force_c1 = ciphertext1_binary[known_length:known_length+brute_force_length]
    segment_to_brute_force_c2 = ciphertext2_binary[known_length:known_length+brute_force_length]

    print("Brute forcing on Ciphertext 1:")
    brute_force_segment(segment_to_brute_force_c1, brute_force_length)

    print("Brute forcing on Ciphertext 2:")
    brute_force_segment(segment_to_brute_force_c2, brute_force_length)

def main():
   #Main function to choose between different operations."""
    print("Choose an option:")
    print("1. Simple XOR of two binary numbers.")
    print("2. Key recovery process for one-time pad with key reuse.")
    print("3. Brute force method on ciphertexts.")
    
    choice = input("Enter your choice (1, 2, or 3): ")

 
    if choice == '1':
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        result = xor_binaries(binary1, binary2)
        print(f"XOR of {binary1} and {binary2} is {result}")
    elif choice == '2':
        main_key_recovery_process()
    elif choice == '3':
        brute_force_option()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
