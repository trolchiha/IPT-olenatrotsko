MOD = 256

class RC4:
    def __init__(self):
        self.key = None
        self.plaintext = None
        self.ciphertext = None

    def __init__(self, key, plaintext, ciphertext):
        self.key = key
        self.plaintext = plaintext
        self.ciphertext = ciphertext

    def set_key(self, key):
        self.key = key

    def set_plaintext(self, plaintext):
        self.plaintext = plaintext

    def set_ciphertext(self, ciphertext):
        self.ciphertext = ciphertext

    def get_key(self):
        return self.key
    
    def get_plaintext(self):
        return self.plaintext
    
    def get_ciphertext(self):
        return self.ciphertext

    def KSA(self, key):       
        sched = [i for i in range(0, MOD)]
    
        i = 0
        for j in range(0, MOD):
            i = (i + sched[j] + key[j % len(key)]) % MOD
            tmp = sched[j]
            sched[j] = sched[i]
            sched[i] = tmp

        return sched
    
    def PRGA(self, sched):
        i = 0
        j = 0
    
        while True:
            i = (i + 1) % MOD
            j = (j + sched[i]) % MOD
            tmp = sched[j]
            sched[j] = sched[i]
            sched[i] = tmp
            
            yield sched[(sched[i] + sched[j]) % MOD]

    def get_keystream(self, key):
        S = self.KSA(key)
        return self.PRGA(S)

    def encrypt(self):
        if self.key is None:
            return
        
        text = [ord(char) for char in self.plaintext]
        key = [ord(char) for char in self.key]

        key_stream = self.get_keystream(key)
        
        ciphertext = ''
        for char in text:
            encrypted = str(hex(char ^ next(key_stream))).upper()
            ciphertext += encrypted

        self.set_ciphertext(ciphertext)
            
        return ciphertext
    
    def decrypt(self):
        if self.key is None:
            return
        
        ciphertext = self.ciphertext.split('0X')[1:]
        ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
        key = [ord(char) for char in self.key]
        
        key_stream = self.get_keystream(key)
        
        plaintext = ''
        for char in ciphertext:
            decrypted = str(chr(char ^ next(key_stream)))
            plaintext += decrypted

        self.set_plaintext(plaintext)
        
        return plaintext
