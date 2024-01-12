#  [ expressão for item in list if condicional ]
# Dentro dos [] tenho uma expressão que será responsável por gerar uma lista de acordo com a expressão
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print (dobros_dos_pares)

# Versão "normal"
dobros_dos_pares2 = []
for i in range(10):
    if i % 2 == 0:
       dobros_dos_pares2.append(i * 2)
print (dobros_dos_pares2)