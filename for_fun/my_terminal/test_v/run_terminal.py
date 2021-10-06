import os, re, glob, json
import scrapping
from data_solving import csv_file
from path_cmd import path_cmd
from file_cmd import file_cmd



class terminal():

    def __init__(self):
        self.path = os.getcwd()
        self.header = ['\033[1;32;60m%s\033[0m@ubuntu:~$ ' % 'synferlo','synferlo @ ubuntu:~$ ', 'Synferlo OoO OS:~#  '][2]
        self.run = True


    def terminal_run(self):
        while self.run:
            command = input('\n' + self.header)
            # quit terminal
            if command == 'quit':
                self.run = False

            # pwd
            if command == 'pwd':
                pwd = path_cmd(self.path).current_position()
                print(pwd)
            # change disk (d:,c:,D:,C:)
            try:
                if re.compile(r'[a-z]{1}:').search(command).group() != None:
                    self.path = re.compile(r'[a-z]:').search(command).group()
                    self.path = path_cmd(self.path).lower_to_capital()
                    print(self.path)
            except:
                pass

            # ls
            if command == 'ls':
                file_cmd(self.path).view_files()

            # cd path
            try:
                if re.compile(r'cd (.*)').findall(command)[0] != '..':
                    after_cd = re.compile(r'cd (.*)').findall(command)[0]
                    valid_folders = []
                    for one_file in glob.glob(os.path.join(self.path, '*')):
                        files = one_file.replace(os.path.join(self.path, ''),'')
                        if '.' not in files:
                            valid_folders.append(files)
                        else:
                            pass
                    if after_cd in valid_folders:
                        self.path = path_cmd(self.path).next_position(after_cd)
                        print(self.path)
                    else:
                        print('Error: No such folder. Command not found.')
            except:
                pass

            # cd..
            if command == 'cd..':
                self.path = path_cmd(self.path).go_back_position()
                print(self.path)
            # mkdir
            try:
                if re.compile(r'mkdir (.*)').findall(command)[0] != []:
                    folder = re.compile(r'mkdir (.*)').findall(command)[0]
                    file_cmd(self.path).mkdir(folder)
            except:
                pass
            # rm
            try:
                if re.compile(r'rm (.*)').findall(command)[0] != []:
                    folder = re.compile(r'rm (.*)').findall(command)[0]
                    file_cmd(self.path).rm(folder)
            except:
                pass
            # touch
            try:
                if re.compile(r'touch (.*)').findall(command)[0] != []:
                    file_name = re.compile(r'touch (.*)').findall(command)[0]
                    file_cmd(self.path).touch(file_name)
            except:
                pass
            # scrapping
            try:
                if re.compile(r'scrapping \w').findall(command) != []:
                    s_mode = re.compile(r"scrapping (\w)").findall(command)[0]
                    scrapping.Scrapping(self.path, s_mode).mode_selection()
            except:
                pass

            # csv
            try:
                if re.compile(r'csv (.*)').findall(command)[0] != []:
                    file_path = os.path.join(self.path, re.compile(r'csv (.*)').findall(command)[0])
                    csv_file(file_path).csv()
            except:
                pass
            # csv.head
            try:
                if re.compile(r'csv\.head (.*\.csv)').findall(command)[0] != []:
                    file_path = os.path.join(self.path, re.compile(r'csv.head (.*\.csv)').findall(command)[0])
                    csv_file(file_path).csv_head()
            except:
                pass

            # run other application/files
            try:
                if re.compile(r'go').findall(command) != []:
                    file_name = re.compile(r'go (.*)').findall(command)[0]
                    file_cmd(self.path).open_file(file_name)
            except:
                pass

            # add to path. then we can use go + <app name> to run without adding path.
            if command == 'add path':
                path_cmd(self.path).add_to_path()

            # delete path
            if command == 'del path':
                path_cmd(self.path).del_path()

            # check the path you have added
            if command == 'check path':
                with open('quick_path.json', 'r') as f:
                    df = json.load(f)
                app = list(df.keys())
                path = list(df.values())
                for i in range(len(app)):
                    print((app[i], path[i]))







if __name__ == '__main__':
    terminal().terminal_run()




