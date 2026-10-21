def analizar_texto(frase:str) -> tuple[int, int]:
    """
    Analiza la frase introducida y cuenta el numero de palabras y vocales que tiene

    :param frase: Frase introducida para ser analizada
    :return Devuelve el numero de palabras y el numero de vocales: 
    """
    frase = frase.lower()
    
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü')
    contador_vocales:int = 0

    contador_palabras:int = len(frase.split())

    for caracter in frase:
        if caracter in vocales:
            contador_vocales += 1
            
    return contador_palabras, contador_vocales

def main():
    """Funcion principal"""
    frase = input("Introduce una frase: ")
    total_palabras:int = analizar_texto(frase)[0]
    total_vocales:int = analizar_texto(frase)[1]

    print(f"Palabras:{total_palabras}")
    print(f"Vocales:{total_vocales}")

if __name__ == "__main__":
    main()