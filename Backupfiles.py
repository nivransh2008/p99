import os 
import shutil 
path = input(" Please enter the specified path:")
list_files = os.listdir(path)
for i in list_files: 
    name, ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == ' ':
        continue 
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+i,path+"/"+ext+"/"+i) 
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+i, path+"/"+ext+"/"+i) 
        