#  [ expressão for item in list if condicinal ]
# Dentro dos [] tenho uma expressão que será responsável por gerar uma lista de acordo com a expressão
dobros = [i * 2 for i in range(1, 10)]
print(dobros)

# Versão "normal"
dobros2 = []
for i in range(1, 10):
    dobros2.append(i * 2)
    print(dobros2)