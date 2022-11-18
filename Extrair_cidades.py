import os
import csv

#Determina qual o nome do arquivo q sera salvo
while True:
    csv_name = input('Insira o nome do arquivo que será salvo: ')
    if csv_name == '':
        csv_name = 'cidades'
    if not ('.' in csv_name):
        break
    else:
        print("Escreva o nome do arquivo sem o ponto")

files_list = os.listdir()
all_city = []
csv_file = open(str(csv_name) + '.csv','w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Cidade','Habitantes','Região'])
count_files = 0

for file in files_list:
 print("Arquivos lidos: " + str(count_files) + '/' + str(len(files_list)))
 municipio = 'zz_not found'
 if os.path.splitext(file)[1] == '.imgbu':
   files_lines = open(file, 'r', encoding = 'latin-1').readlines()
   for line in range(13,23):
       if 'Município' in str(files_lines[line]):
          municipio = files_lines[line + 1].strip()
          break
   all_city.append(municipio)
 count_files +=1

filtred_city = list(set(all_city))
print(filtred_city)
filtred_city.sort()
print(filtred_city)
for name in filtred_city:
    csv_writer.writerow([name,'',''])


csv_file.close()