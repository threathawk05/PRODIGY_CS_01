Caesar Cipher Program
This project is a simple Python program that uses the Caesar Cipher algorithm to encrypt and decrypt messages. The Caesar Cipher is a type of substitution cipher where each letter in the text is "shifted" a fixed number of positions down or up the alphabet.

Features
Encrypts a message by shifting each letter by a specified number of positions.
Decrypts a message by reversing the shift with the same value.
Supports both uppercase and lowercase letters; leaves non-letter characters unchanged.


Prerequisites
Python 3.x is required to run this program.
Git (optional) to clone the repository and manage versions.

Installation
Clone the Repository (optiona):
git clone https://github.com/threathawk05/caesar-cipher.git
cd caesar-cipher
Download the Script Directly:

If you prefer, download caesar_cipher.py directly from GitHub and save it to your desired location.
Usage
Open a terminal and navigate to the folder where caesar_cipher.py is located.

Run the program by executing:
python caesar_cipher.py


Follow the prompts:
Enter your message to encrypt or decrypt.
Specify the shift value (an integer).
Choose whether to encrypt (e) or decrypt (d) the message.


Example
Sample usage of the Caesar Cipher program:

Input:

Message: Hello, World!
Shift: 3
Choice: e (for encrypt)
Output:
Encrypted message: Khoor, Zruog!
Code Explanation
The program includes the following main parts:

encrypt(text, shift): Encrypts text by shifting each letter forward by shift positions in the alphabet.
decrypt(text, shift): Decrypts text by shifting each letter backward by shift positions.
main(): Handles user input and executes either encryption or decryption based on the user's choice.

License
This project is open source and available under the MIT License.

