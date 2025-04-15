import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_reverse(e, t):
    return pow(e, -1, t)  # More efficient modular inverse

def rsa_encrypt(message, e, n):
    return pow(message, e, n)  # Faster exponentiation

def rsa_decrypt(cipher, d, n):
    return pow(cipher, d, n)  # Faster exponentiation

if __name__ == "__main__":
    p = int(input("Enter p: "))  # Prime number
    q = int(input("Enter q: "))  # Prime number

    n = p * q
    t = (p - 1) * (q - 1)

    e = 3
    while gcd(e, t) != 1:
        e += 1

    d = mod_reverse(e, t)

    message = int(input("Enter message: "))

    encrypt = rsa_encrypt(message, e, n)
    decrypt = rsa_decrypt(encrypt, d, n)

    print("Ciphertext:", encrypt)
    print("Decrypted Text:", decrypt)

