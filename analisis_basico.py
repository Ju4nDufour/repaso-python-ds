# ==========================================
# TAREA 1: Definición de Variables y f-strings
# ==========================================

# Variables con tipos de datos nativos
nombre_producto = "Notebook Pro"  # str
precio_unitario = 1250.50          # float
stock_disponible = 8               # int
tiene_descuento = True             # bool

# Resumen formateado utilizando f-string
resumen_producto = (
    f"Producto: {nombre_producto} | "
    f"Precio: ${precio_unitario:.2f} | "
    f"Stock: {stock_disponible} unidades | "
    f"Descuento: {'Sí' if tiene_descuento else 'No'}"
)

print("--- TAREA 1: Resumen de Producto ---")
print(resumen_producto)
print()


# ==========================================
# TAREA 2: Lógica de Negocio (Bucles + Condicional)
# ==========================================

precios = [45.0, 120.5, 89.9, 210.0, 100.0]

print("--- TAREA 2: Clasificación de Precios ---")
for precio in precios:
    # Clasificación según el umbral de 100
    if precio > 100:
        print(f"${precio:.2f} -> Caro")
    else:
        print(f"${precio:.2f} -> Económico")
print()


# ==========================================
# TAREA 3: Estructura de Datos (Diccionarios)
# ==========================================

# Diccionario inicial con pares producto: stock
almacen = {
    "Notebook Pro": 8,
    "Mouse Gamer": 12,
    "Teclado Mecánico": 5
}

# Inserción de un nuevo producto
almacen["Monitor 24"] = 6

print("--- TAREA 3: Gestión de Almacén ---")
# Consulta de stock de un producto específico
producto_consulta = "Notebook Pro"
stock_consultado = almacen.get(producto_consulta, 0)
print(f"Stock disponible de '{producto_consulta}': {stock_consultado}")
print("Inventario completo:", almacen)
print()


# ==========================================
# TAREA 4: Modularización con Funciones
# ==========================================

def resumen_estadistico(numeros):
    """
    Calcula la suma total, el promedio y la cantidad de elementos de una lista numérica.
    Retorna un diccionario con las métricas calculadas.
    """
    # Control de lista vacía para evitar ZeroDivisionError
    if not numeros:
        return {
            "total": 0,
            "promedio": 0.0,
            "cantidad": 0
        }
    
    total = sum(numeros)
    cantidad = len(numeros)
    promedio = total / cantidad
    
    return {
        "total": total,
        "promedio": promedio,
        "cantidad": cantidad
    }


# Llamada de prueba
datos_muestra = [10, 20, 30, 40, 50]
resultado_metricas = resumen_estadistico(datos_muestra)

print("--- TAREA 4: Resumen Estadístico ---")
print("Lista analizada:", datos_muestra)
print("Resultado:", resultado_metricas)
