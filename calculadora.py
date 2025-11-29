while True:
    print("\n=== CALCULADORA ===")
    print("Operaciones: +, -, *, /, ** (potencia)")
    
    operacion = input("Ingresa operación (o 'salir'): ")
    
    if operacion.lower() == 'salir':
        break
    
    try:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
        
        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            print(f"Resultado: {num1 / num2}" if num2 != 0 else "Error: División por cero")
        elif operacion == '**':
            print(f"Resultado: {num1 ** num2}")
        else:
            print("Operación no válida")
    except:
        print("Error: Ingresa números válidos")