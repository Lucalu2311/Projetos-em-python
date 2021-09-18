def taboada_pre():
    c=0
#// o valor a ser calculado é encremenntado na concatenação do print
    while c <= 10:
       print (" 9 x %d = " %(c), + (c * 9))
       c=c+1
    return c 

def taboada_inseri():
    c= 0
    lm=int(input("limete da taboada "))
    valor=int(input("valor a ser multiplicado "))
    while c<=lm:
        print(" %d x %d = " %(valor,c), + (c * valor))
        c=c+1
    return c 
taboada_inseri()