class Date:
    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month}-{self.day}-{self.year}'

    @classmethod
    def millenium_c(cls, month,day):
        return cls(month,day,2000)

    @staticmethod
    def millenium_s(month,day):
        return Date(month,day,2000)



class DateTime(Date):
    def display(self):
        return f'{self.month}-{self.day}-{self.year}-00:00:00PM'


dt1 = DateTime.millenium_c(10,10)
dt2 = DateTime.millenium_s(6,9)



print(dt1.display())
print(f'dt1 is instanse DateTime: {isinstance(dt1,DateTime)}')
print(dt2.display())
print(f'dt2 is instanse DateTime: {isinstance(dt2,DateTime)}')