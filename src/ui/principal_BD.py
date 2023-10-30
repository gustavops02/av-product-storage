import tkinter as tk
from database import crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes

        # labels
        self.lbCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome do Produto:')
        self.lblPreco = tk.Label(win, text='Preço')

        #inputs
        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        # buttons
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar')
        self.btnExcluir=tk.Button(win, text='Excluir')
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)