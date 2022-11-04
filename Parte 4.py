# LESSONS ------------------------------------------------ --------------------------------------

# Create a class to perform operations of addition, subtraction, etc.
class  Arithmetic :

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandA
        self.operandoB = operating B

    def sumar_3(self):
        return  self.operandoA + self.operating B

    def restar_3(self):
        return  self.operandoA - self.operating B

    def multiplicar_3(self):
        return  self.operandoB * self.operating B

    def dividir_3(self):
        return  self.operandoA / self.operating B

arithmetic1  =  Arithmetic ( 4 , 5 )

print ( f'The result of the sum is { arithmetic1 . sum_3 () } ' )
print ( f'The result of the subtraction is { arithmetic1 . subtract_3 () } ' )
print ( f'The result of the multiplication is { arithmetic1 . multiply_3 () } ' )
print ( f'The result of the division is { arithmetic1 . divide_3 ():.2f } ' )

# Create a class to calculate the area of ​​a rectangle.
class Rectangulo:
    def  __init__ ( self , base , altura ):
        self.base = base
        self . height  =  height

    def calcular_area(self):
        return  self.base * self.altura

base  =  float ( input ( 'Please enter the base dimension: ' ))
height  =  float ( input ( 'Please enter the height value: ' ))

rectangle1  =  Rectangle ( base , height )

print ( f'The area of ​​the rectangle is: { rectangle1 . calculate_area ():.2f } m2' )

# Create a class to calculate the volume of a rectangle.
class  Cube :
    def  __init__ ( self , cubeLength , cubeWidth , cubeDepth ):
        self . length  =  cubelength
        self . width  =  cubewidth
        self . depth  =  cubedepth

    def calcular_volumen(self):
        return   self . long  *  self . width  *  self . depth

CubeLength  =  float ( input ( 'Enter the Length: ' ))
bucketWidth  =  float ( input ( 'Enter the width: ' ))
cubeDepth  =  float ( input ( 'Enter depth: ' ))

cube1  =  Cube ( cubeLength , cubeWidth , cubeDepth )
print ( f'The total volume is: { cube1 . calculate_volume ():.2f } m3' )

# Create a class to generate different types of people from an agenda. Implement the methods
#GET and SET on the name attribute. Define the last name attribute as "Read Only"
class Persona:
    def  __init__ ( self , firstname , lastname , age ):
        self . _name  =  name
        self . _surname  =  surname
        self . age  =  age

    @property
    def nombre(self):
        return  self . _Name

    @ name . setter
    def  name ( self , name ):
        self . _name  =  name

    @property
    def apellido(self):
        return self._apellido

    def  show_detail ( self ):
        print ( f'Person: { self . _name } , { self . _surname } . { self . age } years' )

person1  =  Person ( 'Jonathan' , 'Palomeque' , 30 )

print ( f'Person 1 Object: { person1 . _firstname } , { person1 . _lastname } , { person1 . age } ' )
Person . show_detail ( person1 )

# Create a class to generate different types of cars from a sales agency. Encapsulate and implement
# the GET and SET methods on all attributes (brand, color, age).
class Auto:
    def  __init__ ( self , brand , color , age ):
        self _ _brand  =  brand
        self._color = color
        self . _old  =  old

    @property
    def marca(self):
        return  self . _brand
    @ brand . setter
    def  brand ( self , brand ):
        self _ _brand  =  brand

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def antiguedad(self):
        return  self . _antiquity
    @ antiquity . setter
    def  age ( self , age ):
        self . _old  =  old

    def  show_detail ( self ):
        print(f'''Automovil: 
    Brand: { self . _brand }
    Color: {self._color} 
    Age: { self . _seniority } years
    ''')

auto1  =  Auto ( 'Fiat' , 'Rojo' , 10 )
car . show_detail ( auto1 )

# Inherit the characteristics of the parent class "Person", which is passed to the child class "Employees".
# Add the salary attribute
class  Employee ( Person ):
    def  __init__ ( self , first name , last name , age , salary ): # without this line it will give an error
        super (). __init__ ( first name , last name , age )
        self . salary  =  salary

    def  show_detail ( self ):
        print ( f''''Employee:
    Name: { self . _name }
    Surname: { self . _surname } 
    Age: { self . age } years
    Salary: $ { self . salary }
    ''')

employee1  =  Employee ( 'John' , 'Paez' , 28 , 50000 )
Employee . show_detail ( employee1 )

# Define the parent class "Vehicle" with the attributes: color and wheels, encapsulate and implement
# the get and set methods. Create the child classes:
# 1) Coach:
# Add the "speed" attribute. Encapsulate and implement methods
#2) Bike:
# Add the "type" attribute. Encapsulate and implement methods
class Vehiculo:
    def  __init__ ( self , color , wheels ):
        self._color = color
        self . _wheels  =  wheels

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return   self . _wheel
    @wheels . _ setter
    def  wheels ( self , wheels ):
        self . _wheels  =  wheels

    def __str__(self):
        return  f'Color: { self . color } , wheels: { self . wheels } '

class  Car ( Vehicle ):
    def  __init__ ( self , color , wheels , speed ):
        super (). __init__ ( color , wheels )
        self . _speed  =  speed

    @property
    def velocidad(self):
        return  self . _speed

    @ speed . setter
    def  speed ( self , speed ):
        self . _speed  =  speed

    def __str__(self):
        return  f'''Car:
        { super (). __str__ () } , speed: { self . _speed } km/hr'''

class  Bicycle ( Vehicle ):
    def  __init__ ( self , color , wheels , type ):
        super (). __init__ ( color , wheels )
        self . _type  =  type

    @property
    def tipo(self):
        return self._tipo

    @ type . setter
    def  type ( self , type ):
        self . _type  =  type

    def __str__(self):
        return   f'''Bicycle:
        { super (). __str__ () } , type: { self . _type } '' '

car1  =  Car ( 'blue' , 'four type A' , 100 )
print(coche1)

bike1  =  Bike ( 'red' , 'two C's' , 'mountain' )
print(bicicleta1)

#Create a Videogames class, which allows to have a videogame number ID counter
class  Videogame :
    game_counter  =  0

    @classmethod
    def  generate_next_value ( cls ):
        cls . game_counter  +=  1
        return  cls . counter_game

    def  __init__ ( self , name , platform ):
        self . game_id  =  Videogame . generate_next_value ()
        self . name  =  name
        self _ platform  =  platform

    def __str__(self):
        return  f'Videogame [ { self . game_id }  { self . name }  { self . platform } ]'


game1  =  Video Game ( 'Pokemon' , 'Nintendo' )
game2  =  Video game ( 'Mario Bross' , 'Nintendo' )
game3  =  Video game ( 'Mortal Kombat' , 'Play Station' )

print ( f'''Value Video game total counter: { Video game . game_counter }
    Game: { game1 . name }
    Counter: { game1 . game_id }
    Game: { game2 . name }
    Counter: { game2 . game_id }
    Game: { game3 . name }
    Counter: { game3 . game_id }
    ''')

# POLOMORPHISMO:
# Create a child class of the "Employee" class (developed in the first exercises), which
# will be called "Manager" and has the attributes: name, salary and department.
# Apply the concept of polymorphism.

class  Manager ( Employee ):
    def  __init__ ( self , first name , last name , age , salary , department ):
        super (). __init__ ( first name , last name , age , salary )
        self . department  =  department

    def __str__(self):
        return   f'Manager: Department { self . department } , { super (). __str__ () } '

def  print_details ( object ):
    print ( object )
    print(type(objeto))
    if  isinstance ( objeto , Gerente ):
        print ( object . department )

employee1  =  Employee ( 'John' , 'Paez' , 30 , 5000 )
print_details ( employee1 )

print('-'.center(50, '-'))

manager1  =  Manager ( 'Carla' , 'Maciel' , 29 , 20000 , 'Systems' )
print_details ( manager1 )

# PC World Laboratory:
# A) Create the parent class "DeviceInput" with the attributes: inputType and brand. Apply encapsulation
# and get and set methods
class DipositivoEntrada:

    def  __init__ ( self , inputType , flag ):
        self _ _typeInput  =  typeInput
        self _ _brand  =  brand

    @property
    def tipoEntrada(self):
        return self._tipoEntrada
    @ tipoEntrada . sets
    def  typeInput ( self , typeInput ):
        self _ _typeInput  =  typeInput

    @property
    def marca(self):
        return  self . _brand
    @ brand . setter
    def  brand ( self , brand ):
        self _ _brand  =  brand

    def __str__(self):
        print ( f'Features: { self . _entrytype } and { self . _mark } ' )

# B) Create the child class "Mouse" with the attributes: brand and inputType. incorporate the
# class variable "counterMice. Apply encapsulation.
class  Mouse ( InputDevice ):
    mousecounter  =  0

    def  __init__ ( self , flag , inputType ):
        mouse . counterMice  +=  1
        self._idRaton = Raton.contadorRatones
        super (). __init__ ( inputType , flag )

    def __str__(self):
        return  f' ID : { self . _idMouse } , flag: { self . _mark } , type Input: { self . _entryType } '

# C) Create the daughter class "Keyboard" with the attributes: brand and inputType. incorporate the
# class variable "keyboardcounter. Apply encapsulation.
class  Keyboard ( InputDevice ):

    counterKeyboards  =  0

    def  __init__ ( self , flag , inputType ):
        Keyboard . keyboardcounter  +=  1
        self . _idKeyboard  =  Keyboard . counter keyboards
        super (). __init__ ( flag , inputType )

    def __str__(self):
        return  f' ID: { self . _idKeyboard } , make: { self . _flag } , input type: { self . _entryType } '

# D)Create the "Monitor" class with the attributes: brand and size. incorporate the
# class variable "counterMonitors. Apply encapsulation and Get and Set methods.
class Monitor:
    MonitorCounter  =  0

    def  __init__ ( self , make , size ) : _
        monitor . counterMonitors  +=  1
        self._idMonitor = Monitor.contadorMonitores
        self _ _brand  =  brand
        self . _size = size _ _  _ _ 

    @property
    def idMonitor(self):
        return  self._idMonitor
    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    @property
    def marca(self):
        return  self . _brand
    @ brand . setter
    def  brand ( self , brand ):
        self _ _brand  =  brand

    @property
    def tamaño(self):
        return   self . _size _ _
    @ size . _ _ setter
    def  size ( self , size ) : _ _ _
        self . _size = size _ _  _ _ 

    def __str__(self):
        return  f'ID: { self . _idMonitor } , make: { self . _brand } ,size: { self . _size } Inches ' _

# E)Create the class "Computer" with the attributes: name, object references: monitor, keyboard
# and mouse. Add the class variable "counterComputers". Apply encapsulation and methods
# Get y Set.
class  Computer :

    Computercounter  =  0

    def  __init__ ( self , name , monitor , keyboard , mouse ):
        Computer . counterComputer  +=  1
        self . _idComputer  =   Computer . countercomputer
        self . _name  =  name
        self._monitor = monitor
        self . _keyboard  =  keyboard
        self._raton = raton

    @property
    def nombre(self):
        return   self . _Name
    @ name . setter
    def  name ( self , name ):
        self . _name  =  name

    @property
    def monitor(self):
        return self._monitor
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return   self . _keyboard
    @ keyboard . setter
    def  keyboard ( self , keyboard ):
        self . _keyboard  =  keyboard

    @property
    def raton(self):
        return self._raton
    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
        Id: {self._idComputadora} 
        Name: { self . _name }
        Monitor: {self._monitor}
        Keyboard: { self . _keyboard }
        Raton: {self._raton}
        '''

# xxxxxxxxxxxxxxxxxx ------------------------------------------------ ----------------------------
