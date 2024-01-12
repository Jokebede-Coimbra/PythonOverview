from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')
    

def main():
    casa = []    
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Lavar roupa'))
    casa.append(Tarefa('Arrumar quarto'))
    casa.append(Tarefa('Dobrar as roupas'))
    
    for i in casa:
        if i.descricao  == "Lavar prato":
            print(i.concluir())
    for tarefa in casa:
        print( f'- {tarefa}')  
                  
if __name__ == "__main__":
    main()  
       