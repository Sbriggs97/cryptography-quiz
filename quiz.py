import random

# ==========================
# Question Bank (60 Questions)
# ==========================
questions = [
    {
        "question": "Encryption is best defined as:",
        "options": ["A) Converting ciphertext into plaintext",
                    "B) Converting plaintext into ciphertext",
                    "C) Encoding data for storage efficiency",
                    "D) Representing binary as ASCII"],
        "answer": "B"
    },
    {
        "question": "Which of the following should encryption protect?",
        "options": ["A) Data at rest only",
                    "B) Data in transit only",
                    "C) Both data at rest and data in transit",
                    "D) Only plaintext messages"],
        "answer": "C"
    },
    {
        "question": "Which are examples of full disk encryption?",
        "options": ["A) BitLocker",
                    "B) FileVault",
                    "C) AES Crypt",
                    "D) TPM"],
        "answer": "AB"
    },
    {
        "question": "Entropy in cryptography refers to:",
        "options": ["A) Encryption speed",
                    "B) Randomness/unpredictability",
                    "C) Prime factorization",
                    "D) Block size"],
        "answer": "B"
    },
    {
        "question": "Which encoding standard supports 65,536 characters?",
        "options": ["A) ASCII",
                    "B) UTF-8",
                    "C) UTF-16",
                    "D) Base64"],
        "answer": "C"
    },
    {
        "question": "Which are properties of TRNGs?",
        "options": ["A) Non-deterministic",
                    "B) Aperiodic",
                    "C) Based on physical processes",
                    "D) Always repeatable"],
        "answer": "ABC"
    },
    {
        "question": "Which operator outputs 1 when inputs differ?",
        "options": ["A) AND",
                    "B) OR",
                    "C) XOR",
                    "D) NOT"],
        "answer": "C"
    },
    {
        "question": "What is the result of 5 mod 2?",
        "options": ["A) 0",
                    "B) 1",
                    "C) 2",
                    "D) 3"],
        "answer": "B"
    },
    {
        "question": "Which type of numbers are fundamental in public key cryptography?",
        "options": ["A) Rational numbers",
                    "B) Prime numbers",
                    "C) Real numbers",
                    "D) Irrational numbers"],
        "answer": "B"
    },
    {
        "question": "Which number theory concepts are used in cryptography?",
        "options": ["A) Modular arithmetic",
                    "B) Prime numbers",
                    "C) Permutations",
                    "D) Combinations"],
        "answer": "ABCD"
    },
    {
        "question": "Which endian format stores the least significant byte first?",
        "options": ["A) Big Endian",
                    "B) Little Endian",
                    "C) Middle Endian",
                    "D) Reverse Endian"],
        "answer": "B"
    },
    {
        "question": "Which PKCS standard defines password-based encryption?",
        "options": ["A) PKCS #5",
                    "B) PKCS #7",
                    "C) PKCS #10",
                    "D) PKCS #12"],
        "answer": "A"
    },
    {
        "question": "Which PKCS standard is used for Certificate Signing Requests (CSR)?",
        "options": ["A) PKCS #5",
                    "B) PKCS #7",
                    "C) PKCS #10",
                    "D) PKCS #12"],
        "answer": "C"
    },
    {
        "question": "Which are ways to check if a certificate is still valid?",
        "options": ["A) CRL (Certificate Revocation List)",
                    "B) OCSP (Online Certificate Status Protocol)",
                    "C) AES key length",
                    "D) TPM check"],
        "answer": "AB"
    },
    {
        "question": "Which events in probability are independent?",
        "options": ["A) Rolling a die and flipping a coin",
                    "B) Drawing cards without replacement",
                    "C) Modular arithmetic",
                    "D) XOR operations"],
        "answer": "A"
    },
    {
        "question": "Which endian format stores the most significant byte first?",
        "options": ["A) Little Endian",
                    "B) Big Endian",
                    "C) Reverse Endian",
                    "D) Mixed Endian"],
        "answer": "B"
    },
    {
        "question": "Which are properties of hashing functions?",
        "options": ["A) One-way (irreversible)",
                    "B) Produces fixed-length output",
                    "C) Detects integrity violations",
                    "D) Requires a key pair"],
        "answer": "ABC"
    },
    {
        "question": "Which probability event means both cannot occur together?",
        "options": ["A) Dependent",
                    "B) Independent",
                    "C) Mutually exclusive",
                    "D) Random"],
        "answer": "C"
    },
    {
        "question": "Which cipher shifts letters a fixed distance in the alphabet?",
        "options": ["A) Caesar",
                    "B) Playfair",
                    "C) Vigenere",
                    "D) Bifid"],
        "answer": "A"
    },
    {
        "question": "Which are mono-alphabetic ciphers?",
        "options": ["A) Caesar",
                    "B) Pigpen",
                    "C) Vigenere",
                    "D) Playfair"],
        "answer": "AB"
    },
    {
        "question": "Which cipher uses a keyword repeated across text?",
        "options": ["A) Playfair",
                    "B) Vigenere",
                    "C) Caesar",
                    "D) Pigpen"],
        "answer": "B"
    },
    {
        "question": "Which cipher uses a 5x5 grid and omits the letter J?",
        "options": ["A) Playfair",
                    "B) Bifid",
                    "C) Rail Fence",
                    "D) Four-square"],
        "answer": "A"
    },
    {
        "question": "Which are polyalphabetic ciphers?",
        "options": ["A) Vigenere",
                    "B) Enigma",
                    "C) One-time pad",
                    "D) Caesar"],
        "answer": "ABC"
    },
    {
        "question": "Which WWII cipher machine ensured plaintext letters never encrypted to themselves?",
        "options": ["A) Enigma",
                    "B) Bifid",
                    "C) Caesar",
                    "D) Pigpen"],
        "answer": "A"
    },
    {
        "question": "Which cipher is considered unbreakable if used properly?",
        "options": ["A) Vigenere",
                    "B) Enigma",
                    "C) One-time pad",
                    "D) Caesar"],
        "answer": "C"
    },
    {
        "question": "Which is the main challenge with symmetric encryption?",
        "options": ["A) Too slow",
                    "B) Key distribution",
                    "C) Requires two different keys",
                    "D) Doesn’t work for bulk data"],
        "answer": "B"
    },
    {
        "question": "Which block cipher mode is considered weakest?",
        "options": ["A) ECB",
                    "B) CBC",
                    "C) CFB",
                    "D) CTR"],
        "answer": "A"
    },
    {
        "question": "Which modes make block ciphers behave like stream ciphers?",
        "options": ["A) CFB",
                    "B) OFB",
                    "C) CTR",
                    "D) ECB"],
        "answer": "ABC"
    },
    {
        "question": "Which cipher mode allows parallel processing?",
        "options": ["A) CBC",
                    "B) ECB",
                    "C) CTR",
                    "D) OFB"],
        "answer": "C"
    },
    {
        "question": "Which are stream ciphers?",
        "options": ["A) RC4",
                    "B) A5/1",
                    "C) A5/2",
                    "D) ChaCha20"],
        "answer": "ABD"
    },
    {
        "question": "Which are block ciphers?",
        "options": ["A) AES",
                    "B) DES",
                    "C) KASUMI (A5/3)",
                    "D) RC4"],
        "answer": "ABC"
    },
    {
        "question": "Which hashing method includes a secret key for authentication?",
        "options": ["A) SHA",
                    "B) HMAC",
                    "C) MD5",
                    "D) Base64"],
        "answer": "B"
    },
    {
        "question": "Which password-based system generates a new password each use?",
        "options": ["A) OTP",
                    "B) SHA",
                    "C) RSA",
                    "D) AES"],
        "answer": "A"
    },
    {
        "question": "Which OTP variant is based on time?",
        "options": ["A) HOTP",
                    "B) TOTP",
                    "C) HMAC",
                    "D) SHA"],
        "answer": "B"
    },
    {
        "question": "Which public key algorithm is based on factoring large numbers?",
        "options": ["A) Diffie-Hellman",
                    "B) RSA",
                    "C) ECC",
                    "D) OTP"],
        "answer": "B"
    },
    {
        "question": "Which algorithm is more efficient for embedded devices than RSA?",
        "options": ["A) AES",
                    "B) ECC",
                    "C) RC4",
                    "D) DES"],
        "answer": "B"
    },
    {
        "question": "Which key exchange method is vulnerable to man-in-the-middle attacks?",
        "options": ["A) Diffie-Hellman",
                    "B) RSA",
                    "C) ECC",
                    "D) OTP"],
        "answer": "A"
    },
    {
        "question": "Which cipher suite weakness was exploited by DHE_EXPORT attacks?",
        "options": ["A) 512-bit primes",
                    "B) 128-bit AES",
                    "C) 3DES keys",
                    "D) SHA-1 hashes"],
        "answer": "A"
    },
    {
        "question": "Which cipher algorithm is called KASUMI?",
        "options": ["A) A5/1",
                    "B) A5/2",
                    "C) A5/3",
                    "D) RC4"],
        "answer": "C"
    },
    {
        "question": "Which WPA2 mode uses AES-CCMP?",
        "options": ["A) Personal and Enterprise",
                    "B) Only Personal",
                    "C) Only Enterprise",
                    "D) WEP compatibility"],
        "answer": "A"
    },
    {
        "question": "Which are weaknesses of WEP?",
        "options": ["A) 24-bit IV",
                    "B) Weak key scheduling (FMS)",
                    "C) No replay protection",
                    "D) MIC protection"],
        "answer": "ABC"
    },
    {
        "question": "Which algorithm threatens RSA, DH, and ECC with quantum computing?",
        "options": ["A) Grover’s",
                    "B) Shor’s",
                    "C) AES-CTR",
                    "D) RC4"],
        "answer": "B"
    },
    {
        "question": "Which algorithm halves brute force time for symmetric ciphers in quantum models?",
        "options": ["A) Grover’s",
                    "B) Shor’s",
                    "C) RSA",
                    "D) AES"],
        "answer": "A"
    },
    {
        "question": "Which hash function is vulnerable to rainbow table attacks without salting?",
        "options": ["A) SHA",
                    "B) HMAC",
                    "C) MD5",
                    "D) SHA-2"],
        "answer": "A"
    },
    {
        "question": "Which algorithm is used to exchange symmetric keys securely?",
        "options": ["A) Diffie-Hellman",
                    "B) Vigenere",
                    "C) OTP",
                    "D) Pigpen"],
        "answer": "A"
    },
    {
        "question": "Which public key algorithm can also provide digital signatures?",
        "options": ["A) El Gamal",
                    "B) Caesar",
                    "C) AES",
                    "D) OTP"],
        "answer": "A"
    },
    {
        "question": "Which advanced public key algorithm prevents adaptive chosen ciphertext attacks?",
        "options": ["A) Cramer-Shoup",
                    "B) El Gamal",
                    "C) RSA",
                    "D) AES"],
        "answer": "A"
    },
    {
        "question": "Which describes Diffie-Hellman with elliptic curves?",
        "options": ["A) DHE_EXPORT",
                    "B) ECDHE",
                    "C) PKCS #7",
                    "D) AES-CTR"],
        "answer": "B"
    },
    {
        "question": "Which cipher mode requires an IV for the first block?",
        "options": ["A) ECB",
                    "B) CBC",
                    "C) CTR",
                    "D) OFB"],
        "answer": "B"
    },
    {
        "question": "Which cipher mode is least secure because patterns remain visible?",
        "options": ["A) ECB",
                    "B) CTR",
                    "C) CBC",
                    "D) CFB"],
        "answer": "A"
    },
    {
        "question": "Which cipher mode is best for parallel processing?",
        "options": ["A) ECB",
                    "B) CBC",
                    "C) CTR",
                    "D) OFB"],
        "answer": "C"
    },
    {
        "question": "Which cipher uses rotor machines and plugboards?",
        "options": ["A) Enigma",
                    "B) Playfair",
                    "C) Caesar",
                    "D) Four-square"],
        "answer": "A"
    },
    {
        "question": "Which is the U.S. government’s old standard block cipher, replaced by AES?",
        "options": ["A) DES",
                    "B) ECC",
                    "C) El Gamal",
                    "D) RC4"],
        "answer": "A"
    },
    {
        "question": "Which key exchange provides forward secrecy?",
        "options": ["A) Static RSA",
                    "B) ECDHE",
                    "C) DES",
                    "D) OTP"],
        "answer": "B"
    },
    {
        "question": "Which hash function produces fixed-length output regardless of input?",
        "options": ["A) SHA",
                    "B) Base64",
                    "C) ASCII",
                    "D) UTF-16"],
        "answer": "A"
    },
    {
        "question": "Which algorithm was a wireless stream cipher used in GSM?",
        "options": ["A) A5/1",
                    "B) AES",
                    "C) ECC",
                    "D) Diffie-Hellman"],
        "answer": "A"
    },
    {
        "question": "Which wireless security protocol introduced TKIP as a patch to WEP?",
        "options": ["A) WPA",
                    "B) WPA2",
                    "C) GSM",
                    "D) AES"],
        "answer": "A"
    },
    {
        "question": "Which protocol introduced AES-CCMP as mandatory?",
        "options": ["A) WEP",
                    "B) WPA",
                    "C) WPA2",
                    "D) GSM"],
        "answer": "C"
    },
    {
        "question": "Which algorithm did Bitcoin adopt for its cryptography?",
        "options": ["A) RSA",
                    "B) ECC (secp256k1)",
                    "C) Diffie-Hellman",
                    "D) AES"],
        "answer": "B"
    },
    {
        "question": "Which is the purpose of salting in encryption?",
        "options": ["A) Makes ciphertext smaller",
                    "B) Adds randomness to prevent repeat ciphertexts",
                    "C) Replaces keys with IVs",
                    "D) Speeds up decryption"],
        "answer": "B"
    },
]

# ==========================
# Quiz Logic
# ==========================
def run_quiz():
    score = 0
    missed = []

    # Randomize question order
    random.shuffle(questions)

    print("\n🔐 Welcome to the Cryptography Quiz! 🔐")
    print("Enter your answer as letters (e.g., A, B, or AB for multiple).\n")

    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for opt in q['options']:
            print(opt)

        user_answer = input("Your answer: ").strip().upper()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer was: {q['answer']}\n")
            missed.append((q['question'], q['answer'], user_answer))

    # Final Results
    print("=" * 40)
    print(f"Quiz Complete! Your Score: {score}/{len(questions)}")
    print("=" * 40)

    if missed:
        print("\nReview of Missed Questions:")
        for m in missed:
            print(f"- {m[0]}")
            print(f"   Your answer: {m[2]}")
            print(f"   Correct answer: {m[1]}\n")
    else:
        print("🎉 Perfect Score! Well done!")

# ==========================
# Run
# ==========================
if __name__ == "__main__":
    run_quiz()
