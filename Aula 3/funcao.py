
class Loop:
    def __init__(self):
        pass

    def reverse(self):
        num = 20
        while num >= 0:
            print(num)
            num -= 1
    
    def palavra(self):
        palavra = input("Qual meu nome ? ")

        while(palavra != "renan"):
            print("Não é esse")
            palavra = input("Qual meu nome ? ")
        
        print("Acertou!!")

    
    def exercicio1(self):
        num = 5
        while num <= 15:
            print(num)
            num += 1
    
    def exercicio2(self):
        palavra = input("Qual a senha: ")

        while(palavra != "1234"):
            print("Não é esse")
            palavra = input("Qual a senha:  ")
        
        print("Acertou!!")

    def exercicio3(self):
        soma = 0
        while True:
            num = int(input("Digite um número ou 0 para sair: "))
            if num == 0:
                break
            soma += num
            print(soma)
    