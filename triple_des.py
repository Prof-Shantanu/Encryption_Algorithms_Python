from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

while True:
    try:
        key= DES3.adjust_key_parity(get_random_bytes(24))
        break
    except valueError:
        pass

def encrypt(msg):
    cipher=DES3.new(key, DES3.MODE_EAX)
    nonce=cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('ascii')

nonce, ciphertext, tag = encrypt(input('Enter the message: '))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
print(f'Plain text: {plaintext}')
