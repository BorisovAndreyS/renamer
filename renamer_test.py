import os

current_dir = os.getcwd()
print('''Привет это программа renamer v1, поможет массово исправить расширение файлов в текущей директории''')


file_ext_current = '.jpg'
change_ext = input(f'Текущее расширение файла {file_ext_current}, будем менять? y/n: ')
if change_ext == 'y':
    new_ext = input('Введите расширение в виде ".jpg"')

#Получили абсолютный путь до текущего файла
file_name = os.path.basename(os.path.abspath(__file__))

#получили список всех файлов в текущей директории
def files_and_dir():
    return os.listdir()

#список исключения
uninclude = ['.git' , '.idea', '.venv', file_name]

list_file = []

#получаем список полезных файлов
for name in files_and_dir():
    if not name in uninclude:
        list_file.append(name)

#переименование os.rename(original_name, new_name)

for name in list_file:
    os.rename(name, name + file_ext_current)
