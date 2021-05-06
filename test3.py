class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.lower().capitalize()

    @property
    def initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'


n = Name('joHn', 'coNnor')

print(n.initials)
