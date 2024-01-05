import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()
    # Após mudar a configuracao no programa (Database Structure/modifyTable/ em Telefone selecionar U)
    # Acrescentamos OR IGNORE para não gerar erro e também não acrescentar telefones repetidos

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('164_python_sqlite3_+_db_browser_for_sqlite/agenda.db')
    # Será inserida uma nova linha na tabela agenda criada no programa DB Browser for sqlite
    # agenda.inserir('Wellington', '1111111')
    # agenda.inserir('Maria', '1111114')
    # agenda.inserir('João', '1111113')
    # agenda.inserir('Renata', '1111112')
    # agenda.editar('João', '2222222', id=22)
    agenda.inserir('Luiz Otávio', '123456')
    agenda.excluir(22)
    agenda.listar()
    agenda.buscar('luiz')
