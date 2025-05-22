# Caesar Cipher Encryption and Decryption Program with Brute-Force Decryption

def caesar_cipher(text, shift, mode):
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Process each character in the text
    for char in text:
        if char.isalpha():
            # Determine ASCII base (97 for lowercase, 65 for uppercase)
            ascii_base = 65 if char.isupper() else 97
            # Shift the character and wrap around the alphabet
            shifted = (ord(char) - ascii_base + shift) % 26 + ascii_base
            result += chr(shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def brute_force_decrypt(text):
    # Try all possible shifts (1 to 25)
    results = []
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(text, shift, 'decrypt')
        results.append(f"Shift {shift}: {decrypted_text}")
    return results

def main():
    print("Caesar Cipher Program")
    print("--------------------")
    print("Choose mode:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-Force")
    
    # Get user input
    mode = input("Enter mode (1/2/3): ")
    while mode not in ['1', '2', '3']:
        print("Invalid mode! Please choose 1, 2, or 3.")
        mode = input("Enter mode (1/2/3): ")
    
    message = input("Enter the message: ")
    
    if mode in ['1', '2']:
        shift = input("Enter the shift value (1-25): ")
        # Validate shift value
        try:
            shift = int(shift)
            if shift < 1 or shift > 25:
                print("Shift value must be between 1 and 25.")
                return
        except ValueError:
            print("Invalid shift value! Please enter a number.")
            return
        
        # Perform encryption or decryption
        mode_str = 'encrypt' if mode == '1' else 'decrypt'
        result = caesar_cipher(message, shift, mode_str)
        print("\nResult:", result)
    
    elif mode == '3':
        # Perform brute-force decryption
        print("\nBrute-Force Decryption Results:")
        print("------------------------------")
        for result in brute_force_decrypt(message):
            print(result)

if __name__ == "__main__":
    main() 
