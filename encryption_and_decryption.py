from rc4_algorithm import get_keystream


def encrypt(text, key):
    '''
    Encrypt a text using the RC4 stream cipher.

    Parameters:
        text (str): The plaintext to be encrypted.
        key (str): The encryption key.

    Returns:
        str: The encrypted ciphertext in hexadecimal format.
    '''
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]

    key_stream = get_keystream(key)
    
    ciphertext = ''
    for char in text:
        encrypted = str(hex(char ^ next(key_stream))).upper()
        ciphertext += encrypted
        
    return ciphertext
   

def decrypt(ciphertext, key):
    '''
    Decrypt a RC4-encrypted ciphertext.

    Parameters:
        ciphertext (str): The ciphertext in hexadecimal format.
        key (str): The decryption key.

    Returns:
        str: The decrypted plaintext.
    '''
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    
    key_stream = get_keystream(key)
    
    plaintext = ''
    for char in ciphertext:
        decrypted = str(chr(char ^ next(key_stream)))
        plaintext += decrypted
    
    return plaintext
