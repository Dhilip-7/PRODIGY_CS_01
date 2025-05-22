# PRODIGY_CS_01
PRODIGY_CS_01: Caesar Cipher  Decryption
Hey there! Welcome to my first task for the PRODIGY Cyber Security track (Task 01). I built a Python program that implements the Caesar Cipher, a classic encryption technique, and added a cool brute-force decryption feature to crack encrypted messages. This project is all about exploring basic cryptography concepts, which are super relevant to Cyber Security. Let me walk you through what I did, how it works, and how you can try it out!
What’s the Caesar Cipher?
The Caesar Cipher is one of the oldest encryption methods, named after Julius Caesar, who used it to secure his messages. It’s a type of substitution cipher where each letter in your message (plaintext) is shifted by a fixed number of positions in the alphabet to create an encrypted message (ciphertext). For example:

If I shift “CAT” by 3, I get “FDW” (C → F, A → D, T → W).
To decrypt, I shift back by the same number, so “FDW” becomes “CAT” again.

The number of positions you shift (e.g., 3) is the key. It’s a simple but fun way to dive into encryption!
Why Cyber Security?
In Cyber Security, understanding encryption is key (pun intended!). The Caesar Cipher shows how symmetric encryption works, where the same key is used to encrypt and decrypt. It also highlights why simple ciphers aren’t secure today—someone can easily crack them by trying all possible shifts (that’s where my brute-force feature comes in!). This project helped me learn about encryption, key management, and basic cryptanalysis.
What I Built
I wrote a Python program (caesar_cipher.py) that does three things:

Encrypt: Takes a message and a shift value (1–25) and shifts each letter forward to create a ciphertext.
Decrypt: Takes a ciphertext and the same shift value to shift letters back and recover the original message.
Brute-Force Decrypt: Tries every possible shift (1 to 25) to decrypt a message without knowing the key, showing all possible results.

Features

User-Friendly: The program asks you to pick a mode (encrypt, decrypt, or brute-force) and guides you through entering a message and shift value.
Preserves Formatting: Keeps uppercase and lowercase letters as they are and leaves spaces, numbers, and punctuation unchanged.
Input Validation: Checks that the mode is valid (1, 2, or 3) and the shift value is a number between 1 and 25.
Brute-Force Power: The brute-force option shows all possible decryptions, which is great for analyzing how easy it is to crack a Caesar Cipher.
Clean Code: I split the logic into functions (caesar_cipher for encrypt/decrypt, brute_force_decrypt for cracking, and main for the user interface) to keep things organized.

Here’s an example of how it works:

Encryption: Input “Hello” with a shift of 3 → Output “Khoor”.
Decryption: Input “Khoor” with a shift of 3 → Output “Hello”.
Brute-Force: Input “Khoor” → Outputs all 25 possible decryptions, one of which is “Hello” (at shift 3).

Repository Structure
PRODIGY_CS_01/
├── src/
│   └── caesar_cipher.py  # My Python script
├── README.md             # This file, explaining my work
└── LICENSE               # MIT License

How to Set It Up
Want to try it out? Here’s how:

Clone the Repository:git clone https://github.com/Dhilip-7/PRODIGY_CS_01.git


Navigate to the Folder:cd PRODIGY_CS_01


Check for Python:
You need Python 3.x. Run python --version or python3 --version to confirm.


Run the Program:python src/caesar_cipher.py



How to Use It

Run the script: python src/caesar_cipher.py.
Choose a mode:
1 to encrypt a message.
2 to decrypt a message.
3 to brute-force decrypt (no shift value needed).


Enter your message (e.g., “Cyber Security”).
For modes 1 or 2, enter a shift value (1–25, e.g., 5).
Check the output!

Example Run:
Caesar Cipher Program
--------------------
Choose mode:
1. Encrypt
2. Decrypt
3. Brute-Force
Enter mode (1/2/3): 1
Enter the message: Cyber Security
Enter the shift value (1-25): 5
Result: Ijhmw Xjhlwynb

Brute-Force Example:
Enter mode (1/2/3): 3
Enter the message: Ijhmw Xjhlwynb
Brute-Force Decryption Results:
------------------------------
Shift 1: Hignv Wiguwxma
Shift 2: Gfimu Vhftvwlz
...
Shift 5: Cyber Security
...
Shift 25: Jkiox Ykimxzos

What I Learned

Encryption Basics: How the Caesar Cipher shifts letters and why the key matters.
Cryptanalysis: The brute-force feature shows why simple ciphers are weak—trying all 25 shifts takes seconds!
Coding: Writing clean, modular code with input validation to make the program robust.
Cyber Security Insight: This cipher is too basic for real-world use, but it’s a stepping stone to understanding stronger algorithms like AES.

Technologies Used

Python 3: The only tool I needed—no external libraries required.
Standard Library: Used built-in functions like ord(), chr(), and string handling.

Notes

The program only works with the 26-letter English alphabet (A–Z).
The shift value is limited to 1–25 to avoid redundant shifts (a shift of 0 or 26 is the same as no shift).
Brute-force decryption is a simple way to crack the cipher, showing why key length and complexity matter in Cyber Security.

About Me
I’m @dhilip-7, and this is my first task in the PRODIGY Cyber Security track. I had fun building this and learning how encryption ties into protecting data. More to come as I dive deeper into Cyber Security!

