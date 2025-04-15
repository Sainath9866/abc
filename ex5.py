#exp 5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext,key):
  cipher = AES.new(key,AES.MODE_CBC)
  iv = cipher.iv
  encrypted_text = cipher.encrypt(pad(plaintext.encode(),AES.block_size))
  return iv,encrypted_text

def decrypt(cipher_text,key,iv):
  cipher = AES.new(key,AES.MODE_CBC,iv)
  decrypted = unpad(cipher.decrypt(cipher_text),AES.block_size).decode()
  return decrypted

if __name__ == "__main__":
  plaintext =input("Enter the text: ")

  key = get_random_bytes(16)
  iv,encrypted = encrypt(plaintext,key)
  print("IV: ",iv.hex())
  print("Encryptd text : ",encrypted.hex())

  decrypted_text = decrypt(encrypted,key,iv)
  print("Decrypted text: ",decrypted_text)
