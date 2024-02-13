def caesar_cipher_func(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def main():
    message = str(input("Enter the message: "))
    shift = int(input("Enter the shift value: "))
    encrypted = caesar_cipher_func(message, shift)
    print(f"\nEncrypted message: {encrypted}")

    decrypted = caesar_cipher_func(encrypted, -shift)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
