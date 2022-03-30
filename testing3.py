import csv

#Animal class
class Animal:

    # __a="animal private artibute"
    # _b="animal protected artibute"

    def __init__(self,name:str,gender):

        assert isinstance(name,str),f"this {name} is not a string"

        self.name=name
        self.gender=gender
        
        self.__a="private artribute"
        self._b="protected artribute"

    def greeting(self):
        print(self._b)

    @classmethod
    def greeting_from_class(cls):
        print("hello class")
        print(cls)

    def readeCSV(self):
       with open("./items.csv") as f:
           reader=csv.DictReader(f)
           lists= list(reader)
        #    print(lists)
           for i in lists:
               created_instance=Animal(i.get("name"),i.get("gender"))
               print(created_instance)
    
    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    @staticmethod  #static method dont need to pass class creation instance like class method or normal methods in class
    def is_integer():
        print("it is integer")     
                    

#Dog class

class Dog(Animal):
    def __init__(self,name,gender,animal_type):
        super().__init__(name,gender)
        # self.name=name
        # self.gender=gender
        self.animal_type=animal_type




# Cat =Animal("Kuu","male")
# # Cat.greeting_from_class()
# # Animal.greeting_from_class()
# # Cat.readeCSV()
# # Cat.is_integer()
# Bony =Dog("boo","male","dog")
# print(Bony.__dict__)
# print(Bony)


