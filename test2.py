class MyClass:

    def __init__(self, some):
        self.some = some

    def display(self):
        return self

    @staticmethod
    def staticmethod():
        print("static method called")

    @classmethod
    def classmethod(cls):
        print(f'class metod called:{cls}')



MyClass.staticmethod()
MyClass.classmethod()