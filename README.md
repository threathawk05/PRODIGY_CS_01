# Caesar Cipher Program

A simple Python program to encrypt and decrypt messages using the Caesar Cipher algorithm. This algorithm shifts each letter in a message by a specified number of positions in the alphabet.

## Features

- Encrypt messages by shifting each letter forward by a user-defined number of positions.
- Decrypt messages by reversing the shift using the same value.

- Supports both uppercase and lowercase letters, while leaving non-letter characters unchanged.

## Prerequisites
- Python 3.x to run the program.
- Git (optional) for cloning the repository.
  
## Installation

Option 1: Clone The Repository

```bash
  git clone https://github.com/threathawk05/caesar-cipher.git
cd caesar-cipher

```
Option 2 : Download the Script directly
- Download caesar_cipher.py directly from the repository and save it to your desired location.

## Usage/Examples
Open a terminal and navigate to the folder where caesar_cipher.py is located.

Run the program:

```bash
  python caesar_cipher.py

```

Follow the prompts:

- Enter the message to encrypt or decrypt.
- Specify the shift value (an integer).
- Choose e to encrypt or d to decrypt the message.
Example
Input:

Message: Hello, World!
Shift: 3
Choice: e (for encrypt)

Output:
Encrypted message: -
Khoor, Zruog!



## Code Explanation
- encrypt(text, shift): Encrypts the given text by shifting each letter forward by shift positions.
- decrypt(text, shift): Decrypts the text by shifting each letter backward by shift positions.
- main(): Manages user input and performs either encryption or decryption based on the user’s choice.
  
## License

This project is open source and available under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

