# Nome: Matheus de Paula Barros
# Série: 2 ano EM
# A versão mais simples pode ser encontrada aqui: https://github.com/S3EMi/Class1/blob/main/Adição/Simple%20Addition.py


# função para "pausar"
def pause():
    pauseProgram = input("\nPressione a tecla ENTER para continuar")

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
print("\nEscolha a operação.")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# verifique a escolha da alternativa e faça a operação
choice = input("\nSelecione a alternativa 1, 2, 3, 4: ")
if choice in ('1', '2', '3', '4'):
  num1 = input("\nDigite o primeiro número: ")
  num2 = input("Digite o segundo número: ")

# verifica se o valor dado é um número ou não
  try:
    float(num1), float(num2)
  except ValueError:
    print("\nUm ou mais valores não foram identificados como números, se você quer usar decimais utilize '.' e não ','")
    pause()
    exit()

# verifica a escolha e faz a operação
if choice == '1':
  print(num1, " + ", num2, " = ", add(float(num1), float(num2)))


elif choice == '2':
  print(num1, " - ", num2, " = ", subtract(float(num1), float(num2)))

elif choice == '3':
  print(num1, " x ", num2, " = ", multiply(float(num1), float(num2)))

elif choice == '4':
  print(num1, " / ", num2, " = ", divide(float(num1), float(num2)))

else:
    print("Escolha inválida.")

pause()
