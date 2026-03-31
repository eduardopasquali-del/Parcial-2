# Calculadora simples em Python

print("Bem-vindo à calculadora simples!")

# Solicita o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita a operação
print("Escolha a operação:")
print(" +  para adição")
print(" -  para subtração")
print(" *  para multiplicação")
print(" /  para divisão")
operacao = input("Digite a operação: ")

# Executa a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)
