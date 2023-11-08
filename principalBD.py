import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes
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
    
    def consultaProdutos(self, master):
        novaJanela = tk.Toplevel(master)
        novaJanela.title('Consulta de produtos')
        novaJanela.geometry('800x600')
        tree = ttk.Treeview(novaJanela, selectmode='browse', columns=("col1","col2", "col3", "col4"), show='headings')
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
                tree.insert('', 'end', values=row)
                

        except(Exception) as error:
            print(error)
    
    def fCadastrarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')
    
    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')  

    def fExcluirProduto(self):
        try:
            codigo, nome, preco= self.fLerCampos()
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')

    def fLerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            print('Leitura dos dados com sucesso!')

        except:
            print('Não foi possível ler os dados')
        return codigo, nome, preco