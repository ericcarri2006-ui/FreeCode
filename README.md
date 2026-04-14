Proyecto 01: Cifrador de Vigenere
Este proyecto consiste en una implementación en Python del algoritmo de cifrado de Vigenere. Es una herramienta de criptografía simétrica que utiliza una palabra clave para realizar un cifrado por sustitución polialfabética.

Descripcion
El programa permite transformar un texto legible en un mensaje cifrado mediante el uso de una clave. A diferencia del cifrado Cesar tradicional, donde el desplazamiento es constante, el cifrado de Vigenere utiliza una clave para determinar desplazamientos variables en cada letra del mensaje. El sistema es reversible, permitiendo recuperar el texto original aplicando la misma clave en sentido inverso.

Caracteristicas Tecnicas
Logica de Cifrado: Implementacion de una funcion central que gestiona la aritmetica de caracteres mediante el uso del abecedario ingles (26 caracteres).

Tratamiento de Caracteres Especiales: El algoritmo identifica y preserva espacios y caracteres no alfabeticos, garantizando que la estructura del mensaje original se mantenga tras el proceso.

Uso del Operador Modulo: Implementacion de una clave circular mediante la operacion de residuo, permitiendo que claves mas cortas que el mensaje se repitan de forma indefinida.

Arquitectura de Funciones: Estructura modular con funciones especificas para cifrado y descifrado que llaman a un nucleo logico comun.

Conceptos de Programacion Aplicados
Iteracion controlada: Uso de bucles para el procesamiento secuencial de cadenas de texto.

Control de flujo: Estructuras condicionales para discriminar entre tipos de caracteres.

Parametros por defecto: Configuracion de funciones para determinar la direccion del cifrado (positivo o negativo).

Instrucciones de Uso
Descargar el archivo vigenere.py.

Ejecutar el script mediante el interprete de Python: python vigenere.py.

El programa mostrara por consola el texto original, la clave utilizada y el resultado de las operaciones de cifrado y descifrado.
