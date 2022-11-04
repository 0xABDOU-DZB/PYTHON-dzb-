# Write a program that allows you to enter two numbers on the keyboard and then
# display addition, subtraction, multiplication, division, modulus and exponent
# of said numbers. The results should be displayed on the screen. The numbers must
# be requested only once.

value1  =  int ( input ( 'Please enter the first value: ' ))
value2  =  int ( input ( 'Please enter the second value: ' ))

#Addition:
suma = valor1 + valor2
print ( f'The result of the sum is: { sum } ' )
#Subtraction:
resta = valor1 - valor2
print ( f'The result of the subtraction is: { subtraction } ' )
#Multiplication:
multiplicacion = valor1 * valor2
print ( f'The result of the multiplication is : { multiplication } ' )
#Division:
division = valor1 / valor2
print ( f'The result of the division is: { division } ' )
#Modulo:
modulo = valor1 % valor2
print ( f'El modulo es: { modulo } ' )
#Exponent:
exponent  =  value1  **  value2
print ( f'Result of power is: { exponent } ' )

#Average of 4 grades of a student:

grade1  =  int ( input ( 'Enter the result of the first grade: ' ))
grade2  =  int ( input ( 'Enter the result of the second grade: ' ))
grade3  =  int ( input ( 'Enter the result of the third grade: ' ))
grade4  =  int ( input ( 'Enter the result of the fourth grade: ' ))

sumGrades =  grade1  +  grade2  +  grade3  +  grade4
average  =  sumGrades  /  4
print ( f' Total average is: { average } ' )

#Convert units, from tons to pounds:

valueTons  =  float ( input ( 'Enter the value in Tons: ' ))
tonsAKg  =  valueTons  *  1000
valorLibras  =  tonsAKg  *  2.2
print ( f'The result is: { valuePounds } pounds.' )

#Calculate the area and perimeter of a rectangle:

height  =  float ( input ( 'Please enter the height value in meters: ' ))
width  =  float ( input ( 'Please enter the width value in meters: ' ))
perimeter  =  high  *  2  +  ancho  *  2
area  =  height  *  width
print ( f'The value of the perimeter is { perimeter } meters and the value of the area is { area } m2' )

#The user enters the current year and the year of the date of his
# birth. Calculate and issue the age

aCurrent  =  int ( input ( 'Please enter the current year: ' ))
DateBirth  =  int ( input ( 'Please enter the year of your birth: ' ))
age  =  aCurrent  -  dateBirth
print ( f'Age is: { age } ' )

#Make a program that allows entering the existing kilometers between two
# cities and the average speed of a vehicle. Calculate and issue on screen
# the approximate time it will take to get from one point to another taking into account
# count the entered data.

distanceCities  =  float ( input ( ' Enter the distance between the two cities (in Km): ' ))
AverageSpeed  ​​=  float ( input ( ' Enter the average speed of the car (in Km/h): ' ))
estimatedtime  =  averagespeed  //  distanceCities
print ( f'The approximate time to arrive is { EstimatedTime } hours.' )

# A computer house pays its employees a fixed salary of ARS15000,
# plus a commission of 5% on the total billed by each employee. Make a
# program to enter the total billed by an employee and then calculate
# and issue on the screen the total salary to be received for it.

Fixedsalary  =  15000
commission  =  float ( input ( 'Enter the commission percentage: ' ))
subtotal  = ( Fixedsalary  *  commission ) /  100
SalaryTotal  =  SalaryFixed  +  subtotal
print ( f'The total salary that includes the 5% commission is $ { salaryTotal } ' )

# Make a program to enter by keyboard the total square meters of
# a property and the square meters covered; then compute and display by
# display the percentage of square meters covered and the percentage of
# square meters uncovered.

LandSurface  =  float ( input ( 'Enter the area of ​​the lot in m2 :' ))
CoverArea  =  float ( input ( 'Enter the covered area in m2: ' ))
UncoveredArea  =  GroundArea  -  CoveredArea
PercentCovered  = ( CoverArea  *  100 ) /  LandArea
UncoveredPercentage  = ( UncoveredArea  *  100 ) /  LandArea
print ( f' The percentage of meters covered is { percentageCovered } % and uncovered is { percentageDiscovered } %' )

# An important delivery chain has a time promotion
# limited in which it grants a 15% discount on the total value of the
# purchase made. Make a program to request the total amount and the same
# Calculate and display the total to be charged with the discount applied and the amount of the discount.

valuePurchase  =  float ( input ( 'Enter the value of the purchase: ' ))
discount  =  purchasevalue  * 0.15
totalACollect  =  valuePurchase  -  discount
print ( f'The discount is $ { discount } and the total amount to be paid with the discount included is $ { totalACollect } ' )

# A university wants to know the percentages of women and men in the
# careers in exact sciences. A program is requested to load the amount of
# women and the number of men and that it calculates and broadcasts on the screen
# the corresponding percentages.

numberMen  =  int ( input ( 'Enter the number of men: ' ))
numberWomen  =  int ( input ( 'Enter the number of women: ' ))
percentageMen  = ( numberMen  *  100 ) / ( numberWomen  +  numberMen )
percentageWomen  = ( numberWomen  *  100 ) / ( numberWomen  +  numberMen )
print ( f'The percentage of registered men is { percentageMen } % and of women { percentageWomen } %' )

#-------------------------------------------------------------------------------------------------------------------
#Determine which of the two values ​​is the greater

number1  =  int ( input ( 'Enter the first number: ' ))
number2  =  int ( input ( 'Enter the second number' ))

if numero1 > numero2:
    print ( f'The first number is the largest, { number1 } ' )
elif numero1 == numero2:
    print ( 'The numbers are equal' )
else:
    print ( f'The second number is the largest, { number2 } ' )

#Determine if the entered value is Even or Odd:

valueNumeric  =  int ( input ( 'Input a numeric value:' ))

if  numericvalue  %  2  ==  0 :
    print ( 'The number is even' )
else:
    print ( 'The number is odd' )

# Make a program to enter a number and then a billboard is issued by
# display “Positive” if the number is greater than zero, “Negative” if the number is
# less than zero or “Zero” if the number is equal to zero.

numberEvaludo  =  int ( input ( 'Enter the numerical value to evaluate: ' ))

if numeroEvaludo > 0 :
    print ( f'The number { evaluatedNumber } , is positive' )
elif numeroEvaludo < 0:
    print ( f'The number { evaluatedNumber } , is negative' )
else:
    print ( f'The number { EvaluatedNumber } , is zero and therefore neutral' )

# A video game house grants a discount depending on the amount of the
# purchase made according to the following values:
# • If the amount is less than ARS 1000, there is no discount.
# • If the amount is ARS 1,000 or more but less than ARS 5,000, a
# 10% discount.
# • If the amount is ARS 5000 or more, an 18% discount applies.

amountPurchase  =  float ( input ( 'Enter the purchase amount: ' ))
importeConDescuento = None

if importeCompra < 1000:
    print ( f'The amount is less than requested, therefore there is no discount. Amount to pay: $ { importPurchase } ' )
elif importeCompra >= 1000 and importeCompra < 5000:
    importeConDescuento  =  importeCompra  *  0.90
    print ( f' A discount of 10% is applied. The amount to be paid is $ { importWithDiscount } ' )
elif importeCompra >= 5000:
    importeConDescuento  =  importeCompra  *  0.82
    print ( f'A discount of 18% is applied. The amount to be paid is $ { importWithDiscount } ' )

# Make a program to enter a value that will be expressed in minutes. Yes
# the minutes exceed 60, pass the value to hours, otherwise leave it in
# minutes. Show the result on the screen clarifying if minutes or
# hours.

minutes  =  int ( input ( 'Enter the amount in minutes: ' ))
valueEnHs  =  None

if minutos >= 60:
    valueEnHs  =  minutes  /  60
    print ( f' The result in hours is from { valueInHs } hs' )
else:
    print ( f'It is not necessary to pass to hours. The result in minutes is { minutes } ' )

#Range to establish between 0 to 5. Inform if it is within the range

inputValue  =  int ( input ( 'Write the value: ' ))
minimumValue  =  0
maxValue  =  5
withinRange  = ( EnteredValue  >=  MinimumValue ) and ( EnteredValue  <=  MaximumValue )

if dentroDeRango:
    print ( 'It is within range' )
else:
    print ( 'is not within the range' )

#The user must enter the month in which it is and the program must indicate the
#season

month  =  int ( input ( 'enter a month of the year (1-12): ' ))
parking  =  None

if mes == 1 or mes == 2 or mes == 3:
    season  =  'Winter'
elif mes == 4 or mes == 5 or mes == 6:
    season  =  'Spring'
elif mes == 7 or mes == 8 or mes == 9:
    season  =  'Summer'
elif mes == 10 or mes == 10 or mes == 12:
    season  =  'Autumn'
else:
    print ( 'Enter a value within the range 1 to 12' )

print ( f'For the month { month } , the season is { season } ' )

# Make a program that prompts for a number to be entered and then outputs a
# poster on the screen clarifying if it is a multiple of 5.
numMultiple  =  int ( input ( 'Enter the value to query: ' ))

if numMultiplo % 5 == 0:
    print ( f'The number { numMultiple } is a multiple of 5' )
else:
    print ( f'The number { numMultiple } is not a multiple of 5' )

# Make a program that asks for the input of two numbers and then calculate:
# a. The subtraction if the first is greater than the second.
# b. The sum if they are equal.
# c. The product if the first is less.
# A poster should be issued per screen with the corresponding result.

num1  =  int ( input ( 'Enter the first number: ' ))
num2  =  int ( input ( 'Enter the second number: ' ))
result  =  None

if num1 > num2:
    result  =  num1  -  num2
    print ( f' The subtraction of the numbers was carried out and the result is: { result } ' )
elif num1 == num2:
    result  =  num1  +  num2
    print ( f'A sum was performed, the result is { result } ' )
else:
    result  =  num1  *  num2
    print ( f'The product was calculated, the result is { result } ' )

# Make a program to input two numbers. If the second is different from
# zero, calculate the division of the first by the second and display the result by
# screen; Otherwise, issue a notice clarifying that it cannot be divided by
# zero.
value_1  =  int ( input ( 'Enter the first number: ' ))
value_2  =  int ( input ( 'Enter the second number: ' ))
resul = None

if valor_2 != 0:
     result =  value_1 / value_2  
    print ( f'The result of the division is { result } ' )
else:
    print ( 'Cannot divide by zero' )

# An important liquid disinfectant business offers discounts
# depending on the number of liters sold according to the following scale:
# a. If you sell less than 100 litres, there is no discount.
# b. If you sell between 101 and 300 liters, the discount is 10%.
# c. If you sell between 301 and 500 litres, the discount is 15%.
# d. Finally, if the sale is more than 500 liters, the discount is 25%.
# Make a program that requests the entry of the total amount of the sale and the
# number of liters sold and calculate and issue the amount with the discount
# applied.

quantityLitrosSold  =  float ( input ( 'Enter the quantity of liters sold: ' ))
amountWithoutDiscount  =  float ( input ( 'Enter the amount to be charged: ' ))
totalAbonar = None

if  quantityLitersSold  <=  100 :
    print ( f'Discount is not applied, you must pay $ { undiscounted amount } ' )
elif cantidadLitrosVendidos > 100 and cantidadLitrosVendidos <= 300:
    totalPay  =  amountWithoutDiscount  *  0.9
    print ( f'A discount of 10% is applied and the amount to be charged is $ { totalAbonar } ' )
elif cantidadLitrosVendidos > 300 and cantidadLitrosVendidos < 500:
    totalPay  =  amountWithoutDiscount  *  0.85
    print ( f'A discount of 15% is applied and the amount to pay is $ { totalAbonar } ' )
else:
    totalPay =  amountWithoutDiscount  *  0.75
    print ( f'A discount of 25% is applied and the amount to be paid is $ { totalAbonar } ' )

# Write a program to enter by keyboard the length of the three sides of a
# triangle and then determine and report with an explanatory sign to what type
# of triangle corresponds:
# a. Equilateral: when all three sides are equal.
# b. Isosceles: when two of the three sides are equal.
# c. Scalene: when all the sides are different.

long1  =  float ( input ( 'Enter the length of the first side: ' ))
long2  =  float ( input ( 'Enter the length of the second side: ' ))
long3  =  float ( input ( 'Enter the length of the third side: ' ))

if  long1  ==  long2 and long1 == long3 :    
    print ( 'The triangle is equilateral, it has three equal sides' )
elif long1 == long2 or  long2 == long3 or long3 == long1:
    print ( 'The triangle is isosceles, two of its sides are equal' )
else:
    print ( 'The triangle is scalene, none of its sides are equal' )
