# Materia: Algoritmos y Estructuras de Datos II
# Alumno: Lautaro Cazon
# Ejercicio N°: 1
# Fecha de entrega: 23/04/2026

# ============================================================
# EJERCICIO: Sistema de transporte con herencia y polimorfismo
# ============================================================


# ── CLASE BASE ───────────────────────────────────────────────
class Vehiculo:
    """Clase madre que representa un vehículo genérico."""

    def __init__(self, marca, velocidad_max):
        # Atributos comunes a todos los vehículos
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
        # Método base, será sobreescrito por cada subclase
        print(f"Vehículo: {self.marca} | Velocidad máxima: {self.velocidad_max} km/h")


# ── SUBCLASE: Auto ───────────────────────────────────────────
class Auto(Vehiculo):
    """Clase hija que representa un auto. Hereda de Vehiculo."""

    def __init__(self, marca, velocidad_max, cantidad_puertas):
        # Llamamos al constructor de la clase madre para heredar sus atributos
        super().__init__(marca, velocidad_max)
        # Atributo específico de Auto
        self.cantidad_puertas = cantidad_puertas

    def describir(self):
        # Sobreescribimos describir() con información específica del auto
        print(f"[AUTO]  Marca: {self.marca} | "
              f"Vel. máx: {self.velocidad_max} km/h | "
              f"Puertas: {self.cantidad_puertas}")


# ── SUBCLASE: Moto ───────────────────────────────────────────
class Moto(Vehiculo):
    """Clase hija que representa una moto. Hereda de Vehiculo."""

    def __init__(self, marca, velocidad_max, tipo):
        # Llamamos al constructor de la clase madre
        super().__init__(marca, velocidad_max)
        # Atributo específico de Moto (ej: deportiva, cruiser, scooter)
        self.tipo = tipo

    def describir(self):
        # Sobreescribimos describir() con información específica de la moto
        print(f"[MOTO]  Marca: {self.marca} | "
              f"Vel. máx: {self.velocidad_max} km/h | "
              f"Tipo: {self.tipo}")


# ── PROGRAMA PRINCIPAL ───────────────────────────────────────
if __name__ == "__main__":

    # Creamos objetos de cada subclase
    auto1 = Auto(marca="Toyota", velocidad_max=180, cantidad_puertas=4)
    auto2 = Auto(marca="Ford", velocidad_max=200, cantidad_puertas=2)
    moto1 = Moto(marca="Honda", velocidad_max=220, tipo="Deportiva")
    moto2 = Moto(marca="Yamaha", velocidad_max=160, tipo="Scooter")

    # Creamos una lista con todos los vehículos (polimorfismo)
    # Aunque son objetos distintos, todos tienen el método describir()
    flota = [auto1, auto2, moto1, moto2]

    print("=" * 55)
    print("        SISTEMA DE TRANSPORTE - FLOTA DE VEHÍCULOS")
    print("=" * 55)

    # Recorremos la lista y llamamos a describir() en cada objeto
    # Python sabe automáticamente qué versión de describir() usar
    for vehiculo in flota:
        vehiculo.describir()

    print("=" * 55)
