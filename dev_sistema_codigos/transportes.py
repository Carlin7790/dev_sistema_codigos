class Transporte:
    def __init__(self, capacidade, velocidade_maxima):
        self.__capacidade = capacidade
        self.__velocidade= velocidade_maxima

    def getCapacidade(self): 
        return self.__capacidade   
    def getVelocidade_Maxima(self):
        return self.__velocidade

    def descricao(self):
        print(f'A capacidade do transporte e {self.getCapacidade()}, e a velocidade maxima {self.getVelocidade_Maxima()}KM/H')
    def mover(self):
        print('O transporte esta em movimento')
tr1 = Transporte(50,200)
tr1.descricao()
tr1.mover()

class Onibus(Transporte):
    def __init_subclass__(self, capacidade, velocidade_maxima):
        super().__init__(capacidade,velocidade_maxima)
    def mover(self):
        print('O onibus esta seguindo sua rota')


class Bicicleta(Transporte):
    def __init_subclass__(self, capacidade, velocidade_maxima):
        super().__init__(capacidade,velocidade_maxima)
    def mover(self):
        print('A bicicleta esta sendo pedalada')
on1 = Onibus(40,120)
on1.descricao()
on1.mover()
bi1 = Bicicleta(1,30)
bi1.mover()
bi1.descricao()
  
  



