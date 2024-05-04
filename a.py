import random

def generar_folio(distrito):
    """
    Genera un folio aleatorio basado en el distrito dado.

    Args:
        distrito (str): El distrito en formato de cadena.

    Returns:
        str: Un folio aleatorio generado.
    """
    # Verificar que el distrito sea válido
    if len(distrito) != 2 or not distrito.isdigit():
        raise ValueError("El distrito debe ser un número de dos dígitos.")

    # Generar el resto del folio de manera aleatoria
    folio_resto = ''.join([str(random.randint(0, 9)) for _ in range(11)])

    # Combinar el distrito y el resto del folio
    folio = f'{distrito}{folio_resto}'

    return folio

# Ejemplo de uso:
distrito = '30'  # Por ejemplo, distrito 30
cantidad_folios = 100
folios_aleatorios = [generar_folio(distrito) for _ in range(cantidad_folios)]
print("Folios aleatorios:", folios_aleatorios)
