from tkinter import *

class janela:
    def __init__(self, toplevel1):
        self.fr1 = Frame(toplevel1)
        self.fr1.pack()

        self.botao1 = Button(self.fr1,text='se quiser sim mano')
        self.botao1['background'] = 'red'
        self.botao1['font'] = ('verdana', '18', 'italic', 'bold')
        self.botao1['height'] = 5
        self.botao1.pack()

        self.botao2 = Button(self.fr1, bg='pink', commad=toplevel1.destroy)
        self.botao2['text'] = 'se quiser nao mano'
        self.botao2['fg'] = 'blue'
        self.botao2['width'] = 15
        self.botao2.pack()


raiz = Tk()
janela(raiz)
raiz.mainloop()


