import fileSelecting
import merging
import saving

import time
import subprocess

if saving.load(filename="files.pkl") == None:
    filesMerging,filePath=fileSelecting.selectFiles()
else:
    filesMerging,filePath=fileSelecting.selectFiles(startDir=saving.load(filename="files.pkl"))

if filePath != None:
    saving.save(filePath, filename="files.pkl")

    if saving.load(filename="path.pkl") == None:
        result = fileSelecting.selectFolder()
    else:
        result = fileSelecting.selectFolder(startDir=saving.load())

    saving.save(result, filename="path.pkl")

    if result!= None:
        merging.merge(filesMerging, result+"/"+str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))+".pdf")
        subprocess.run(['explorer', result])