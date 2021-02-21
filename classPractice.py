class Person:
    def __init__(self, name, edad):
        self._name = name
        self._edad = edad
    
    def saludar(self):
        print(f"Hola {self._name}, yo soy un bot")

def main():
    #person = Person("Enrique", 20)
    #person.greetings()
    a = int(input("A: "))
    b = int(input("B: "))
    print(addition(a, b))
    print(substraction(a, b))

if __name__ == "__main__":
    main() 