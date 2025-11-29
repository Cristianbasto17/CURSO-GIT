print("=== VERIFICADOR DE PALÍNDROMOS ===\n")

texto = input("Ingresa una palabra o frase: ")

# Limpiar el texto: quitar espacios y convertir a minúsculas
texto_limpio = texto.replace(" ", "").lower()

# Verificar si es palíndromo
if texto_limpio == texto_limpio[::-1]:
    print(f"\n✓ '{texto}' SÍ es un palíndromo")
else:
    print(f"\n✗ '{texto}' NO es un palíndromo")

print(f"Al revés se lee: {texto_limpio[::-1]}")