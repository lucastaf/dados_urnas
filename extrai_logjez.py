import os
import py7zr
import csv

infolder = os.getcwd()
files_list = os.listdir()


for file in files_list:
 file_ext = os.path.splitext(file)[1]
 if file_ext == '.dat' or file_ext == '.jez':
     os.remove(file)

files_list = os.listdir()

for zip_file in files_list:
    if py7zr.is_7zfile(zip_file):
     #print(zip_file)
     py7zr.unpack_7zarchive(zip_file, infolder)
     files = (py7zr.SevenZipFile(zip_file, mode='r', filters=None, dereference=False, password=None)).getnames()
     if len(files) > 1:
        os.remove(files[0])

     os.rename('logd.dat', os.path.splitext(zip_file)[0] + '.dat')
     file = open(os.path.splitext(zip_file)[0] + '.dat','r',encoding="latin-1").readlines()

     for line in range(len(file)):
         if "Identificação do Modelo de Urna" in file[line]:
             print(str(line)+" "+ file[line].split()[-2])
             break

