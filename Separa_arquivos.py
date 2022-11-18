import os
import pathlib
import shutil

infolder = os.getcwd() + '\\'
try:
 os.mkdir(infolder + '\imbgu')
 os.mkdir(infolder + '\logjez')
except:
 print("Folder ja existe")


imbgufolder = infolder + 'imbgu\\'
logjezfolder = infolder + 'logjez\\'
arquivo_list = os.listdir()
arquivo_ext = os.listdir()
print(logjezfolder)

for x in range(len(arquivo_list)):
 arquivo_ext[x] = pathlib.Path(arquivo_list[x]).suffix
 if arquivo_ext[x] == '.imgbu':
  shutil.move(infolder + arquivo_list[x],imbgufolder + arquivo_list[x])
 if arquivo_ext[x] =='.logjez':
  shutil.move(infolder + arquivo_list[x],logjezfolder)
 if not(arquivo_ext[x]=='.imgbu' or arquivo_ext[x]=='.logjez' or arquivo_ext[x]=='' or arquivo_ext[x]=='.py' or arquivo_ext[x]=='.zip'):
  os.remove(arquivo_list[x])


print(arquivo_list)
print(arquivo_ext)