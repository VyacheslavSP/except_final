class DateFormatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} Некорректый формат даты'.format(self.value)
    
class PhoneNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} номер телефона не целое беззнаковое число'.format(self.value)
class SexError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} некорректный пол'.format(self.value)
class SizeError(Exception):
    def __init__(self,value):
       self.value=value
    def __str__(self):
        answer=" больше " if self.value>6 else " меньше "
        tmp="количество введеных данных"+answer+"требуемых" 
        return tmp.format(self.value)
    