class Data:
    def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano
 
    def __str__(self):
     return f'{self.dia}/{self.mes}/{self.ano}'
 
d1 = Data(24, 5, 2023)
# d1.dia = 24
# d1.mes = 8
# d1.ano = 2023
print(d1)

d2 = Data(21, 11, 2024)
# d2.dia = 21
# d2.mes = 11
# d2.ano = 2024
print(d2)