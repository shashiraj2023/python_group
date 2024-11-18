import os,shutil
folders={
  'videos':['.mp4','.mkv'],
  'audios':['.mp3','.waav'],
  'images':['.jpg','.png'],
  'documents':['.pdf','.xlsx','.xls',".zip",".rar",'.txt'],
}
# print(folders)
# for folder_name in folders:
#   print(folder_name,folders[folder_name])
# directory=input("enter the location ")
def create_move(ext,file_name):
     find=False
     for folder_name in folders:
         if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                 os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name)) 
            find=True  
            break
     if find!=True:
        if other_name not in os.listdir(directory):
                 os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))
               
    
        
        
        
directory="C:\\Users\\ankit\\Downloads"
other_name=input("enter the name for unknown format: ")
all_files=os.listdir(directory)
# print(all_files) 
for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        create_move(i.split(".")[-1],i)






