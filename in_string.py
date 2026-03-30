def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    name=input("ingresa un nombre")
    namem=name.lower()

    "a" in namem
    "e" in namem
    "i" in namem
    "o" in namem
    "u" in namem

    print(f"Contiene a: {"a" in namem}")
    print(f"Contiene e: {"e" in namem}")
    print(f"Contiene i: {"i" in namem}")
    print(f"Contiene o: {"o" in namem}")
    print(f"Contiene u: {"u" in namem}")
    pass


