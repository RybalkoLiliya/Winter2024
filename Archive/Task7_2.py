def caesar_encrypter(text, shift):

    ab = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for char in text.lower():
        if char in ab:
            new_index = (ab.index(char) + shift) % len(ab)
            encrypted_text += ab[new_index]
        else:
            encrypted_text += char
    return encrypted_text


print(caesar_encrypter('Dictum – factum', 1))

