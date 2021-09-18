matriz = [["Joao","São paulo","(11)9999-5241"],["Maria","Ribeirão preto","(16)9999-8596"],["Ana","Manaus","(92)9999-8574"]]
#//implemtentar loop abaixo 
# for x in matriz:
#   print("Nome: %s"%(matriz[x][0]))
#   print("Cidade: %s"%(matriz[x][1]))
#   print("Telefone: %s"%(matriz[x][2]))
x=0
while x< len(matriz):
    print("Nome: %s"%(matriz[x][0]))
    print("Cidade: %s"%(matriz[x][1]))
    print("Telefone: %s"%(matriz[x][2]))
    x=x+1