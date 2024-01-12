class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderxxxx'        
        
if __name__ == '__main__':
    gabriel = Humano('Gabriel')        
    pedro = Humano('Pedro')
    pedro.das_cavernas()
    
    print(f'Humano.especie: {Humano.especie}')
    print(f'Humano.especie: {pedro.especie}')
    print(f'Humano.especie: {gabriel.especie}')