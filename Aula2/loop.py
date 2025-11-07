

class Loop:
    def __init__(self):
        pass

    def Numeros(self,numero):
        try:
            for i in range(numero):
                return i
        except Exception as e:
            print(f'Erro {e}')

    def Numeros2(self,numero):
        return [(i,) for i in range(1, numero + 1)]
    
    def Tabuada(self,numero):
        try:
            for i in range(1,11):
                print(f'{numero} X {i} = {(numero * i)}')

        except Exception as e:
            print(f'Erro na função Tabuada: {e}')


    def Exercicio1(self,nomes):
        try:
            for item in nomes:
                print(item)
        except Exception as e:
            print(f'Erro na função Exercicio1: {e}')
    
    def Exercicio2(self,palavra):
        contador = 0
        try:
            vogais = 'aeiouAEIOU'
            for letra in palavra:
                if letra in vogais:
                    contador += 1
            return contador
        except Exception as e:
            print(f'Erro: {e}')

    def Exercicio3(self):
        try:
            lista_numeros = [5,8,2,10,1]
            soma = sum(lista_numeros)
            return soma
        except Exception as e:
            print(f'Erro: {e}')