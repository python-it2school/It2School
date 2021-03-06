class DMessageEngine:
    # КОНСТРУКТОР КЛАССА
    def __init__(self, key):
        self.key = key
        self.alphabet = [ letter for letter in range(ord('a'), ord('z') + 1) ]

    def transform(self, letter, key):
        ord_letter = ord(letter)

        if (ord_letter in self.alphabet):
            first_letter = self.alphabet[0]
            transformed = ( (ord_letter + key - first_letter) % len(self.alphabet) ) + first_letter 
            return chr( transformed )
        else:
            return letter

    def cipher(self, message):
        return "".join([self.transform(letter, self.key) for letter in message])

    def decipher(self, ciphered):
        return "".join([self.transform(letter, -self.key) for letter in ciphered])

    def report(self, begin_message):
        print("Используем ключ: {}".format(self.key))

        print( "Исходный текст: {}".format(begin_message))

        ciphered = self.cipher(begin_message)
        print( "После шифрования: {}".format(ciphered) )

        deciphered = self.decipher(ciphered)
        print( "После дешифрования: {}".format(deciphered) )
        
        print("-" * 40)