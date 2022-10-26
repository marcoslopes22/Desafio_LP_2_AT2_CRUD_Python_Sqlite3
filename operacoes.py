import sqlite3;

# ESCOLA TÉCNICA ESTADUAL PORTO DIGITAL;
# ALUNOS: MARCOS, LUCAS, VITÓRIA, GUILHERME, RAVEL, MAURO, MARCIO;
# DESENVOLVIMENTO DE SISTEMAS - MÓDULO II;
# DISCIPLINA: LÓDIGA DE PROGRAMAÇÃO - PROFESSOR: CLOVIS ROCHA;

# ATIVIDADE: CRUD COM PYTHON E SQLITE3;

class Operacoes:

    tituloColeta = str();
    pontoColeta = str();
    dataCriacao = str();
    nomeCidadao = str();
    descricaoColeta = str();
    status = str();

    # CONSTRUTOR, CRIAÇÃO E CONEXÃO COM O BANCO DE DADOS;
    def __init__(self):
        try: 
            self.__conn = sqlite3.connect('coleta_db.db');
            self.__cur = self.__conn.cursor();
            self.criarTabela();
        except:
            print("Erro na conexão!");

    # CRIAR TABELA SE A MESMA NÃO EXISTIR;
    def criarTabela(self):
        try:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS oportunidades_coleta (
                id INTEGER PRIMARY KEY, 
                titulo_coleta VARCHAR(50) NOT NULL, 
                ponto_coleta VARCHAR(100) NOT NULL,
                data_criacao VARCHAR(50) NOT NULL,
                nome_cidadao VARCHAR(50) NOT NULL,
                descricao_coleta VARCHAR(1000) NOT NULL,
                status VARCHAR(50) NOT NULL)
                ''');
            self.__conn.commit();
        except:
            print("Erro ao tentar criar tabela!");

    # CADASTRAR;
    def cadastrar(self):
        self.__cur.execute(f'''INSERT INTO oportunidades_coleta (
            titulo_coleta,ponto_coleta,data_criacao,nome_cidadao,descricao_coleta,status
            ) VALUES (
            '{self.tituloColeta}','{self.pontoColeta}','{self.dataCriacao}','{self.nomeCidadao}','{self.descricaoColeta}','{self.status}'
            )''');
        self.__conn.commit();

    # LER;
    def ler(self):
        self.__cur.execute(f"SELECT * FROM oportunidades_coleta ORDER BY id");
        self.__conn.commit();
        result = self.__cur.fetchall();
        print("=====================================================================");
        print("\nPONTOS DE COLETAS:\n");
        for i in result: print(f"ID: {i[0]}, Título do Ponto: {i[1]}, Nome do Ponto: {i[2]}, Data de Criação: {i[3]}, Nome do Responsável: {i[4]}, Descrição: {i[5]}, Status: {i[6]}");
        print("\n");
    
    # VERIFICAR SE HÁ REGISTROS NA LISTA;  
    def verificarLista(self):
        self.__cur.execute("SELECT * FROM oportunidades_coleta");
        self.__conn.commit();
        result = self.__cur.fetchall();
        if result == []: return False;
        elif result != []: return True;

    # ATUALIZAR;
    def atualizar(self,idRegistro):
        self.__cur.execute(f'''UPDATE oportunidades_coleta SET 
            titulo_coleta='{self.tituloColeta}', 
            ponto_coleta='{self.pontoColeta}',
            data_criacao='{self.dataCriacao}',
            nome_cidadao='{self.nomeCidadao}',
            descricao_coleta='{self.descricaoColeta}',
            status='{self.status}'
        WHERE id='{idRegistro}';''');
        self.__conn.commit();

    # DELETAR;
    def deletar(self,idRegistro):
        self.__cur.execute(f"DELETE FROM oportunidades_coleta WHERE id='{idRegistro}'");
        self.__conn.commit();
    
    # PESQUISAR;
    def pesquisar(self):
        self.__cur.execute(f'''SELECT * FROM oportunidades_coleta 
            WHERE titulo_coleta='{self.tituloColeta}' AND 
            ponto_coleta='{self.pontoColeta}' AND
            data_criacao='{self.dataCriacao}' AND
            nome_cidadao='{self.nomeCidadao}' AND
            descricao_coleta='{self.descricaoColeta}' AND
            status='{self.status}';''');
        self.__conn.commit();
        result = self.__cur.fetchall();
        if result == []: return False;
        elif result != []: return result;

    # PESQUISAR PELO NÚMERO DE CADASTRO DO PONTO DE COLETA;
    def pesquisarID(self,idRegistro):
        self.__cur.execute(f"SELECT * FROM oportunidades_coleta WHERE id='{idRegistro}'");
        self.__conn.commit();
        result = self.__cur.fetchall();
        if result == []: return False;
        elif result != []: return result;