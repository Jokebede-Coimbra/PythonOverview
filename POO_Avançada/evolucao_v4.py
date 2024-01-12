class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome
        self._idade = None
    
    @property    
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número psitivo')
        self._idade = idade
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderxxxx'     
        
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
            
if __name__ == '__main__':
    
    gabriel = HomoSapiens('Gabriel')  
    gabriel.idade = 40  

    print(f'Nome: {gabriel.nome}, Idade: {gabriel.idade}')
    
  