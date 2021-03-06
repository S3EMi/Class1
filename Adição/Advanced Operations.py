# Nome: Matheus de Paula Barros
# Série: 2 ano EM
# A versão mais simples pode ser encontrada aqui: https://github.com/S3EMi/Class1/blob/main/Adição/Simple%20Addition.py

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

import math as mt

def restart():
  def gotor():
    if pause() == "":
      clearConsole()
      restart()
    else:
      clearConsole()
      restart()

  def pause():
      input("\nPressione a tecla ENTER para continuar...")

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
  print("\n\nEscolha a operação.")
  print("1. Adicionar")
  print("2. Subtrair")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Calcular Bhaskara")

  # verifique a escolha da alternativa e faça a operação
  choice = input("\nSelecione a alternativa 1, 2, 3, 4, 5: ")
  if choice in ('1', '2', '3', '4'):
    num1 = input("\nDigite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

  # verifica se o valor dado é um número ou não
    try:
      float(num1), float(num2)
    except ValueError:
      print("\nUm ou mais valores não foram identificados como números, se você quer usar decimais utilize '.' e não ','")
      gotor()

  # verifica a escolha e faz a operação
  if choice == '1':
    print(num1, " + ", num2, " = ", add(float(num1), float(num2)))
    gotor()

  elif choice == '2':
    print(num1, " - ", num2, " = ", subtract(float(num1), float(num2)))
    gotor()

  elif choice == '3':
    print(num1, " x ", num2, " = ", multiply(float(num1), float(num2)))
    gotor()

  elif choice == '4':
    print(num1, " / ", num2, " = ", divide(float(num1), float(num2)))
    gotor()
    
  elif choice == '5':

    a = input("Primeiro número (a): ")
    b = input("Segundo número (b): ")
    c = input("Terceiro número (c): ")
    try:
        float(a), float(b), float(c)
    except ValueError:
        print("Um ou mais valores dados não foram identificados")
        gotor()
    a = float(a)
    b = float(b)
    c = float (c)
    disc = (b**2 - 4*a*c)
    try:
        res1 = (-b - mt.sqrt(disc))/(2*a)
        res2 = (-b + mt.sqrt(disc))/(2*a)
    except ZeroDivisionError:
        print("Erro: não é possível dividir por 0")
        gotor()
    except ValueError:
        print("Erro de domínio matemático")
        gotor()

    print("\nx' = ", res1)
    print("x'' = ", res2)
    gotor()

restart()
