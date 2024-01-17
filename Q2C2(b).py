def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_text = ""
    for char in cryptogram:
        if char.isalpha():
            ascii_value = ord(char)
            decrypted_char = chr((ascii_value - shift_key - ord('A')) % 26 + ord('A')) if char.isupper() else \
                             chr((ascii_value - shift_key - ord('a')) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNIAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

for shift_key in range(26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift_key)
    print(f"Shift Key {shift_key}: {decrypted_text}")
