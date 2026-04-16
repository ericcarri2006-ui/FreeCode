Validador de Tarjetas - Algoritmo de Luhn
Este proyecto consiste en una implementación en Python del Algoritmo de Luhn, también conocido como fórmula de módulo 10. Es una suma de comprobación utilizada para validar diversos números de identificación, tales como números de tarjetas de crédito y códigos IMEI.

Competencias Adquiridas
El desarrollo de este script ha permitido consolidar los siguientes conocimientos técnicos:

Manipulación Avanzada de Strings: Uso de técnicas de slicing para la inversión de cadenas ([::-1]) y la selección de rangos con saltos ([::2]).

Normalización de Datos: Implementación de tablas de traducción mediante str.maketrans y translate para la limpieza de caracteres no numéricos (espacios y guiones).

Lógica Aritmética: Aplicación de operadores de división entera (//) y módulo (%) para la descomposición y validación de cifras.

Estructuración de Código: Organización del flujo del programa mediante funciones (def) y un punto de entrada principal (main).

Explicación del Código
El programa se divide en dos bloques principales:

1. Función de Verificación (verify_card_number)
La función procesa el número de la tarjeta siguiendo estos pasos:

Inversión y Segmentación: Se invierte el número para operar desde el dígito de control (derecha a izquierda). Se separan los dígitos en posiciones impares y pares.

Procesamiento de Posiciones Impares: Se suman directamente los dígitos que ocupan las posiciones 1, 3, 5, etc.

Procesamiento de Posiciones Pares: * Se multiplica cada dígito por 2.

Si el resultado es mayor o igual a 10 (dos cifras), se suman sus dígitos individuales para obtener un solo valor (por ejemplo, 12 se convierte en 1 + 2 = 3).

Validación Final: Se suman ambos resultados (pares e impares). El número se considera válido si el total es un múltiplo de 10.

2. Función Principal (main)
Este bloque gestiona la interfaz del usuario y la preparación de los datos:

Limpieza: Antes de procesar el número, se eliminan los caracteres especiales para evitar errores de ejecución.

Evaluación: Se invoca la lógica de validación y se devuelve una salida binaria por consola: VALID! o INVALID!.

Ejecución
Para utilizar el validador, es necesario disponer de un intérprete de Python 3.x:
