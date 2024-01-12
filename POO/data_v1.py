class Data:
  
    def __str__(self):
     return f'{self.dia}/{self.mes}/{self.ano}'
 
d1 = Data()
d1.dia = 24
d1.mes = 8
d1.ano = 2023
print(d1)

d2 = Data()
d2.dia = 21
d2.mes = 11
d2.ano = 2024
print(d2)