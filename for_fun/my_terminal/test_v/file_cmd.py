import glob,re,os,json

class file_cmd():

    def __init__(self, my_path):
        self.path = my_path

    #ls
    def view_files(self):
        for one_file in glob.glob(os.path.join(self.path,'*')):
            file_name = one_file.replace(os.path.join(self.path, ''),'')
            print(file_name)


    def mkdir(self, folder_name):
        if '.' not in folder_name:
            os.mkdir(os.path.join(self.path, folder_name))
        else:
            print('Error: This is not a folder form. It should not include an extension')

    def rm(self, folder_name):

        if os.path.exists(os.path.join(self.path, folder_name)):
            if '.' in folder_name:
                os.remove(os.path.join(self.path, folder_name))
            else:
                os.removedirs(os.path.join(self.path, folder_name))
        else:
            print('Error: No such folder/file.')


    def touch(self, file_name):
        if os.path.exists(os.path.join(self.path, file_name)):
            print('Error: File name has already existed. Try another one.')
        if '.' not in file_name:
            print('Error: A file should have a extension.')
        with open(os.path.join(self.path, file_name), 'w', encoding = 'utf-8') as f:
            f.write('')

    def open_file(self, file_name):
        check_further = True
        for one_file in glob.glob(os.path.join(self.path, '*')):
            name = one_file.replace(os.path.join(self.path, ''),'')
            if file_name == name:
                os.startfile(os.path.join(self.path, file_name))
                check_further = False
        if check_further == True:
            with open('quick_path.json', 'r') as f:
                df = json.load(f)
                if file_name in list(df.keys()):
                    os.startfile(df[file_name])
                else:
                    print('Error: there is not such file under current file, neither in path')