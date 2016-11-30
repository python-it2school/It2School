alphabet = [ letter for letter in range(ord('a'), ord('z') + 1) ]

def transform(letter, key):
    ord_letter = ord(letter)

    if (ord_letter in alphabet):
        first_letter = alphabet[0]
        transformed = ( (ord_letter + key - first_letter) % len(alphabet) ) + first_letter 
        return chr( transformed )
    else:
        return letter

def cipher(text, key):
    return "".join([transform(letter, key) for letter in text])

    
def decipher(text, key):
    return "".join([transform(letter, -key) for letter in text])

def d_message(message, key):
    print("Используем ключ: {}".format(key))

    print( "Исходный текст: {}".format(message))

    ciphered = cipher(message, key)
    print( "После шифрования: {}".format(ciphered) )

    deciphered = decipher(ciphered, key)
    print( "После дешифрования: {}".format(deciphered) )

d_message("hello world!", 10)
d_message("hello world!", 12)

print("-" * 30)

d_message("very good", 12)