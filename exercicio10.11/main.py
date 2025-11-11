#Crie um programa em Python que calcule a média final de um aluno.
#Para isso, peça ao usuário que digite duas notas (as notas podem conter casas
#decimais). Em seguida, exiba o resultado da média com uma mensagem explicativa.



def media():
    try:
        print("______________exercicio 1____________")
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        media_final = (nota1 + nota2) / 2
        print(f"A média final do aluno é: {media_final:.2f}")
        print("_____________________________________")
    except Exception as e:
        print(f"Erro em calcular a média {e}")


#Crie um programa em Python que peça ao usuário o valor do produto e a
#quantidade comprada. Ao final, mostre o total a pagar no console.

def venda():
    try:
        print("______________exercicio 2____________")
        Valor_produto = float(input('Informe o valor do produto: '))
        Qtd_produto = int(input('Informe a quantidade comprada: '))
        Valor_total = Valor_produto * Qtd_produto
        print(f'Valor total é: {Valor_total}R$')
        print("_____________________________________")
    except Exception as e:
        print(f"Erro ao calcular o valor total dos produtos: {e}")

#Crie um programa em Python que peça dois números ao usuário e mostre a
#diferença entre eles no console com uma mensagem explicativa.

def diferenca():
    try:
        print("______________exercicio 3____________")
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        diferenca = (num1 - num2)
        print(f"A diferença entre os números é: {diferenca}")
        print("_____________________________________")
    except Exception as e:
        print(f"Erro ao calcular a diferença: {e}")


#Crie um programa em Python que peça um número ao usuário e mostre:
#O dobro do número
#O triplo do número
#E se ele é ímpar ou par, usando o resto da divisão dele por 2 para saber.

def numero():
    try:
        print("______________exercicio 4____________")
        num = int(input('Informe um número: '))
        dobro = num *2
        print(f"O dobro desse número é: {dobro}")
        triplo = num *3
        print(f"O triplo desse número é: {triplo}")
        ParImpar = num % 2
        if ParImpar == 0:
            print("Esse número é Par")
        else:
            print("Esse número é Impar")

        print("_____________________________________")
    except Exception as e:
        print(f"Erro {e}")

if __name__ == "__main__":
    media()
    venda()
    diferenca()
    numero()