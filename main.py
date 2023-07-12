from class_personal import Personal
from class_exception import SizeError
from work_file import write_file
def pare_input_string(string):
    result=string.split()
    if len(result) !=6:
        raise SizeError(len(result))
    return result
def build_person_info(result):
    now_person=Personal()
    now_person.set_first_name(result[0])
    now_person.set_second_name(result[2])
    now_person.set_last_name(result[1])
    now_person.set_date_of_birth(result[5])
    now_person.set_phone_num(result[4])
    now_person.set_sex(result[3])
    print('all correct')
    return now_person
    


InString=input("Введите через пробел Имя,Отчество,Фамиию,пол,номер телефона, дату рождения"+'\n')
result=pare_input_string(InString)
now_person=build_person_info(result)
write_file(now_person)