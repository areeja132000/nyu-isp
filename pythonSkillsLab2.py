# I will leave white spaces as they are in my program 
# Was given the assumption that the inputted text would have only a-z (I turned any uppercase letters to lowercase) and white spaces

def char_to_num(character):
  return ord(character) - 97

def num_to_char(integer):
  return chr(integer + 97)

def encrypt(text, encryption_key):
  encrypted_string=""
  for i in range(len(text)):
    if text[i]!=' ':
      encrypted_string+=num_to_char((char_to_num(text[i])+encryption_key)%26)
    else:
      encrypted_string+=' '
  return encrypted_string

def decrypt(text, encryption_key):
  decrypted_string=""
  for i in range(len(text)):
    if text[i]!=' ':
      decrypted_string+=num_to_char((char_to_num(text[i])-encryption_key)%26)
    else:
      decrypted_string+=' '
  return decrypted_string

if __name__ == "__main__":

  encrypt_or_decrypt = input("Would you like to encrypt (enter 'e') or decrypt the string (enter 'd'): ")
  encryption_key = input("Please enter the encryption key: ")
  text = input("Please enter the text you would like to encrypt/decrypt: ")

  if not encryption_key.isnumeric():
    print("Encryption key is not an integer")
    exit()

  encryption_key = int(encryption_key)

  if encrypt_or_decrypt == 'e':
    print("Encrypted text: " + encrypt(text.lower(), encryption_key))
  elif encrypt_or_decrypt == 'd':
    print("Decrypted text: " + decrypt(text.lower(), encryption_key))
  else:
    print("Neither encryption ('e') nor decryption ('d') selected")



