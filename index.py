import tkinter as tk
import crud as crud
import principalBD as ui
#-------------------------------------
#Programa Principal
#-------------------------------------
janela=tk.Tk()
principal=ui.PrincipalBD(janela)
janela.title('Bem Vindo a Tela de Cadastro')
janela.geometry("600x500")
janela.mainloop()