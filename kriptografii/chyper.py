# Function to encrypt the text
def encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            # Handle uppercase letters
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.isdigit():
            # Handle numbers
            encrypted_text += chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:
            # Non-alphanumeric characters are added as is
            encrypted_text += char

    return encrypted_text

# Function to decrypt the text
def decrypt(text, key):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - key + 26) % 26 + ord('a'))
            # Handle uppercase letters
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key + 26) % 26 + ord('A'))
        elif char.isdigit():
            # Handle numbers
            decrypted_text += chr((ord(char) - ord('0') - key + 10) % 10 + ord('0'))
        else:
            # Non-alphanumeric characters are added as is
            decrypted_text += char

    return decrypted_text


# Main program
if __name__ == "__main__":
    choice = input("Mau enkripsi atau dekripsi?(e/d)").lower()

    if choice == 'e':
        text = input("Masukan Pesan: ")
        key = int(input("Masukan Kunci: "))
        encrypted_message = encrypt(text, key)
        print(f"Pesan dienkripsi: {encrypted_message}")

    elif choice == 'd':
        text = input("Masukan Pesan: ")
        key = int(input("Masukan Kunci: "))
        decrypted_message = decrypt(text, key)
        print(f"Pesan didekripsi: {decrypted_message}")

    else:
        print("Pilihan salah!!")
