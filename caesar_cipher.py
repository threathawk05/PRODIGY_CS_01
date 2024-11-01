# Function to encrypt text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Wrap around the alphabet if shift is larger than 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char  # Leave non-letter characters as they are
    return encrypted_text

# Function to decrypt text
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function to run the program
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
