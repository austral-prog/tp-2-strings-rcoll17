def ficha():

    A = input("Nombre completo").strip()
    B = input("Email").strip().lower()
    nota1 = int(input("Nota 1"))
    nota2 = int(input("Nota 2"))
    nota3 = int(input("Nota 3"))

    D = A.title()
    E = D.find(" ")

    nombre = D[:E]
    apellido = D[E + 1:]
    dom = B.find("@")

    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {D}")
    print(f"Email: {B}")
    print(f"Caracteres en nombre: {len(D)}")
    print(f"Iniciales: {D[0] + D[E + 1]}")
    print(f"Usuario: {apellido.lower()}.{nombre.lower()}")
    print(f"Email valido: {'@' in B}")
    print(f"Dominio: {B[dom + 1:]}")
    print(f"Nombre para archivo: {D.replace(' ', '_')}")
    print(f"Cantidad de a: {D.lower().count('a')}")
    print(f"Codigo secreto: {D[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("========================")


ficha()
