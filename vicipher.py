alpha = []
temp = [str(chr(x)) for x in range(65, 91)]
alpha.append(temp)
for i in range(25):
    temp = temp[1:] + temp[:1]

    alpha.append(temp)

#print(len(alpha))


def encrypt(plaintext, key):

    global alpha
    plaintext = list(plaintext.upper().replace(" ", ""))
    key = list(key.upper().replace(" ", ""))

    #print(plaintext,key)

    plen = len(plaintext)

    while plen >= len(key):
        key += key[:]
    key = key[:len(plaintext)]
    #print(plaintext,key)

    ciphertext = []

    for i in range(plen):

        ch = alpha[ord(plaintext[i]) - 65][ord(key[i]) - 65]

        ciphertext.append(ch)
    ciphertext = ''.join(map(str, ciphertext))
    print("encrypted : ", ciphertext)

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = []
    global alpha
    print(key)
    key = list(key.upper().replace(" ", ""))
    ciphertext = list(ciphertext.upper().replace(" ", ""))
    plen = len(ciphertext)

    while plen >= len(key):
        key += key[:]
    key = key[:plen]
    print(ciphertext, key)

    for i in range(len(ciphertext)):
        plaintext.append(chr(alpha[ord(key[i]) - 65].index(ciphertext[i]) +
                             65))
    return ''.join(map(str, plaintext))


#print("decrpted : ",decrypt(ciphertext,key))