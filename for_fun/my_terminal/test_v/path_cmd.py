import os, json



class path_cmd():

    def __init__(self,my_path):
        self.path = my_path


    def current_position(self):
        #D:\Yan\PHD PROGRAM\Class\Spring 2020\Econ 9000 Machine learning\Try_pycharm_\for_fun\my_terminal
        pos = self.path
        return pos

    #cd..
    def go_back_position(self):
        #D:\Yan\PHD PROGRAM\Class\Spring 2020\Econ 9000 Machine learning\Try_pycharm_\for_fun
        back_pos = os.path.abspath(os.path.join(self.path, os.path.pardir))
        return back_pos

    def next_position(self, next_folder):
        pos = os.path.join(self.path, next_folder)
        return pos

    def lower_to_capital(self):
        letter = self.path.replace(':','')
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if letter in lower:
            letter = upper[lower.index(letter)]

        return letter + ':/'

    def add_to_path(self):
        app_name = input('App name: ')
        app_path = input('App path: ')
        df = {app_name : app_path}

        if not os.path.exists('quick_path.json'):
            with open('quick_path.json', 'w') as f:
                json.dump(df,f)
        else:
            with open('quick_path.json', 'r') as f:
                database = json.load(f)

            with open('quick_path.json', 'w') as g:
                database.update(df)
                json.dump(database, g)

    def del_path(self):
        app_name = input('app you want to delete: ')
        with open('quick_path.json', 'r') as f:
            df = json.load(f)
            del df[app_name]
        with open('quick_path.json', 'w') as g:
            json.dump(df, g)

