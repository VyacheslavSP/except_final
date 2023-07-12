from class_exception import DateFormatError,PhoneNumberError,SexError
from datetime import datetime

class Personal:
    def __init__(self):
        pass
    def set_first_name(self,first_name):
        if isinstance(first_name, str): 
            self.first_name=first_name
        else:
            raise ValueError 
    def set_second_name(self,second_name):
        if isinstance(second_name, str):
            self.second_name=second_name
        else:
            raise ValueError
    def set_last_name(self,last_name):
        if isinstance(last_name, str):
            self.last_name=last_name
        else:
            raise ValueError
    def set_date_of_birth(self,date_of_birth):
        format = "%d.%m.%Y"
        try:
            if datetime.strptime(date_of_birth, format):
                self.date_of_birth=date_of_birth
        except:
            raise DateFormatError(date_of_birth)
    def set_phone_num(self,phone_number): 
        try:
            temp=int(phone_number)
        except:
            raise PhoneNumberError(phone_number)
        if temp>=0:
                self.phone_number=phone_number
        else:
            raise PhoneNumberError(phone_number)
    def set_sex(self,sex):
        if sex=='m' or sex=='f':
            self.sex=sex
        else:
            raise SexError(sex)        
