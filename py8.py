#Question.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

#Answer
class circle:
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius
    def getCircumference(self):
        return 2 * 3.14 * self.radius
t1 = circle(5)
print(t1.__doc__)
print("area of circle is ", t1.getArea())
print('circumference of circle is {}'.format(t1.getCircumference()))


#Question.2- Create a Student class and initialize it with name and roll number. Make methods to :
# Display - It should display all informations of the student.
# setAge - It should assign age to student 3. setMarks - It should assign marks to the student.

#Answer
class Student:
    def __init__(self, name, rno):
        self.n = name
        self.r = rno

    def Display(self):
        print('name {}\n rollno of {}'.format(self.n, self.r))

    def setAge(self, age):
        self.age = age
        print('here we have set age of {} as {} '.format(self.n, self.age))

    def setMarks(self, m):
        self.marks = m
        print('here we have set marks of {}  as {} '.format(self.n, self.marks))


t1 = Student('Saurav', 1610991785)
t1.Display()
t1.setAge(20)
t1.setMarks(90)


# Q.3- Create a Temprature class and create two methods:
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

#Answer
class Temprature:
    def __init__(self):
        print("converting Temprature")

    def convertFahrenheit(self, c):
        self.c = c
        print('the {}C ->{}F'.format(self.c, ((self.c * 9 / 5) + 32)))

    def convertCelsius(self, f):
        self.f = f
        print('the {}F ->{}C'.format(self.f, ((self.f - 32) * 5 / 9)))


t1 = Temprature()
t1.convertFahrenheit(-10)
t1.convertCelsius(0);


# Question.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
# Make methods to
# 1. Display the details.
# 2. Add the movie details.

#Answer
class MovieDetails:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("Create a class MovieDetails")

    def display(self):
        print('artist name {}\n year of release {}\n ratings {} star'.format(self.a, self.b, self.c))

    def setaddmoviedetails(self, actorname):
        self.ac = actorname
        print('actorname added now using setter fun is {}'.format(self.ac))


t1 = MovieDetails('Emran', 2006, 5)
t1.display()
t1.setaddmoviedetails('Jannat')


# Question.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
# Answer
class Animal:
    def animal_attribute(self):
        print("base clas animal_attribute ")


class Tiger(Animal):
    def dis(self):
        print("derievd class called")


r = Tiger()
r.dis()
r.animal_attribute()


# Question.6
# Answer is A B
#        A B


# Question.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.

#Answer
class Shape:
    def __init__(self, ll, bb):
        self.l = ll
        self.b = bb

    def Area(self):
        '''area method created'''

class rectangle(Shape):

    def Area(self):
        print('area of rectangle is ', (self.l * self.b))


class square(Shape):

    def Area(self):
        print('area of square is ', (self.l * self.l))


r = rectangle(2, 4)
r.Area()
q = square(2,5)
q.Area()
