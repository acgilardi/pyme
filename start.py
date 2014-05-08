from models import *

MyPerson = person.Person('bob', 'jones', 54)
MyCar = car.Car('name')

print "his name was %s %s and he was %i years old" % \
      (MyPerson.first_name, MyPerson.last_name, MyPerson.age)


for random_number in generator.lottery():
    print "And the next number is %d" % random_number





