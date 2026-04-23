# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Lautaro Cazon
# Ejercicio N°: 2
# Fecha de entrega: 23/04/2026

# ============================================================
# EJERCICIO: Figuras geométricas con herencia y polimorfismo
# ============================================================

import math  # Necesario para usar el valor de PI (math.pi)


# ── CLASE BASE ───────────────────────────────────────────────
class Figura:
    """Clase madre que representa una figura geométrica genérica."""

    def __init__(self, color):
        # Atributo común a todas las figuras
        self.color = color

    def area(self):
        # Método base: retorna 0. Cada subclase lo sobreescribirá
        # con su propia fórmula.
        return 0

    def describir(self):
        # Este método está en la clase MADRE pero llama a self.area()
        # Gracias al polimorfismo, Python usará el area() correcto
        # según el objeto real (Rectangulo o Circulo)
        print(f"Figura de color '{self.color}' | Área: {self.area():.2f}")


# ── SUBCLASE: Rectangulo ─────────────────────────────────────
class Rectangulo(Figura):
    """Clase hija que representa un rectángulo. Hereda de Figura."""

    def __init__(self, color, base, altura):
        # Heredamos el atributo color de la clase madre
        super().__init__(color)
        # Atributos específicos del rectángulo
        self.base = base
        self.altura = altura

    def area(self):
        # Sobreescribimos area() con la fórmula del rectángulo
        # Área = base × altura
        return self.base * self.altura

    def describir(self):
        # Sobreescribimos describir() con información específica
        print(f"[RECTÁNGULO] Color: {self.color} | "
              f"Base: {self.base} | Altura: {self.altura} | "
              f"Área: {self.area():.2f}")


# ── SUBCLASE: Circulo ────────────────────────────────────────
class Circulo(Figura):
    """Clase hija que representa un círculo. Hereda de Figura."""

    def __init__(self, color, radio):
        # Heredamos el atributo color de la clase madre
        super().__init__(color)
        # Atributo específico del círculo
        self.radio = radio

    def area(self):
        # Sobreescribimos area() con la fórmula del círculo
        # Área = π × radio²
        return math.pi * (self.radio ** 2)

    def describir(self):
        # Sobreescribimos describir() con información específica
        print(f"[CÍRCULO]    Color: {self.color} | "
              f"Radio: {self.radio} | "
              f"Área: {self.area():.2f}")


# ── PROGRAMA PRINCIPAL ───────────────────────────────────────
if __name__ == "__main__":

    # Creamos objetos de cada subclase
    rect1 = Rectangulo(color="rojo",  base=10, altura=5)
    rect2 = Rectangulo(color="azul",  base=7,  altura=3)
    circ1 = Circulo(color="verde",    radio=6)
    circ2 = Circulo(color="amarillo", radio=4)

    # Lista de figuras mezcladas (polimorfismo)
    figuras = [rect1, rect2, circ1, circ2]

    print("=" * 55)
    print("         SISTEMA DE FIGURAS GEOMÉTRICAS")
    print("=" * 55)

    # Recorremos la lista y llamamos describir() en cada figura.
    # Python sabe automáticamente qué versión usar según el objeto.
    for figura in figuras:
        figura.describir()

    print("=" * 55)

    # ── Verificación extra: polimorfismo con área desde clase madre
    # Creamos una figura genérica para demostrar que area() base retorna 0
    print("\n── Verificación polimorfismo con clase base ──")
    figura_generica = Figura(color="gris")
    figura_generica.describir()  # Debe mostrar área = 0.00
