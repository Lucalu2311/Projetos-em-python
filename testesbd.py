import os
import pyodbc 
driver = "SQL Server"
server = "LAPTOP-2E9UIFE5\SQLEXPRESS"
base_dados = "Tradicao"
conexao = pyodbc.connect("DRIVER="+driver+"; Server="+server+"; Database="+base_dados+"; TrustedConnection=yes")
cursor= conexao.cursor()
Produto_id = [] # no banco de dados
Nome_p = [] #no banco de dados
Valor_p = [] #no banco de dados
pd=[] #Nome do produto incrementado na função de  venda
vd=[] # valor dos produtos incrementado na função de venda 
qt=[] # quantidade de produtos incrementado na função de vendas 

def select_id(cursor,Produto_id):
   Produto_id.clear()
   cursor.execute("select Produto_id from Produtos")
   id = cursor.fetchone()
   def ID_PROD(id,Produto_id,):
       while id:
           for coluna in id:
               Produto_id.append(coluna)
               id = cursor.fetchone()
       return coluna
   ID_PROD(id,Produto_id)
   return Produto_id
def select_nome(cursor,Nome_p):
   Nome_p.clear()
   cursor.execute("select Nome from Produtos")
   Nome = cursor.fetchone()
   def NOME_PROD(Nome,Nome_p):
       while Nome :
           for coluna in Nome:
               Nome_p.append(coluna)
               Nome = cursor.fetchone()
       return coluna 
   NOME_PROD(Nome,Nome_p)
   return Nome_p
def select_valor(cursor,Valor_p):
   Valor_p.clear()
   cursor.execute("select Valor from Produtos")
   Valor = cursor.fetchone()
   def VALOR_PROD (Valor,Valor_p):
       while Valor:
           for coluna in Valor:
               Valor_p.append(coluna)
               Valor = cursor.fetchone()
       return coluna
   VALOR_PROD(Valor,Valor_p)
   return Valor_p


def estoque(Produto_id,Nome_p,Valor_p,cursor):
    select_id(cursor,Produto_id)
    select_nome(cursor,Nome_p)
    select_valor(cursor,Valor_p)
    print("---- Estoque ----")
    x=0
    for x in range(len(Produto_id)):
        print("%d - %s R$:%s"%(Produto_id[x],Nome_p[x],Valor_p[x]))
    print("-----------")


def cadastro(Produto_id,cursor):
    print("--- Cadastro de Produtos ---")
    flg=True
    while flg == True:
        nom= input("Nome do Produto ")
        valor = float(input("Valor R$:  "))
        tamanho = len(Produto_id)+1
        cursor.execute("insert into Produtos (Produto_id,Nome,Valor) values (?,?,?)",(tamanho,nom,valor))
        conexao.commit()
        select_id(cursor,Produto_id)
        select_nome(cursor,Nome_p)
        select_valor(cursor,Valor_p)
        op=input("Novo produto (S/N)? ")
        if op == 's':
            nom =''
            valor= None
            tamanho=None
        else:
            flg= False

def venda (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt):
    estoque(Produto_id,Nome_p,Valor_p,cursor)
    print("-- Selecione um Produto --")
    fl = True
    while fl ==True:
        o=int(input("... "))
        q=int(input("Qantidade : "))
        pd.append(Produto_id[o])
        vd.append(Valor_p[o])
        if q >=1:
            qt.append(q)
        else:
            print(".... ERRO ....")

        t=input("Deseja continuar (S/N) ? ")
        if t  =='n' or t == "N":
            fl= False
        if t =='s' or t == 'S':
            o=0
            q=0
    

    return pd,vd,qt

def carrinho(pd,vd,qt):
    print(" -- Carrinho --")
    h=0
    for x in range(len(vd)): #função pra tentar corrigir o proble ao printar o valor total dos produtos
        vd[x]= vd[x].split("\n")
        if vd[x]=="":
            vd= vd[x].split(vd[x])

    for p in range(len(pd)): 
        print("%s x  %s = R$: %s"%(qt[h],Nome_p[pd[h]],(vd[h])*(qt[h])))
        h=h+1
    
    return p
def finalizar (qt,vd):
    trc = True
    total = 0 
    while trc == True:
        for i in range(len(qt)) :
            total = (qt[i]*vd[i]) 
        trc=False
    print("Valor total = R$: %s"%(total))
    troco = float(input("Pago ... R$: "))
    tt= troco-float(total)
    print("Troco = R$: %s"%(tt))
    return tt
#incrementar a função index off para colocar o nome do produto no momento de printar a nota de compra.
#incrementar a função que printa o valor total dos produtos no momento de printar a nota de compra. 

def menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt):
    controle = True
    while controle == True:
        print("1- Estoque ")
        print("2- Cadastro ")
        print("3- Venda")
        print("4- Carrinho ")
        print("5- Finalizar ")
        op=int(input("... "))
        if op == 1:
            op=0
            estoque(Produto_id,Nome_p,Valor_p,cursor)
            l=(input("Voltar (S/N) ? "))
            if l == 's' or l=="S":
                os.system('cls||clear')
                menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
            if l =='n' or l=='N':
                controle == False
        if op ==2:
            op=0
            cadastro(Produto_id,cursor)
            l=(input("Voltar (S/N) ? "))
            if l == 's' or l=="S":
                os.system('cls||clear')
                menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
            if l =='n' or l=='N':
                controle == False
        if op ==3:
            op=0
            venda (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
            l=(input("Voltar (S/N) ? "))
            if l == 's' or l=="S":
                os.system('cls||clear')
                menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
            if l =='n' or l=='N':
                controle == False
        if op == 4:
            op=0
            carrinho(pd,vd,qt)
            l=(input("Voltar (S/N) ? "))
            if l == 's' or l=="S":
                os.system('cls||clear')
                menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
            if l =='n' or l=='N':
                controle == False
        if op == 5:
            op = 0
            finalizar(qt,vd)
    pd,vd,qt = None
    menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)
    return   op 
select_id(cursor,Produto_id)
select_nome(cursor,Nome_p)
select_valor(cursor,Valor_p)
menu (Produto_id,Nome_p,Valor_p,pd,vd,cursor,qt)

#incrementar na função do menu um break para que quando a opção 5 for selecionada e execultada o sistema zere.
#incrementar uma função para alterar o valor dos produtos já cadastrados
