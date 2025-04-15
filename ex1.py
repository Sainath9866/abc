def encrypt_text(plaintext,n):
    ans = ""
    for ch in plaintext:
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans
plaintext = input("Enter the text: ")
n = int(input("Enter the shift pattern: "))

print("Cipher Text is : " + encrypt_text(plaintext,n))
