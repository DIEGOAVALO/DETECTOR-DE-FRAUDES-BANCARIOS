# 1. NUESTROS DATOS (Conceptos de transferencias recientes)
transferencias = [
    "Pago de la colegiatura del mes de mayo",                          # Aprobado (Legítimo)
    "Compra de sustancias sospechosas y armas ilegales",               # Alerta (Fraude)
    "Transferencia a mi hermano por la cena de ayer",                  # Aprobado (Legítimo)
    "Inversión en negocios prohibidos por la ley",                     # Alerta (Fraude)
    "Pago de renta del departamento e internet",                       # Aprobado (Legítimo)
    "Para la clonación de tarjetas de crédito",                        # Alerta (Fraude)
    "Aquí tienes el dinero de las sustancias para el laboratorio",     # Alerta (Fraude)
    "Reembolso por el boleto del concierto",                           # Aprobado (Legítimo)
    "Broma entre amigos: pago por el cargamento ilegal",               # Alerta (Falso positivo por broma)
    "Compra de figuras de colección Star Wars: El ataque de los clones"# Alerta (Falso positivo por palabra 'clon')
]

# 2. NUESTRO MODELO (Palabras de alerta del sistema financiero)
alertas_fraude = ["armas", "ilegal", "prohibidos", "sustancias", "clonación", "clon"]

def modelo_ia_banco(concepto):
    concepto_minuscula = concepto.lower()
    
    # El modelo analiza si la transacción es segura o de riesgo
    for palabra in alertas_fraude:
        if palabra in concepto_minuscula:
            return "ALERTA (Posible Fraude / Cuenta Congelada)" # Predicción 1
            
    return "APROBADO (Transacción Exitosa)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- DETECTOR DE FRAUDES BANCARIOS ---")
for i, concepto in enumerate(transferencias, 1):
    prediccion = modelo_ia_banco(concepto)
    print(f"Transacción {i}: '{concepto}' -> RESULTADO: {prediccion}")
