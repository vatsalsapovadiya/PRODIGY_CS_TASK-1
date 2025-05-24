def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26 

    for char in text:
        if char.isalpha():
            shift_direction = shift if mode == "encrypt" else -shift
            base = ord("A") if char.isupper() else ord('a')
            new_position = (ord(char) - base + shift_direction) % 26
            new_char = chr(base + new_position)
            result += new_char
        else:
            result += char
    return result

def main():
    print("="*40)
    print("Caesar Cipher Encryptor / Decryptor")
    print("="*40)
    
    while True:
        print("\nMenu: ")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Select an option(1,2,3): ").strip()

        if choice == "1" or choice == "2":
            message = input("Enter the message: ")
            try:
                shift = int(input("Enter shift value(1-25): "))
                if not 1 <= shift <= 25:
                    raise ValueError
            except ValueError:
                print("Invalid shift value. Please enter a number between 1 and 25.")
                input("Press Enter to continue...")
                continue

            mode = "encrypt" if choice == "1" else "decrypt"
            output = caesar_cipher(message, shift, mode)
            print(f"\n{mode.capitalize()}ed message: {output}")

        elif choice == "3":
            print("Exiting the program. See you soon...!!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
