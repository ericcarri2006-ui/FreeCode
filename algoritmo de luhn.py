def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # Invertimos el número de la tarjeta para empezar a contar desde la derecha
    card_number_reversed = card_number[::-1]
    
    # Extraemos los dígitos en posiciones impares (1º, 3º, 5º...) empezando desde atrás
    odd_digits = card_number_reversed[::2]

    # Sumamos directamente todos los dígitos de las posiciones impares
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Extraemos los dígitos en posiciones pares (2º, 4º, 6º...)
    even_digits = card_number_reversed[1::2]
    
    for digit in even_digits:
        # Multiplicamos por 2 los dígitos de las posiciones pares
        number = int(digit) * 2
        
        # Si el resultado es mayor o igual a 10, sumamos sus dos cifras (ej: 14 -> 1+4 = 5)
        # Esto es lo mismo que restar 9 al número
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        # Acumulamos el resultado en la suma de pares
        sum_of_even_digits += number

    # Calculamos el total combinando ambas sumas
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Si el total es divisible por 10, el número de tarjeta sigue el patrón de Luhn
    return total % 10 == 0

def main():
    # Número de tarjeta de prueba con guiones
    card_number = '4111-1111-4655-1141'
    
    # Creamos una tabla de traducción para limpiar el número de guiones y espacios
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Llamamos a la función y mostramos el veredicto final
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Punto de entrada del programa
main()