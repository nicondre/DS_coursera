"""
Clase 3: Trabajando con Letras ARS
"""


def tea(precio, capital, plazo):
    """
    Calcula la TEA de una letra.
    Parámetros:
        precio  : Precio de la letra cada 100 VN.
        capital : Monto de capital que devuelve la letra cada 100 VN.
        plazo   : Plazo residual en días.
    """
    return (capital / precio) ** (365. / plazo) - 1.


def tna(precio, capital, plazo):
    """
    Calcula la TNA de una letra.
    Parámetros:
        precio  : Precio de la letra cada 100 VN.
        capital : Monto de capital que devuelve la letra cada 100 VN.
        plazo   : Plazo residual en días.
    """
    return ((capital / precio) - 1.) * (365. / plazo)


if __name__ == '__main__':
    # Los imports los realizo acá y no arriba de todo porque sólo voy a
    # utilizar estos paquetes en este pequeño script de abajo. No hace falta
    # que sea global a tódo el módulo.
    import json
    import matplotlib.pyplot as plt

    data = json.load(open('data/c3_mkt_data.json'))

    # Usando loop tradicional
    for lc, ld in data['mercado'].items():
        # Debajo **ld funciona sólo si ld es un dict que tiene las mismas
        # etiquetas que los nombres de los parámteros de la función. Hace
        # tea(ld['precio'], ld['capital'], ld['plazo']) de forma automática.
        irr = tea(**ld)

        # Si ld en vez de un dict fuese una list de tantos elementos como
        # parámetros tenga la función, en nuestro caso 3, por ejemplo
        # [90.25, 100.0, 7] (importante aquí el ordenamiento) podríamos llamar
        # a la función tea(*ld). Notar el uso de 1 SOLO asterisco en vez de 2.

        print(f'{lc} - TEA = {irr:7.2%} - Plazo = {ld["plazo"]:3}')

    # Usando list comprehension
    curve = [(ld['plazo'], tea(**ld)) for ld in data['mercado'].values()]

    # Graficamos curva
    plt.scatter([d for d, y in curve], [y for d, y in curve])
    plt.show()
