def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


def caesar_decrypt(ciphertext, shift):
    # Decrypt by shifting in the opposite direction
    return caesar_encrypt(ciphertext, -shift)


# Example usage
if __name__ == "__main__":
    message = input("Enter the message: ")
    shift = int(input("Enter shift key (1-25): "))

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\nEncrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
