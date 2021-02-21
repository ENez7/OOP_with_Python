class Person:
    
    def __init__(self, name):
        self.name = name
    
    def moving(self):
        print('Walking')

class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def moving(self):
        print('Moving on a bicycle')

def main():
    person = Person('Jose')
    person.moving()
    
    cyclist = Cyclist('Daniel')
    cyclist.moving()

if __name__ == '__main__':
    main()
    