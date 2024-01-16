def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ''

    for char in cryptogram:
        if char.isalpha():
            # Determine the case (upper or lower) of the character
            is_upper = char.isupper()

            # Apply the shift to the character
            decrypted_char = chr((ord(char) - shift - (65 if is_upper else 97)) % 26 + (65 if is_upper else 97))

            decrypted_text += decrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char

    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Example cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG ORFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the shift key
find_shift_key(cryptogram)
