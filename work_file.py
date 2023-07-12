import os,traceback
from class_personal import Personal
def find_file_name(name):
    return os.path.exists(name)
def build_format_string(Personal):
    string=None
    string='<'+Personal.second_name+'>'+'<'+Personal.first_name+'>'+'<'+Personal.last_name+'>'+'<'+Personal.date_of_birth+'>'+'<'+Personal.phone_number+'>'+'<'+Personal.sex+'>'
    return string
def write_file(Personal):
    name=Personal.second_name
    string=build_format_string(Personal)
    if(find_file_name(name)): # если такой файл уже есть то дозаписать
        try:
            f=open(name,'r')            ## ожидаются ошибки ошибка чтения и ошибка записи файла (ну и файл не найден,хотя и есть проверка на это)
            tmp=f.read()
            f.close
            l=tmp.splitlines();l.insert(0,string);tmp='\n'.join(l)
            f=open(name,'w')
            f.write(tmp)
            f.close
        except Exception:    
            tb=traceback.format_exc()
            print(tb)
    else:
        try:
            f=open(name,'w')
            f.write(string)
            f.close
        except Exception:    
            tb=traceback.format_exc()
            print(tb)
            

