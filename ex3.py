#-------------------------- 3rd Experiment  ----------------------------------------------------

import hashlib
def compute_hash(text):
  sha1_hash = hashlib.sha1(text.encode()).hexdigest()
  sha256_hash = hashlib.sha256(text.encode()).hexdigest()
  sha512_hash = hashlib.sha512(text.encode()).hexdigest()
  print(sha1_hash)
  print(sha256_hash)
  print(sha512_hash)

if __name__ =="__main__":
  text = input("Enter the text:")
  compute_hash(text)