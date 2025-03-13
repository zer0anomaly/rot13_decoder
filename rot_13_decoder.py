import codecs

plaintext = input("Give the plaintext:")

def rot13(text):
    return codecs.encode(text, 'rot_13')

result = rot13(plaintext)

print(result)