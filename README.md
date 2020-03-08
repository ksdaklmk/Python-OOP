# Object-oriented programming in Python

Object-oriented programming (OOP) means that programs have a strong tendency of being organised around data, or objects, rather than functions and logic. That means a class represents the idea or concept behind something more tangible, like an actual object reasonably specific to your business. For example, when working on an education program, a class could be a student, teacher, or classroom.

With Python, it certainly can be used as a scripting language, it is designed as an object-oriented programming language.

### Prerequisites
Basic knowledge of Python programming is required. Watch the following YouTube videos to recap your Python skills:

**Basic Python 3 - Part 1**

[![Part 1](http://img.youtube.com/vi/Jw3h06aIHYk/0.jpg)](http://www.youtube.com/watch?v=Jw3h06aIHYk)

**Basic Python 3 - Part 2**

[![Part 1](http://img.youtube.com/vi/I_fpG3wrVaQ/0.jpg)](http://www.youtube.com/watch?v=I_fpG3wrVaQ)

### Topics
1. Classes and instances
2. Class variables
3. Class and static methods
4. Inheritance
5. Special methods

### 1. Classes and instances

```python
class Car():

    def __init__(self, maker, year):
        self.maker = maker
        self.year = year
        self.status = 'dirty'
    
    def clean():
        print('... cleaning the car!')
        self.status = 'clean'


my_car = Car('Honda', 2020)
print(my_car.maker)
print(f'The car is in {my_car.status} status')
my_car.clean()
print(f'The car is now in {my_car.status} status')
```
