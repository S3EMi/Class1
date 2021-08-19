def pause():
    pause = input("Pressione ENTER para continuar")

n1 = (input("Primeiro Número: "))
n2 = (input("Segundo Número: "))
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