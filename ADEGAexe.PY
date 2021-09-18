pde = ["Zomo","Ziggy","Ceda","Rosh","Carvão 1kg"]
vde = [10,12,2,20,60]
pdb = ["Skol 350ml","Skol 550ml","Fardo Skol","Whisky cockland(garrafa)","Whisky Ballantines(garrafa)","gelo de coco","vibe (2L)","long one(2L)","corote","chevete","Balalaika"]
vdb = [4,8,40,50,100,3.50,12,10,4,10,15]







def venda ():
   valor = float(input("Valor da compra R$:"))
   pago = float(input("Valor pago R$:"))
   total = (pago - valor)
   print ("Troco = R$:",total)
   return total

def produtos():
    c=0
    print("1- essências")
    print("2- Bebidas")
    ope = int(input())
    if ope== 1:
        while c<= 4:
            print("%s R$:%d"%(pde[c],vde[c]))
            c=c+1
    if ope== 2:
        while c<= 10:
            print("%s R$:%d"%(pdb[c],vdb[c]))
            c=c+1
    return
# loop de repetição do Menu
flg = 0
opp = 1
while flg != 3 :
    print("1-Vender")
    print("2-Valores")
    print("3- sair")
    op = int(input(""))
    flg = op
    if op == 1:
        print('\n' * 150)
        venda()
        print("---------------------")
    if op == 2:
        print('\n' * 150)
        produtos()
        print("---------------------")