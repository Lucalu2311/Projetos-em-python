
def media_escolar():
    notas = [5,7,10,3]
    c=0
    d=0
    for x in notas:
        c=c+x
        d=d+1
    media = c/d
    print(media)
    return media
def media_vendas():
    vendas = []
    c = 0
    soma=  0
    while c <=3:
        vendas.append(float(input("valor das vendas")))
        c=c+1
    for x in vendas:
        soma = soma + x
    media = soma / len(vendas)
    print("Total de vendas = %d "%(soma))
    print("Média = %d"%(media))
    return  vendas,media,soma



matriz = [["a",1],["b",2]]#/ exemplo de matriz
print(matriz[0][0])# como acessar o valor do indice da matriz e o conteudo do indice dentro do elemennte ( no caso, o elemente da posição aonde está a informação que eu quero, e depois o indice de uma certa informação dentro desse elemento)