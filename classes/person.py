class Person:
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print(f'Hi, I am {self.name}')


person1 = Person("Madhav Paudel")
person1.talk()

person2 = Person("Ravi Mathya")
person2.talk()
