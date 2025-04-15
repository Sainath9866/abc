
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()
with open('private.pem', 'wb') as f:
    f.write(private_key)
with open('public.pem', 'wb') as f:
    f.write(public_key)
def sign_message(message, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature
def verify_signature(message, signature,public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
if __name__ == "__main__":
    message = "This is a secret message."
    signature = sign_message(message, private_key)
    print(f"Signature: {signature.hex()}")
    is_valid = verify_signature(message, signature,public_key)
    print(f"Signature valid: {is_valid}")
