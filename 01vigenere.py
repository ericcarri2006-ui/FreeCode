text = 'pronto estara navegando'
custom_key = 'velero'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Añadir cualquier carácter que no sea una letra al mensaje (espacios, etc.)
        if not char.isalpha():
            final_message += char
        else:        
            # Encontrar el carácter de la clave correspondiente para cifrar/descifrar
            key_char = key[key_index % len(key)]
            key_index += 1

            # Definir el desplazamiento y la letra cifrada/descifrada
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# Ciframos el mensaje original
encryption = encrypt(text, custom_key)
print(f'\nTexto encriptado: {encryption}')
print(f'Clave: {custom_key}')

# Desciframos para comprobar que vuelve a la normalidad
decryption = decrypt(encryption, custom_key)
print(f'\nTexto desencriptado: {decryption}\n')
