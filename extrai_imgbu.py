import os
import csv



#nome_arquivo = input("Qual deve ser o nome do arquivo onde sera salvo os dados?")
#estado = input("Qual o estado da votação?")
csv_file = open(str(nome_arquivo) + '.csv','w',newline='')
csv_writer = csv.writer(csv_file)

lowestado = estado.lower()
arquivo_list = os.listdir()

csv_writer.writerow(['ID','UF','MUNICIPIO','MUNICIPIO_ID','ZONA','SECAO','TOTAL','ABSTENCAO','NULO','BRANCO','LULA','BOLSONARO','SOMA','P_LULA','P_BOLSONARO','LINK_TSE'])


for file in range(len(arquivo_list)):
 arquivo = (open(arquivo_list[file], "r", encoding="latin-1")).readlines()
 arquivo_ext = (os.path.splitext(arquivo_list[file])[1]
 if arquivo_ext == '.imgbu':
  file_name = os.path.splitext(arquivo_list[file])[0]
  print(arquivo_list[file])
  for line in range(13,23):
   if "Município" in str(arquivo[line]):
    municipio_id = arquivo[line].split()[-1]
    municipio = arquivo[line + 1].strip()
    zona = arquivo[line + 3].split()[-1]
    secao = arquivo[line + 5].split()[-1]

  for line in range(65,75):
   if "LULA" in str(arquivo[line]):
     try:
      lula = int(arquivo[line].split()[-1])
     except:
      lula = 0
     try:
      bolsonaro = int(arquivo[line + 1].split()[-1])
     except:
      bolsonaro = 0
     soma = lula+bolsonaro
     plula = round((lula/soma)*100,2)
     pbolsonaro = round((bolsonaro/soma)*100,2)

  for line in range(73,83):
    if "Eleitores Aptos" in str(arquivo[line]):
     total = arquivo[line].split()[-1]
     branco = arquivo[line+2].split()[-1]
     nulo = arquivo[line+3].split()[-1]
     abstencao = str(int(total) - int(arquivo[line + 4].split()[-1]))
  linktse = ("https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e545;uf="+lowestado+";ufbu="+lowestado+";mubu="+municipio_id+";zn="+zona+";se="+secao+"/dados-de-urna/boletim-de-urna")
  data = [file_name,estado.upper(),municipio,municipio_id,zona,secao,total,abstencao,nulo,branco,str(lula),str(bolsonaro),str(soma),str(plula),str(pbolsonaro),linktse]
  csv_writer.writerow(data)

csv_file.close()