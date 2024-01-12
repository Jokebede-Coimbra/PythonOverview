class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome

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
    grokn = Neanderthal('Grokn')

    print(f'Evolução (a partir da classe):  {", ".join(HomoSapiens.especies())}')
    print()
    print(f'Evolução (a partir da instacia):  {", ".join(gabriel.especies())}')
    print()
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print()
    print(f'Gabriel evoluído? {gabriel.is_evoluido()}')
    print(f'Gronkn evoluído? {grokn.is_evoluido()}')
  