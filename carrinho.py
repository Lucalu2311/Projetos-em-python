#BD
pdb = ["Skol 350ml","Skol 550ml","Fardo Skol","Whisky cockland(garrafa)","Whisky Ballantines(garrafa)","gelo de coco","vibe (2L)","long one(2L)","corote","chevete","Balalaika","Zomo","Ziggy","Ceda","Rosh","Carvão 1kg"]
vdb = [4,8,40,50,100,3.50,12,10,4,10,15,10,12,2,20,60]
#Loop de exibição dos produtos controlado pela quantidade de produtos do vetor
# encrementar autoamtização de loop!!!!!!
print("-------------------------------------------------------------------------")
for c in pdb:
    print("|%d|: %s R$:%d"%(c,pdb[c],vdb[c]))
print("--------------------------------------------------------------------------")
#
flg=True
s="s"
n="n"
tt =[]
aa=[]
bb=[]
t=0
to=0
p=0
x=0
k=0
m=0
z=0
q=0
produto_soma= []
#loop principal/controle 
while flg==True:
    a = int(input("selecione um produto: "))
    qtd = int(input("quantidade: "))
    t=vdb[a]
    to=(t*qtd)
    tt.append(to)
    aa.append(pdb[a])
    bb.append(qtd)
    produto_soma.append(t)
    t=input("Deseja continuar s/n? ")
    if t==n:
        while x<=p:
            k=k+tt[x]
            x=x+1
        print("----------------------- PRODUTOS --------------------------------------")
        while z<=p:
            print("%d x %s = R$:%d"%(bb[z],aa[z],produto_soma[z]))
            z=z+1
        print("-----------------------------------------------------------------------")
        print("Total R$:%d" %(k))
        l=float(input("Valor Pago R$:"))
        m=(l-k)
        print("Troco = R$:%d"% (m))
        flg= False
    if (t!= s) and (t!=n):
        print("opção incorreta")
        flg=False
    if t==s:
        to=0
        t=0
        p=p+1






