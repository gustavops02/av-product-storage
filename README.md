![Python](https://img.shields.io/badge/Python-fff?style=for-the-badge&logo=python&logoColor=yellow)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Colaboradores: **Gustavo Paulo da Silva** e **Victor Abadia do Nascimento**


## Estoque de Produtos 

### Primeira etapa do RAD - Levantamento de Requisitos

Nesta primeira etapa, foi feita uma modelagem UML para definir como será a entidade do banco de dados.

O sistema realizará um serviço de CRUD completo. onde terá os seguintes campos: <br><br>
<img width="300" src="https://github.com/gustavops02/av-product-storage/assets/87784023/120b1278-adac-4e1f-bd87-4434aa1a2d01">

<hr>
O Valor ajustado será uma taxa de 10% do valor do produto

### Segunda etapa do RAD - Protótipo

Na segunda etapa, foi elaborado o protótipo (a tela com o tkinter) para a visualização detalhada do projeto.

<img width="500" src="https://github.com/gustavops02/av-product-storage/assets/87784023/2e147195-1355-45a7-8e81-8ff2ecf19c37"/>

<img width="500" src="https://github.com/gustavops02/av-product-storage/assets/87784023/6179396f-fd1b-4ac3-b44c-2195dc23958a" />

Onde o preço ajustado é definido automaticamente em uma coluna separada, preservando a normalização e a integridade dos dados.

### Terceira etapa - Construção do código

Este código é uma função que cria uma conexão com um banco de dados PostgreSQL usando a biblioteca psycopg2.
Onde:


#### Arquivo crud.py (classe AppBD)


```python
def create_connection():

  try:
  # Tenta estabelecer uma conexão com o banco de dados PostgreSQL
  
    connection = connector.connect(dbname='av-python', user='postgres', port='5432', host='localhost')
    return connection
  
  # Retorna a conexão bem-sucedida
  except connector.Error as err:
    print("database error: ", err)
  
  return connection # Retorna 'None' se a conexão falhar

def inserirDados(self, codigo, nome, preco): # Pega os campos como parâmetro para a criação do campo
       
    try: 
        self.abrirConexao() # Abre a conexão e inicializa o cursor
        cursor = self.connection.cursor()

        query = """ INSERT INTO public."PRODUTO"("CODIGO", "NOME", "PRECO", "PRECO_AJUSTADO") VALUES (%s,%s,%s,%s)"""
        # Implementação do requisito do preço ajustado, onde é incrementado 10% do seu valor.
        preco_ajustado = preco + (preco * 0.1)

        # roda a query com os campos passados por parâmetro e implementados manualmente (preço ajustado)
        record_to_insert = (codigo, nome, preco, preco_ajustado)
        cursor.execute(query, record_to_insert)
        self.connection.commit()
        count = cursor.rowcount # retorna a quantidade de linhas manipuladas após operações no banco de dados.
        print (count, "Registro inserido com successo na tabela PRODUTO")
    except (Exception, psycopg2.Error) as error:
        if(self.connection):
            print("Falha ao inserir registro na tabela PRODUTO", error) # Caso dê uma exceção, printa o erro.
    finally:  # Fecha a conexão com o banco e o cursor
        if(self.connection): 
            cursor.close()
            self.connection.close()

  def getDados(self):
      try:
          self.abrirConexao()
          cursor = self.connection.cursor()
          query = """SELECT * FROM public."PRODUTO"; """
          cursor.execute(query)
          records = cursor.fetchall() # retorna todos os registros em formato de List
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
        preco_ajustado = preco + (preco* 0.1) # também é implementado no update, para ter sempre coerência com o preço
        cursor.execute(query, (nome, preco, preco_ajustado, codigo))
        self.connection.commit()
        count = cursor.rowcount
        print(count, "Registro atualizado com sucesso! ")
        print("Registro Depois da Atualização ")
        sql_select_query = """select * from public."PRODUTO" where "CODIGO" = %s"""
        cursor.execute(sql_select_query, (codigo,)) # Dá um select para a impressão da linha atualizada
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
        sql_delete_query = """DELETE FROM public."PRODUTO" where "CODIGO" = %s""" # Deleção do registro
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

```

#### Arquivo principalBD.py

```python
class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        # inicialização dos componentes
        self.lbCodigo=tk.Label(win, text='Código do Produto:')
        self.lblNome=tk.Label(win, text='Nome do Produto')
        self.lblPreco=tk.Label(win, text='Preço')

        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
        self.btnConsultar=tk.Button(win, text='Consultar')
        self.btnConsultar.bind("<Button>", lambda e: self.consultaProdutos(win)) # cria uma nova tela

        # localização dos campos
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
        self.btnConsultar.place(x=250, y= 250)

    def consultaProdutos(self, master): # Neste método, não nos preocupamos no princípio da responsabilidade única do SOLID.
        novaJanela = tk.Toplevel(master) # configuração da nova tela
        novaJanela.title('Consulta de produtos')
        novaJanela.geometry('800x600')
        tree = ttk.Treeview(novaJanela, selectmode='browse', columns=("col1","col2", "col3", "col4"), show='headings') # Configuração da TreeView
        tree.column("col1", width=100, minwidth=50, stretch='no')
        tree.heading("#1", text="Id")
        tree.column("col2", width=200, minwidth=50, stretch='no')
        tree.heading("#2", text="Nome")
        tree.column("col3", width=200, minwidth=50, stretch='no')
        tree.heading("#3", text="Preço")       
        tree.column("col4", width=300, minwidth=50, stretch='no')
        tree.heading("#4", text="Preço Ajustado") 
        tree.pack(expand=True, fill='both') 
        try: 
            record = self.objBD.getDados()
            for row in record:
                tree.insert('', 'end', values=row) # Implementação de cada registro na tabela, utilizando um laço for para obter cada registro
                

        except(Exception) as error:
            print(error)

    def fCadastrarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos() # chama o método para manipular na query
            self.objBD.inserirDados(codigo, nome, preco) # chama o método 
            self.fLimparTela() # chama o método para limpar os inputs
            print('Produto Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')
    
    def fLimparTela(self):
        try: # limpa todos os inputs
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    def fAtualizarProduto(self):
        try: # pega os campos e passa como parâmetro do método de atualização 
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')  

    def fExcluirProduto(self):
        try: # deleta o registro passando a primary key
            codigo, nome, preco= self.fLerCampos()
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')

    def fLerCampos(self): # ler todos os campos inputados
        try:
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            print('Leitura dos dados com sucesso!')

        except:
            print('Não foi possível ler os dados')
        return codigo, nome, preco

```
#### Arquivo index.py
```
#-------------------------------------
#Programa Principal
#-------------------------------------
janela=tk.Tk()
principal=ui.PrincipalBD(janela)
janela.title('Bem Vindo a Tela de Cadastro')
janela.geometry("600x500")
janela.mainloop()
```

### Prints das linhas do banco de dados

![print-bd](https://github.com/gustavops02/av-product-storage/assets/87784023/73f404c1-d3b2-46e8-88fc-66a90f25864f)


