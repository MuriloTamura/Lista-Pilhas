def gerar_codigo(expressao):
    pilha = []
    temp_count = 0

    for simbolo in expressao:
        if simbolo.isalpha():  # Operando (A, B, C...)
            pilha.append(simbolo)
        else:  # Operador
            op2 = pilha.pop()
            op1 = pilha.pop()
            temp_count += 1
            temp = f"TEMP{temp_count}"

            if simbolo == '+':
                print(f"LD {op1}")
                print(f"AD {op2}")
            elif simbolo == '-':
                print(f"LD {op1}")
                print(f"SB {op2}")
            elif simbolo == '*':
                print(f"LD {op1}")
                print(f"ML {op2}")
            elif simbolo == '/':
                print(f"LD {op1}")
                print(f"DV {op2}")

            print(f"ST {temp}")
            pilha.append(temp)

    # No final, o resultado está no último TEMP
    print(f"# Resultado final em {pilha[-1]}")
    