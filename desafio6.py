# Programa de conversão de tempo

print("=== Conversor de Tempo ===")
print("Escolha a opção:")
print("1 - Converter segundos em horas, minutos e segundos")
print("2 - Converter horas, minutos e segundos em segundos")

opcao = input("Digite 1 ou 2: ")

if opcao == "1":
    # Converter segundos em horas, minutos e segundos
    total_segundos = int(input("Digite o número de segundos: "))
    
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    
    print(f"{total_segundos} segundos correspondem a {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")

elif opcao == "2":
    # Converter horas, minutos e segundos em segundos
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    
    total_segundos = horas * 3600 + minutos * 60 + segundos
    
    print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s) correspondem a {total_segundos} segundos.")

else:
    print("Opção inválida! Digite 1 ou 2.")
