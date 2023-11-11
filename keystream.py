MOD = 256

def KSA(key):
    sched = [i for i in range(0, MOD)]
    
    i = 0
    for j in range(0, MOD):
        i = (i + sched[j] + key[j % len(key)]) % MOD
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp

    return sched

def PRGA(sched):
    i = 0
    j = 0
    
    while True:
        i = (i + 1) % MOD
        j = (j + sched[i]) % MOD
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
        yield sched[(sched[i] + sched[j]) % MOD]
    

def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)
