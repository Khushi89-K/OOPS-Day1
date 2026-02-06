class father:
    def __init__(self,surname,father_name):
        self.surname=surname
        self.father_name=father_name
    def display_surname(self):
        print("the surname is:", self.surname)
class son(father):
    def __init__(self, name,surname, father_name):
        super().__init__(surname, father_name)
        self.name=name
    def display_name(self):
        print("The son name is:", self.name)
class daughter(father):
    def __init__(self, name,surname, father_name):
        super().__init__(surname, father_name)
        self.name=name
    def display_name(self):
        print("The daughter name is:", self.name)    
obj=son("Raj","k","likith")
obj.display_surname()
obj.display_name()

obj1=daughter("maria","s","rajesh")
obj1.display_surname()
obj.display_name()
