import os
import subprocess
import shutil
from collections import defaultdict

class File_organizer:
    def __init__(self, path):
        self.path = path
        self.files = defaultdict(list)
        self.extensions_maps={
            'audio':['.mp3','.wav','.flac','.m4a'],
            'video':['.mp4','.mkv','.MKV','.flv','.mpeg'],
            'images':['.jpg','.jpeg','.png','.gif','.heic','.psd','.bmp','.raw'],
            'documents':['.doc','.xls','.ppt','.docx','.xlsx','.pptx','.pdf','.txt','.rtf','.tex'],
            'compressed':['.zip','.rar'],
            'executable':['.exe','.msi'],
            'code':['.py','.java','.c','.cpp','.class','.h','.js','.css','.xml','.php'],
            'web':['.url','.html','.htm','.website'],
            'others':[]
        }

    def map_files(self):
        type_found_and_sorted=[]
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,file)):
                extension_type=os.path.splitext(file)[1]
                for file_type,extensions in self.extensions_maps.items():
                    if extension_type in extensions:
                        self.files[file_type].append(file)
                        type_found_and_sorted.append(file)
                        break  
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,file)) and file not in type_found_and_sorted:
                self.files['others'].append(file) 
        

    def organize_files(self):
        for file_type,files in self.files.items():
            file_dir=os.path.join(self.path,file_type)
            if os.path.exists(file_dir)==False:
                os.mkdir(os.path.join(self.path,file_type))
            for file in files:
                    shutil.move(os.path.join(self.path,file),os.path.join(self.path,file_type))
                
                

    def run(self):
        self.map_files()
        self.organize_files()
        command='start cmd.exe @cmd /k echo "The files have been organized! Organizing one\'s life is a key to having a successful life, and it starts with little things like oraganizing one\'s files which is why i chose this code. "'
        subprocess.run(command,shell=True)


path=input('Enter the path of the directory to be organized: ')
organizer=File_organizer(path)
organizer.run()