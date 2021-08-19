# Nome: Matheus Barros
# Série: 1 ano EM

def pause():
    pause = input("Pressione ENTER para continuar")

n1 = (input("Primeiro Número: "))
n2 = (input("Segundo Número: "))

# Dar um erro bem mais simplificado se o valor dado não for um número
# Verifica se os números são inteiros ou decimais, se não, retorna com um erro e fecha o programa
try:
    int(n1), int(n2)
except ValueError:
    try:
        float(n1), float(n2)
    except ValueError:
        print("Um ou mais valores dados não foram identificados.")
        pause()
        exit()

add = float(n1) + float(n2)
print("A soma é: ", add)
pause()
