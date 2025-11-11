#CONJUNTOS
#um conjunto é uma coleção nao ordenada, sem indice, que nao aceita valores repetidos

numeros ={1,2,8,3,5}
print(numeros)
#add um item
numeros.add(6)
print(numeros)

#removendo um item
numeros.remove(8)
print(numeros)

print(10 in numeros)

#DICIONARIOS
aluno ={
    "nome" :"Ricardo",
    "idade" : 10,
    "curso" : "informática"

}

pc ={
    "placaMae" : "B450",
    "processador" : "Ryzen5",
    "qntMemoriaRam" :"16gb",
    "armazenamento" : "1TB",
    "placaDeVideo" : "RTX5090"


}
#Como acesso o valor de um dicionario
print(pc["placaDeVideo"])

#adicionando uma nova chave

pc["fonte"] = "500w"
print(pc)
#atualizar uma nova chance

pc["placaMae"] = "8550"
print(pc)

#Remover uma chave
pc.pop("qntMemoriaRam")
print(pc)
 