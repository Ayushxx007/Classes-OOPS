from abc import ABC, abstractmethod;   #abstract base class


class Animal(ABC):
    kingdom="animalia"  # class level variable

    def __init__(self, name,age):          #constructor
        self.name = name       # instance variable (public)
        self._age = age         # protected
        self.__dna="secret";    #encapsulation/data hiding  private

    @property
    def age(self):            # getters (abstracted access)
        return self._age;
    @age.setter
    def age(self,value):                  # setters
        if value < 0:
            return ValueError("Age cannot be negative");
        self._age = value;

    @abstractmethod        #abstract method
    def speak(self):
        pass;

    @abstractmethod      #abstract method
    def move(self):
        pass;

    def describe(self):       # instance method
        return print(f"{self.name} is {self.age} years old ,kingdom is {self.kingdom}");

    @classmethod    # class method
    def get_kingdom(cls):
        return cls.kingdom;

    @staticmethod    # static method
    def is_alive(status):
        return "Alive" if status else "Dead";



class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age);     # calling parent constructor
        self.breed = breed;


    def speak(self):                # polymorphism
        return f"{self.name} is {self.age} years old ,breed is {self.breed}";

    def move(self):
        return f"{self.name} has four legs"

    def fetch(self,item="ball",times=1):
        return f"{self.name} fetches {item}*{times} times";


class Bird(Animal):
    def __init__(self, name, age,can_fly=True):
        super().__init__(name, age);
        self.can_fly = can_fly;

    def speak(self):
        return f"{self.name} says:tweet"

    def move(self):
        action="flies" if self.can_fly else "walks"
        return f"{self.name}  {action}";



class Guard:
    def protect(self):
        return "Guarding";
    def alert(self):
        return "Alerting";



class PoliceDog(Animal,Guard):     # multiple inheritence
    def __init__(self, name, age,badge_number):
        super().__init__(name, age);
        self.badge_number = badge_number;

    def speak(self):
        return f"Officer {self.name} barks: woof woof"

    def move(self):
        return f"{self.name} has four legs"


class Puppy(Dog):
    def __init__(self, name, age,breed):
        super().__init__(name,age,breed=breed);

    def speak(self):
        return f"{self.name} says:puppy"
    def move(self):
        return f"{self.name} has four legs"






d1=Dog("guarand",33,"street");
d2=PoliceDog("puffy",33,11);














