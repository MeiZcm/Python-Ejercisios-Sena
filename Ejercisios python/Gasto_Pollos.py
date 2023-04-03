def costo_produccion_pollos(num_pollos, costo_alimento, costo_alojamiento, costo_veterinario):
    costo_alimentacion = num_pollos * 2 * costo_alimento  # Supongamos que cada pollo come 2 kg de alimento
    costo_alojamiento = num_pollos * costo_alojamiento
    costo_veterinario = num_pollos * 0.1 * costo_veterinario  # Supongamos que el 10% de los pollos necesitan atención veterinaria
    costo_total = costo_alimentacion + costo_alojamiento + costo_veterinario
    return costo_total

costo_total = costo_produccion_pollos(1000, 0.5, 2, 10)
print(costo_total)
