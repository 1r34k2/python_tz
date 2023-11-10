import os, shutil, stat
from sys import argv
from git import Repo
import json
from zipfile import ZipFile
from datetime import datetime
import time

def removeReadOnly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

start_time = time.time()
repoFolder = os.path.join(os.getcwd(), argv[1].split('/')[-1])
if(os.path.exists(repoFolder)):
    shutil.rmtree(repoFolder, onexc=removeReadOnly)
Repo.clone_from(argv[1], repoFolder)
end_time = time.time()
print('Клонирование успешно, время выполнения: ', end_time - start_time)

start_time = time.time()
for f in os.listdir(repoFolder):
    if(f == argv[2].split("/")[0]):
        continue
    elif(os.path.isdir(os.path.join(repoFolder,f))):
        shutil.rmtree(os.path.join(repoFolder, f), onexc=removeReadOnly)
    else:
        os.remove(os.path.join(repoFolder, f))
end_time = time.time()
print('Удаление файлов кроме исходников успешно, время выполнения', end_time - start_time)

start_time = time.time()
files = []

for f in os.listdir(os.path.join(repoFolder, argv[2])):
    if(f.endswith('.py') or f.endswith('.js')):
        files.append(f)
    

textInFile = { "name": "hello world", "version": argv[3], "files": files }
with open(os.path.join(repoFolder,'version.json'), 'w+') as versionFile:
    json.dump(textInFile, versionFile)
end_time = time.time()
print('Создание файла version.json успешно, время выполнения', end_time - start_time)

start_time = time.time()
with ZipFile(argv[2].split('/')[-1] + datetime.now().strftime('%d%m%Y') + '.zip','w') as zip:
    for root, dirs, files in os.walk(repoFolder.split('\\')[-1]):
        print(root)
        for file in files:
            zip.write(os.path.join(root, file))
end_time = time.time()
print('Архивация успешна, время выполнения:', end_time - start_time)
