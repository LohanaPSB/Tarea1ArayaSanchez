def check_char(caracter):  # Metodo de encontar error o no
    # Variables del sistema
    indicadorletra = 0
    indicadorcaracter = 0
    indicadornumero = 0
    # Listas del codigo
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
              "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Aqui se compara si el caracter es un string
    if isinstance(caracter, str):
        # Actualiza variables para esta caracter
        longitud = len(caracter)
        dato = caracter.lower()
        # Si tiene una longitud de uno
        if longitud == 1:

            # Verifica si solo es una letra
            for letra in letras:
                if dato == letra:
                    return "0"  # Caso 1.A
            # Si no cae en el caso C
            else:
                return "Error C"

        # Si la longitud es mayor a 1 entra aqui
        else:
            i = 0

            # Recorre la parabra caracter por caracter
            while (i < longitud):

                # Coloca el caracter actual en minuscula
                dato = caracter[i].lower()
                # Inicializa contadores
                contadorletra = 0
                contadornumero = 0

                # Recorre la lista letras
                for letra in letras:
                    # Si el caracter es igual a alguna de la lista, cuenta
                    if dato == letra:
                        indicadorletra += 1
                        contadorletra += 1

                # Recorre la lista numeros
                for numero in numeros:
                    # Si el caracter es igual a alguna de la lista, cuenta
                    if dato == numero:
                        indicadornumero += 1
                        contadornumero += 1
                # Si no contiene numero ni letra es un caracter y lo cuenta
                if contadornumero == 0 and contadorletra == 0:
                    indicadorcaracter += 1

                # Pasa al siguiente caracter
                i += 1

            # Despues del salir del while comparará
            # Si no tiene caracteres y no tiene letra o numero es caso B
            if indicadorcaracter == 0 and (indicadorletra == 0 or
                                           indicadornumero == 0):
                return "Error B"
            # Si tiene caracteres o letra o numero es el caso C
            elif indicadorcaracter > 0 or (indicadorletra > 0 or
                                           indicadornumero > 0):
                return "Error C"
            # De no cumplirse algo de lo anterior es el caso D
            else:
                return "Error D"
    # Del if de arriba si no es string es el caso D
    else:
        return "Error D"


# Metodo de cambio de mayuscula a minuscula o viseversa
def caps_switch(dato):
    # Verifica que no sea el caso a
    resultado = check_char(dato)
    # Si es el caso a, cambia a mayuscula o a miniscula
    if resultado == "0":
        datonuevo = dato.swapcase()
        return datonuevo

    # De no ser el caso 0 retorna el error
    else:
        return resultado
