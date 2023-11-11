from keystream import get_keystream


def encrypt(text, key):
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]

    key_stream = get_keystream(key)
    
    ciphertext = ''
    for char in text:
        encrypted = str(hex(char ^ next(key_stream))).upper()
        ciphertext += encrypted
        
    return ciphertext
   

def decrypt(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    
    key_stream = get_keystream(key)
    
    plaintext = ''
    for char in ciphertext:
        decrypted = str(chr(char ^ next(key_stream)))
        plaintext += decrypted
    
    return plaintext
