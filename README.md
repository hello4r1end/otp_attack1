# GitHub Documentation for XOR Binary Operation and Cryptanalysis Tool

This repository hosts a Python script designed to perform various operations related to XOR binary manipulations and basic cryptanalysis techniques. It is primarily focused on operations involving binary strings and offers a range of functionalities from simple XOR operations to more complex tasks such as key recovery and brute force methods in the context of one-time pad systems with key reuse.

## Installation

To use this script, clone the repository to your local machine:

```bash
git clone https://github.com/hello4r1end/otp_attack1
```

Make sure Python is installed on your system. This script is compatible with Python 3.x.

## Usage

Run the script using Python:

```bash
python xor_cryptanalysis.py
```

### Main Features

1. **Simple XOR of Binary Numbers**: Perform an XOR operation between two binary strings.

2. **Key Recovery Process for One-Time Pad with Key Reuse**: This function aids in the key recovery process for scenarios where a one-time pad has been reused, compromising its security.

3. **Brute Force Method on Ciphertexts**: This feature allows for a brute force attack on ciphertexts with a known plaintext, useful in scenarios where the key length is relatively short.

### Functions

- `xor_binaries(binary1, binary2)`: XOR operation between two binary strings.
- `string_to_binary(text)`: Convert a string to its binary representation.
- `binary_to_string(binary_text)`: Convert a binary string back to ASCII text.
- `xor_binary_strings(bin1, bin2)`: Perform XOR operation between two binary strings.
- `find_key_part(ciphertext_binary, known_plaintext_bin)`: Find a part of the key by XORing a known plaintext with a part of the ciphertext.
- `main_key_recovery_process()`: Execute the main key recovery process for one-time pad with key reuse.
- `decimal_to_text(decimal_values)`: Convert decimal values to text.
- `brute_force_segment(ciphertext_segment, key_length)`: Brute force a segment of the ciphertext.
- `brute_force_option()`: Brute force method on ciphertexts with known plaintext.

## Contribution

Contributions to this project are welcome. Please fork the repository and submit a pull request for any enhancements, bug fixes, or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Note: Ensure to replace https://github.com/hello4r1end/otp_attack1  with the actual URL of the GitHub repository. This documentation provides a general overview and basic usage guide for the script. Users are encouraged to read the source code for more in-depth understanding.
