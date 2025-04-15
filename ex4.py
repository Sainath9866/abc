#exp 4 
from Crypto.Cipher import DES
from binascii import unhexlify, hexlify

def des_encrypt(text, key):
    cipher = DES.new(unhexlify(key), DES.MODE_ECB)
    text = unhexlify(text)
    for round_num in range(1, 17):
        text = cipher.encrypt(text)
        print(f"Round {round_num}: {hexlify(text).decode()}")
    return hexlify(text).decode()

def des_decrypt(text, key):
    cipher = DES.new(unhexlify(key), DES.MODE_ECB)
    text = unhexlify(text)
    for round_num in range(1, 17):
        text = cipher.decrypt(text)
        print(f"Round {round_num}: {hexlify(text).decode()}")
    return hexlify(text).decode()

if __name__ == "__main__":
    plaintext, key = "123456ABCD132536", "AABB09182736CCDD"
    print("Plain Text:", plaintext)
    print("Key:", key)
    encrypted_text = des_encrypt(plaintext, key)
    print("Cipher Text:", encrypted_text)
    decrypted_text = des_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)