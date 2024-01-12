from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
      return self.tarefas.__iter__()
      
    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))
         
    def pendentes(self):
        tarefa_pendentes = [tarefa for tarefa in self.tarefas if not tarefa.feito]
        return tarefa_pendentes

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas 
               if tarefa.descricao == descricao][0]
         
    def __str__(self):
        return f'{self.nome}\n({len(self.pendentes())} tarefa(s) pendente(s))'
             

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        status = []
        if self.feito:
            status.append('>>> Concluída <<<')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('>>> Vencida <<<')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'Vence em {dias} dias')
        return f'{self.descricao} >>> ' + ' ' .join(status)
    
    
def imprimir_tarefas(projeto, vencimento=None):
   for tarefa in projeto:
        if vencimento is None or (tarefa.vencimento and tarefa.vencimento == vencimento):
            print(tarefa)
   return tarefa  

def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Lavar prato', datetime.now() + timedelta(days=2, minutes=12))
    casa.add('Lavar roupa')
    casa.add('Arrumar quarto', datetime.now())
    casa.add('Dobrar as roupas')
    print(casa)
    
    casa.procurar('Lavar roupa').concluir()
    imprimir_tarefas(casa)
    
    print(casa)
    
    print('===============================')
     
    
    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas')
    mercado.add('Carnes', datetime.now() + timedelta(days=5, minutes=12))
    print(mercado)
    
    mercado.procurar('Frutas').concluir()
    imprimir_tarefas(mercado)
    
    print(mercado) 
    
               
if __name__ == "__main__":
    main()  
             