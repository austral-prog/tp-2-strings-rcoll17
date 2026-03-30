def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio= int(input("Precio:"))
    descuento= float(input("Descuento:"))
    cantidad= int(input("Cantidad:"))

    preciodes=precio-descuento
    total=preciodes*cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {preciodes}")
    print(f"Total: {total}")
    pass
