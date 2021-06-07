# Apartado 34 (Relaciones entre Clases - Relaciones de Dependencia)
class Pais:
    def __init__(self, nom, pre):
        self.nombre = nom
        self.presidente = pre

    def __str__(self):
        txt = "País: {0} / Presidente: {1}"
        return txt.format(self.nombre, self.presidente)


class Ciudad:
    def __init__(self, nom, hab, pai):
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self):
        txt = "Ciudad: {0} / Habitantes: {1} / ({2})"
        return txt.format(self.nombre, self.habitantes, self.pais)


class Urbanizacion:
    def __init__(self, nom, ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        txt = "Urbanización: {0} / ({1})"
        return txt.format(self.nombre, self.ciudad)


pais1 = Pais("España", "Felipe VI")
print(pais1)

ciudad1 = Ciudad("Mataró", 100000, pais1)
print(ciudad1)

urbe1 = Urbanizacion("Vistalegre", ciudad1)
print(urbe1)
