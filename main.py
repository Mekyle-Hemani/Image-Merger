import fileSelecting
import merging
import saving

import time

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
        merging.merge(filesMerging, result+"/"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+".pdf")