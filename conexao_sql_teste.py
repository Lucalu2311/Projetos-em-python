
import pyodbc 
driver = "SQL Server"
server = "LAPTOP-2E9UIFE5\SQLEXPRESS"
base_dados = "adega"
conexao = pyodbc.connect("DRIVER="+driver+"; Server="+server+"; Database="+base_dados+"; TrustedConnection=yes")
cursor= conexao.cursor()

cursor.execute("select * from Produtos")
linha = cursor.fetchone()
res = []
def teste(linha,res):
    while linha:
        for coluna in linha:
           res.append(coluna)
           print(res)
           linha = cursor.fetchone()
    return coluna
teste(linha,res)
print(res)
