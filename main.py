from tkinter import*
from constantes import*
from gera import*
from atualizar import*
import random
...
raiz = Tk()

class Janela():
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = Frame(raiz,bg=cinza1)
        self.fr3.pack()

        self.fr4 = Frame(raiz,bg=cinza1)
        self.fr4.pack()
        ...
        self.img_center = PhotoImage(file='imagens/senha1.png')
        ...
        #texto inicial
        self.lb1 = Label(self.fr1, text='Gerador de Senhas', font=title1,bg=cinza1, fg= azul_claro)
        self.lb1.pack(pady=10)
        ...
        #Imagem do cadeado
        self.lbimg1 = Label(self.fr2, image= self.img_center,bg=cinza1)
        self.lbimg1.pack(pady=10)
        ...
        #Botao gerador de senha
        self.gerador = Button(self.fr3, text='GERAR SENHAS', bg=cinza2, font=fonte5, relief=RAISED, border=8, command=self.acao_do_botao)
        self.gerador.pack(pady=30)
        ...
        self.lb2 = Label(self.fr4, text='', bg=cinza2, fg=cinza1, font=fonte3, width=15, pady=10)
        self.lb2.pack()
    def gerar_senha(self):
        tamanho = 8
        caracteres = 'AaBbCcDdEeFfGgHhIiJjKklLmMnNOoPpQqTtRrSsUuVvWwXxYyZz!@#$%&*_123456789'
        senha = ''
        ...
        for num in range(tamanho):
            aleatorios = random.choice(caracteres)
            senha += aleatorios
        return senha
    def acao_do_botao(self):
        senha_gerada = self.gerar_senha()
        self.lb2.config(text=senha_gerada)


raiz.geometry('450x450+300+300')
raiz.title('Gerador de Senhas by KevinCruzz')
raiz['bg'] = cinza1
raiz.iconbitmap('imagens/cadeado.ico')
janela = Janela(raiz)
raiz.mainloop()