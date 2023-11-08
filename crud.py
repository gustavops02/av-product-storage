import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="", host="localhost",port="5432",database="av-python")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
    
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            query = """ INSERT INTO public."PRODUTO"("CODIGO", "NOME", "PRECO", "PRECO_AJUSTADO") VALUES (%s,%s,%s,%s)"""
            preco_ajustado = preco + (preco * 0.1)
            record_to_insert = (codigo, nome, preco, preco_ajustado)
            cursor.execute(query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # closing database connection.
            if(self.connection):
                cursor.close()
                self.connection.close()

    def getDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            query = """SELECT * FROM public."PRODUTO"; """
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except (Exception, psycopg2.Error) as error:
            print('Falha ao consultar os dados')
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            query = """Update public."PRODUTO" set "NOME" = %s,"PRECO" = %s, "PRECO_AJUSTADO" = %s where "CODIGO" = %s"""
            preco_ajustado = preco + (preco* 0.1)
            cursor.execute(query, (nome, preco, preco_ajustado, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."PRODUTO" where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """DELETE FROM public."PRODUTO" where "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo, ))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:    
            print("Erro na Exclusão", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
