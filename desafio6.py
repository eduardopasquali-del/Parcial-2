# Conversor de tempo simplificado
print("=== Conversor de Tempo ===")
opcao = input("Escolha a opção:\n1 - Segundos → horas/minutos/segundos\n2 - horas/minutos/segundos → segundos\nDigite 1 ou 2: ")

if opcao == "1":
    s = int(input("Digite o número de segundos: "))
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    print(f"{h} hora(s), {m} minuto(s) e {s} segundo(s)")

elif opcao == "2":
    h = int(input("Horas: "))
    m = int(input("Minutos: "))
    s = int(input("Segundos: "))
    total = h * 3600 + m * 60 + s
    print(f"Total em segundos: {total}")

else:
    print("Opção inválida!")
