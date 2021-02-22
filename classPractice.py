class Person:
    def __init__(self, name, edad):
        self._name = name
        self._edad = edad
    
    def greetings(self):
        print(f"Hola {self._name}, yo soy un bot")

def main():
    person = Person("Enrique", 20)
    person.greetings()

if __name__ == "__main__":
    main() 