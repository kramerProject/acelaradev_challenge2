import abc

bonus = 0.15
journey_hours=8

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        return journey_hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def get_department(self):
        return self.__departament.name

    def set_department(self,nome):
        self.__departament.name=nome

    def calc_bonus(self):
        return self.salary * bonus


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_department(self):
        return self.__departament.name

    def set_department(self,nome):
        self.__departament.name=nome

    def get_sales(self):
        return self.__sales

    def put_sales(self,sales):
        self.__sales+=sales

    def calc_bonus(self):
        return self.__sales * bonus

