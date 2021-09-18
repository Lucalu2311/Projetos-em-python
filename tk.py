import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.msg = Label(self.frame, text="oi porra")
        self.msg.pack()
myapp = App()
#Cria a aplicação 
myapp.master.title("teste")
myapp.master.maxsize(50000,50000)
#inicia o programa
myapp.mainloop()