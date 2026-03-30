def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f"Palabra: {palabra}")
    A=len(palabra)
    print(f"Longitud: {A}")
    B=palabra[0]
    print(f"Primera letra: {B}")
    C=palabra[-1]
    print(f"Ultima letra: {C}")
    D=palabra*3
    print(f"Repetida: {D}")
    E="***"+palabra+"***"
    print(f"Decorada: {E}")


