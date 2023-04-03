def precio_pollo(peso_kilos, precio_kilo):
    precio =float(peso_kilos * precio_kilo)
    return precio

precio = precio_pollo(17, 2000)

print(f"El precio de venta del pollo es de: {precio}")
