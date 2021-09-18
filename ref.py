import os
pdb = ["Skol 350ml","Skol 550ml","Fardo Skol","Whisky cockland(garrafa)","Whisky Ballantines(garrafa)","gelo de coco","vibe (2L)","long one(2L)","corote","chevete","Balalaika","Zomo","Ziggy","Ceda","Rosh","Carvão 1kg"]
vdb = [4,8,40,50,100,3.50,12,10,4,10,15,10,12,2,20,60]
def estoque():
    x=0
    print("----- Estoque -----")
    for c in pdb:
        print("%d  | %s R$:%d"%(x,c,vdb[x]))
        x=x+1
    print("------------------------")
    return x

def cadastro():
    flg=True
    print("--- Cadastro de Produtos ---")
    while  flg == True:
        pdb.append(input("Nome do produto : "))
        vdb.append(float(input("Valor R$: ")))
        t=input("Novo produto (S/N) ? ")
        if t == 'n':
            flg= False
    return pdb,vdb 
def venda ():
    print("Selecione um produto ")
    estoque()
    pd=[]
    vd=[]
    flg=True
    while flg == True:
        o=int(input(""))
        q=int(input("Qantidade : "))
        pd.append(pdb[o])
        vd.append(vdb[o]*q)
        t=input("Deseja continuar (S/N) ? ")
        if t=="n":
            flg= False 
        if t=="s":
            o=0
            q=0
    return pd,vd
def carrinho(pd,vd):
    print(" -- Carrinho --")
    for p in pd:
        print("%s R$: %d"%(pd[p],vd[p]))
    return p,pd,vd
def menu ():
    controle = True
    while controle == True:
        print("1 - Estoque  ")
        print("2 - Cadastro ")
        print("3- Venda  ")
        print("4- Carrinho ")
        op=int(input("...  "))
        if op == 1:
            estoque()
            x=(input("Voltar (S/N) ? "))
            if x== "s":
                os.system('cls||clear')
                menu()
            if x=="n":
                controle = False    
        if op == 2:
            cadastro()
            x=(input("Voltar (S/N) ? "))
            if x== "s":
                os.system('cls||clear')
                menu()
            if x=="n":
                controle = False
        if op == 3:
            venda()
            x=(input("Voltar (S/N) ? "))
            if x== "s":
                os.system('cls||clear')
                menu()
            if x=="n":
                controle = False
        if op == 4:
            carrinho()
            x=(input("Voltar (S/N) ? "))
            if x== "s":
                os.system('cls||clear')
                menu()
            if x=="n":
                controle = False
    return op
menu()
