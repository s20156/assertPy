class Employee:
    def __init__(self, __lastname, __firstname, __email):
        self.__lastname = __lastname
        self.__firstname = __firstname
        self.__email = __email

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_lastname(self):
        return self.__lastname

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email


class ProductionWorker(Employee):
    def __init__(self, __lastname, __firstname, __email, __change_number, __pay_hour):
        super().__init__(__lastname, __firstname, __email)
        self.__change_number = __change_number
        self.__pay_hour = __pay_hour

    def set_change_number(self, change_number):
        if change_number == 1 or change_number == 2:
            self.__change_number = change_number
        else:
            raise Exception("Wrong change")

    def get_change_number(self):
        return self.__change_number

    def set_pay_hour(self, pay_hour):
        if (type(pay_hour) != int and type(pay_hour) != float) or pay_hour <= 0:
            raise Exception("Hourly pay has to be positive number")
        self.__pay_hour = pay_hour

    def get_pay_hour(self):
        return self.__pay_hour

