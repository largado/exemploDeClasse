
#criando a classe
class Moto:
    #atributos da classe
    def __init__(self):
        self.marca = "honda"
        self.modelo = "xlr125"
        self.cor = "Azul"

    def Andar(self):
        print("a moto andou agora")



#instanciando a classe , como se tivesse criando o objeto no java
minhaMoto = Moto()

#acessando atributo da classe que já foi instanciada
print(minhaMoto.cor)



#executando o método da classe instanciada
minhaMoto.Andar()
