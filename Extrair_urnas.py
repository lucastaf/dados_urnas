import os
import csv
import py7zr

#Variaveis definida pelo usuario
while True:
 #define Codigo do estado

 while True:
  estado = input('insira o código do estado: ')
  if len(estado) == 2:
     break
  else:
      print('O código do estado precisa ter apenas 2 letras')
 #define nome do arquivo que sera salvo

 while True:
  csv_name = input('insira o nome do arquivo que sera salvo (deixe em branco para ' + estado + '.csv): ')
  if csv_name == '':
      csv_name = estado
  if not('.' in csv_name):
      break
  else:
   print("Escreva o nome do arquivo sem o ponto")
 # decidi onde esta os dados das cidades

 while True:

  csv_city_name = input('insira o nome do arquivo onde está os dados de cada cidade (deixe em branco para nao preencher a tabela com dados de cidades): ')
  if csv_city_name == '':
      csv_city_name = False
  if '.' in str(csv_city_name):
   print("Escreva o nome do arquivo sem o ponto")
  else:
   break
 if not(csv_city_name ==  False):
  csv_city_name = csv_city_name + '.csv'
  # testa se o arquivo da cidade existe
 try:
  if not(csv_city_name == False):
   csv_test = open(csv_city_name, 'r')
   csv_test.close()
 except:
  print("Arquivo nao existe, essa aba da tabela nao sera preenchida")
  csv_city_name = False

 #decidir deletar arquivos inuteis
 delete_choice_files = input('Deletar arquivos inuteis?(Insira "N" para nao): ')
 if "N" in delete_choice_files.upper():
  delete_choice_files = False
 else:
  delete_choice_files = True
 #decidir deletar arquivos uteis
 delete_choice_info = input('Deletar arquivos uteis?(Insira "N" para nao): ')
 if "N" in delete_choice_info.upper():
  delete_choice_info = False
 else:
  delete_choice_info = True
 #Confirma a seleção dos dados
 print('\nEssas informações estão corretas? Estado= '+estado+', Nome do arquivo a ser salvo= '+csv_name+'.csv, Arquivo onde esta os dados da cidade= '+str(csv_city_name)+', Deletar Arquivos inuteis= '+str(delete_choice_files)+', Deletar arquivos uteis= '+str(delete_choice_info))
 reset_choice = input('Deixe em branco para confirmar ou digite "n" para reescrever as opções: ')
 if not("N" in reset_choice.upper()):
  break

#Variaveis Criadas: estado, csv_name, csv_city_name, delete_choice_files, delete_choice_info
#Fim da seleção de variaveis
print("\n Começando Extração dos dados")

#apaga a quebra de linha do arquivo com dado de cidades
if csv_city_name != False:
 csv_city_file = open(csv_city_name,'r',encoding="utf-8-sig").readlines()
 for line in range(len(csv_city_file)):
  csv_city_file[line] = csv_city_file[line][:-1]

#define alguns padroes para o arquivo csv a ser gerado
csv_file = open(str(csv_name) + '.csv','w',newline='',encoding="latin-1")
csv_writer = csv.writer(csv_file)
 #primeira linha do arquivo csv
if csv_city_name != False:
 csv_writer.writerow(['ID','UF','MUNICIPIO','MUNICIPIO_ID','ZONA','SECAO','Ver_Urna','TOTAL','ABSTENCAO','NULO','BRANCO','LULA','BOLSONARO','SOMA','P_LULA','P_BOLSONARO','Num_hab_cid','Regiao_cid','LINK_TSE'])
else:
 csv_writer.writerow(['ID', 'UF', 'MUNICIPIO', 'MUNICIPIO_ID', 'ZONA', 'SECAO','Ver_Urna', 'TOTAL', 'ABSTENCAO', 'NULO', 'BRANCO', 'LULA', 'BOLSONARO', 'SOMA', 'P_LULA', 'P_BOLSONARO', 'LINK_TSE'])
#Adquiri a lista de arquivos na pasta
file_list = os.listdir()
infolder = os.getcwd()
#essa variavel ira contar quantos arquivos ja foram lidos na pasta
num_file_read = 0
#Caso tenha sobrado algum arquivo dat ou jez na pasta, dara problema na hora de extrair do logjej.
#isso é só uma garantia de que nao tera nenhum
for file in file_list:
 file_ext = os.path.splitext(file)[1]
 if file_ext == '.dat' or file_ext == '.jez':
     os.remove(file)
#a lista das estensões de arquivos que são inuteis
useless_ext = '.bu .rdv .vscmr .jez .logsajez .busa .vscsa'
#este for ira ler todos os arquivos dentro da lista de arquivos
for zip_file in file_list:
 print('arquivos concluidos: ' + str(num_file_read) +'/'+ str(len(file_list)) +' '+str(zip_file))
 #reseta variaveis do arquivo anterior
 lula=bolsonaro=soma=plula=pbolsonaro=total=branco=nulo=abstencao=0
 municipio=municipio_id=zona=secao=city_hab=city_region='not_found'
 #abre cada arquivo zip
 if os.path.splitext(zip_file)[1] in useless_ext and delete_choice_files == True and not(os.path.isdir(zip_file)):
  os.remove(zip_file)
 #se o arquivo for um zip, entao ele sera relevante
 if py7zr.is_7zfile(zip_file):
  file_name = os.path.splitext(zip_file)[0]
  py7zr.unpack_7zarchive(zip_file, infolder)
  zip_file_list = (py7zr.SevenZipFile(zip_file, mode='r', filters=None, dereference=False, password=None)).getnames()
  #renomea o logd.dat, para garantir q ele tera um id unico
  os.rename('logd.dat', file_name + '.dat')
  #le o arquivo extraido
  file = open(file_name + '.dat', 'r', encoding="latin-1").readlines()

  #procura onde esta o modelo de urna
  for line in range(50,55):
   if "Identificação do Modelo de Urna" in file[line]:
     urna_ver = file[line].split()[-2]
     break
  #aqui começa a extração do arquivo imgbu, que possui o mesmo nome que o arquivo logjez.
  #caso esse arquivo não exista, este try ira denunciar isso.
  try:
   file = open(file_name + '.imgbu','r', encoding="latin-1").readlines()
   dis_secao = 5
  except:
   try:
    file = open(file_name + '.imgbusa','r', encoding="latin-1").readlines()
    dis_secao = 4
   except:
    print("Nao foi encontrado imbgu(sa) para arquivo " + str(file_name))
  #procura as informações da cidade e da sessão
  for line in range(13, 23):
   #defini informações da sessão
   if "Município" in str(file[line]):
    municipio_id = file[line].split()[-1]
    municipio = file[line + 1].strip()
    zona = file[line + 3].split()[-1]
    secao = file[line + dis_secao].split()[-1]
   #defini os votos para lula e bolsonaro
  for line in range(65, 82):
   if "LULA" in str(file[line]):
    lula = int(file[line].split()[-1])
   if "JAIR BOLSONARO" in str(file[line]):
    bolsonaro = int(file[line].split()[-1])
  soma = lula + bolsonaro
  if soma != 0:
   plula = round((lula / soma) * 100, 2)
   pbolsonaro = round((bolsonaro / soma) * 100, 2)
 #defini os demais dados(total, nulos, etc.)
  for line in range(73, 83):
   if "Eleitores Aptos" in str(file[line]):
    total = file[line].split()[-1]
    branco = file[line + 2].split()[-1]
    nulo = file[line + 3].split()[-1]
    abstencao = str(int(total) - int(file[line + 4].split()[-1]))
  #gera o link do tse
  linktse = ("https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e545;uf="+estado.lower()+";ufbu="+estado.lower()+";mubu="+municipio_id+";zn="+zona+";se="+secao+"/dados-de-urna/boletim-de-urna")
  #procura qual as informações deste municipio no arquivo definido, caso ele tenha sido definido
  if csv_city_name != False:
   for line in csv_city_file:
    if municipio in line:
     city_info = line.split(',')
     city_hab = city_info[1]
     city_region = city_info[2]
     break
  #gera todas as informações coletadas numa array, uma versao com os dados da cidade, e uma sem.
  if csv_city_name != False:
   data = [file_name,estado.upper(),municipio,municipio_id,zona,secao,urna_ver,total,abstencao,nulo,branco,str(lula),str(bolsonaro),str(soma),str(plula),str(pbolsonaro),city_hab,city_region,linktse]
  else:
   data = [file_name, estado.upper(), municipio, municipio_id, zona, secao,urna_ver, total,  abstencao, nulo, branco,str(lula), str(bolsonaro), str(soma), str(plula), str(pbolsonaro),linktse]
  #iseri a data gerada
  csv_writer.writerow(data)
  #deleta o arquivo lido, ja que ele nao sera mais necessario
  if delete_choice_info == True and not(zona == 'not found'):
   os.remove(file_name + '.dat')
   try:
    os.remove(file_name + '.imgbu')
   except:
    try:
     os.remove(file_name + '.imgbusa')
    except:
     print("Imgbu(sa) não encontrado: " + file_name)
 #deleta o arquivo zip, nao lembro porque mas isso fica aqui  ¯\_(ツ)_/¯
 if delete_choice_files == True and os.path.splitext(zip_file)[1] == '.logjez':
  os.remove(zip_file)
 #aumenta um na contagem de arquivos lidos
 num_file_read += 1

#finalizado tudo, fecha o arquivo csv
csv_file.close()
if delete_choice_files == True:
 file_list = os.listdir()

for file in file_list:
 file_ext = os.path.splitext(file)[1]
 if file_ext in useless_ext and not(os.path.isdir(file)):
  os.remove(file)


print('\nLeitura dos arquivos finalizada.')