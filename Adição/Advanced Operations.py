# Nome: Matheus de Paula Barros
# Série: 2 ano EM
# A versão mais simples pode ser encontrada aqui: https://github.com/S3EMi/Class1/blob/main/Adição/Simple%20Addition.py

# função para "pausar"
def pause():
    pauseProgram = input("Pressione a tecla ENTER para continuar")

# adicionar
def add(x, y):
    return x + y

# subtrair
def subtract(x, y):
    return x - y

# multiplicar
def multiply(x, y):
    return x * y

# dividir
def divide(x, y):
    return x / y

# escolher a operação
print("Escolha a operação.")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# verifique a escolha da alternativa e faça a operação
choice = input("Selecione a alternativa 1, 2, 3, 4: ")
if choice in ('1', '2', '3', '4'):

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

# verifica a escolha e faz a operação
if choice == '1':
  print(num1, " + ", num2, " = ", add(num1, num2))


elif choice == '2':
  print(num1, " - ", num2, " = ", subtract(num1, num2))

elif choice == '3':
  print(num1, " x ", num2, " = ", multiply(num1, num2))

elif choice == '4':
  print(num1, " / ", num2, " = ", divide(num1, num2))

else:
    print("Escolha inválida.")

pause()
