import os
import shutil

path=input("Enter path of the folder to organize the files: ")

files = os.listdir(path)

for file in files:
    filename,extension =os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
print("THE FILES HAVE BEEN ORGANIZED😁")
