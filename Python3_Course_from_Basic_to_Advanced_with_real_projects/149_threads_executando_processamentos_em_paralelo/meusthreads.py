from time import sleep
from threading import Thread
from threading import Lock

# Cada thread executa uma tarefa ou processo

"""
# 1 maneira de usar
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        # Chamamos o init() da Thread
        # Thread.__init__() # outra maneira de chamar a Thread
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()  # inicia a execução da Thread

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
# 2 maneira de usar
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

"""
# 3 maneira de usar
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()
t1.join()  # Se junta a thread principal, espera ela acabar para exibir algo.

while t1.is_alive():
    print('Esperando a thread!')
    sleep(2)

print('Thread acabou!')
"""


# Possível problema que poderia ocorrer usando Threads
# Este problema poblema poderia ocorrer devido a falta de sincronia

class Ingressos:

    'Classe que vende ingressos'

    def __init__(self, estoque):
        " Inicializando..."
        ""
        " :param estoque: quantidade de ingressos em estoque "

        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade):
        " Compra determinada quantidade de ingressos "

        " : param quantidade: A quantidade de ingressos que deseja comprar "
        " : type quantidade: int "
        " : return: Nada "
        " : rtype: None "

        # Tranca o método após uma solicitação
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método após executar e sai.
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(
            f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque.')

        # Libera o método (para trancar a liberação de todas as solicitações simultâneas)
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram
    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)
