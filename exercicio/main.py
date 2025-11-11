class colecao:
    def __init__(self):
        self.nome = ['Renan','Bruna','Amanda','Thiago','Matheus']
        self.numero = {1,2,3,4,5}
        pass

    def exercicio1(self):
        self.nome.append('Miguel')
        print(self.nome)

    def exercicio2(self):
        self.numero.add(6)
        print(self.numero)

    def exercicio3(self,posicao):
        self.frutas.insert(posicao,'damasco')
        print(self.frutas)
    

if __name__ == "__main__":
    c = colecao()

    c.exercicio1()
    c.exercicio2()