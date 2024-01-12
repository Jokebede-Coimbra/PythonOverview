from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
      return self.tarefas.__iter__()
      
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
         
    def pendentes(self):
        tarefa_pendentes = [tarefa for tarefa in self.tarefas if not tarefa.feito]
        return tarefa_pendentes

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas 
               if tarefa.descricao == descricao][0]
         
    def __str__(self):
        return f'{self.nome}\n({len(self.pendentes())} tarefa(s) pendente(s))'
             

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')
    
def imprimir_tarefas(projeto):
    teste = [tarefa for tarefa in projeto]
    return teste    
    

def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Lavar prato')
    casa.add('Lavar roupa')
    casa.add('Arrumar quarto')
    casa.add('Dobrar as roupas')
    print(casa)
    
    casa.procurar('Lavar roupa').concluir()
    imprimir_tarefas(casa)
    
    print(casa)
    
    print('===============================')
     
    
    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas')
    mercado.add('Carnes')
    print(mercado)
    
    mercado.procurar('Frutas').concluir()
    imprimir_tarefas(mercado)
    
    print(mercado) 
    
               
if __name__ == "__main__":
    main()  
             