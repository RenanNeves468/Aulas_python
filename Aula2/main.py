from loop import Loop

def main():
    l = Loop()
    # numero = 100
    # num = l.Numeros2(numero)
    # for items in num:
    #     logger.info(f'numero: {items[0]}')
    #l.Tabuada(5)

    nomes = ['Renan','Felipe','Bruno','Thiago','Jefferson']
    print("___________________Exercicio 01______________________")
    l.Exercicio1(nomes)
    print("___________________Exercicio 02______________________")
    palavra = input('Digite uma palavra: ')
    print(l.Exercicio2(palavra))
    print("___________________Exercicio 03______________________")
    print(l.Exercicio3())




if __name__ == "__main__":
    main()
