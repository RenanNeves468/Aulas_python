class colecao:
    def __init__(self):
        self.frutas = ['banana','maracujá','tomate','goiaba','manga']
        pass

    def lista(self):
        print(self.frutas)

    def adicionar(self):
        self.frutas.append('uva')
        print(self.frutas)

    def inserir(self,posicao):
        self.frutas.insert(posicao,'damasco')
        print(self.frutas)
    
    def remover(self):
        self.frutas.pop(3)
        print(self.frutas)
    
    def exibir(self,posicao):
        print(self.frutas[posicao])
        

class conjunto:
    def __init__(self):
        self.numeros = {1,2,8,3,5}
        pass

    def exibir(self):
        print(self.numeros)

    def adicionar(self,numero):
        self.numeros.add(numero)
        print(self.numeros)

    def excluir(self,posicao):
        self.numeros.remove(posicao)
        print(self.numeros)

    def verificar(self,num):
        print(num in self.numeros)


def main_lista():
    c = colecao()

    c.lista()
    c.adicionar()
    c.inserir(0)
    c.remover()
    c.exibir(2)

def main_conjunto():
    c = conjunto()

    c.exibir()
    c.adicionar(3)
    c.excluir(1)
    c.verificar(5)

if __name__ == "__main__":
    main_lista()
    main_conjunto()