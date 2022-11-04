# CICLO WHILE    ---------------------------------------------------------------------------
#increase value from 2 to 2, until reaching 250:
contador = 0

while contador <= 250:
    print ( f'The value is: { counter } ' )
    contador += 2
else:
    print ( 'End of loop' )

# Make a program that displays the numbers from 1 to 100 by 5 by 5. Example:
# 0, 5, 10, 15, 20.... 100.
cont = 0

while cont <= 100:
    print(cont)
    cont += 5
else:
    print ( 'End of loop' )

# Make a program to display the numbers from 10 to 1. It should not be done
# no request for data. USING WHILE.
cont1_  =  10

while cont1_ >= 1:
    print(cont1_)
    cont1_  -=  1

# Make a program that requests the age of a group of people. The program
# should ask for ages until an age less than 18 is entered. shall
# show on the screen how many seniors have registered.
countPerOlder  =  0
age  =  int ( input ( 'Enter age: ' ))

while edad >= 18:
    countPerOlder  +=  1
    age  =  int ( input ( 'Enter age: ' ))
else:
    print ( f'The number of people over 18 years of age is { countPerOlder } ' )

# Make a program that asks for two numbers and then displays the numbers
# between the smallest and the largest of them. Remember, using While.
n1  =  int ( input ( 'Enter the first number: ' ))
n2  =  int ( input ( 'Enter the second number: ' ))

if n1 > n2:
    largest_  =  n1
    minor_  =  n2
else:
    mayor_  =  n2
    smallest_  =  n1
while menor_ < mayor_:
    print(menor_)
    smallest_  +=  1

# Make a program that asks for ONE number and then calculates and outputs a billboard
# clarification if it is prime or not prime.
with_cousins  ​​=  0
laps_primes  =  1

v1  =  int ( input ( 'Enter the value to evaluate: ' ))

while  returns_primes  <=  v1 :
    if  v1  %  laps_primes  ==  0 :
        with_cousins  ​​+=  1
    laps_primes  +=  1

if  with_primes  ==  2 :
    print ( 'The number is prime' )
else:
    print ( 'Number is not prime' )

# Make a program that asks for a list of numbers that it cuts when
# enter a zero and then display the maximum of them and the position
# in which it was entered.
number  =  int ( input ( 'Please enter the number: ' ))
contNumber = 0
maxNumber = None

while number != 0:
    if contNumber == 0:
        maxNumber = number
    elif number > maxNumber:
        maxNumber = number
    contNumber += 1
    number  =  int ( input ( 'Please enter the number: ' ))
else:
    print ( f'The largest number is { maxNumber } and was entered at position { contNumber } ' )

# Make a program that asks for a list of numbers that it cuts when
# enter a zero and then display the smallest and second smallest.
#also indicate the position in which each of the minima was found.
number_  =  int ( input ( 'Please enter the number: ' ))
pGlobal = 0
minNumber1_  ​​=  None
minNumber2_  =  None
pMin1  =  0
pMin2  =  0

while number_ != 0:
    if pGlobal == 0:
        minNumber1_  ​​=  number_
        pMin1  +=  1
        pGlobal += 1
    elif  number_  <  minNumber1_ ​​:
        minNumber2_  =  minNumber1_
        minNumber1_  ​​=  number_
        pMin2  =  pMin1
        pMin1  =  pGlobal
    number_  =  int ( input ( 'Please enter the number: ' ))
    pGlobal += 1
else:
    print ( f'The smallest number is { minNumber1_ ​​} and was entered at position { pMin1 } , the second smallest is { minNumber2_ } '
          f'y was entered at position { pMin2 } ' )

# Make a program that asks for a list of numbers that it cuts when
# enter a zero and then display the maximum of the numbers
# negative and the minimum of the positive numbers.
ban_ = 0
maxNeg = 0
minPos = 0
input_num  =  int ( input ( 'Enter the number: ' ))

while  num_entered  !=  0 :
    if  ban_  ==  0 :
        if  num_entered  >  0 :
            minPos  =  num_incomes
        else:
            maxNeg  =  num_incomes
        ban_ += 1
    elif minPos == 0 or maxNeg == 0:
        if  minPos  ==  0  and  num_entries  >  0 :
            minPos  =  num_incomes
        elif  maxNeg  ==  0  and  num_entered  <  0 :
            maxNeg  =  num_incomes
    if  num_entered  <  0  and  num_entered  <  maxNeg :
        maxNeg  =  num_incomes
    if  num_entered  >=  1  and  num_entered  <  minPos :
        minPos  =  num_incomes
    input_num  =  int ( input ( 'Enter the number: ' ))
else:
    print ( f'The maximum of the negative numbers is { maxNeg } and the minimum of the positive ones is { minPos } ' )

# Make a program to input a list of numbers that cuts when
# enter a zero then display: the number of prime numbers, the number of
# even numbers, the number of positives and the number of negatives.
cantPri_ = 0
cantPares_ = 0
cantPositv_ = 0
cantNega_  =  0
nEntered_  =  int ( input ( 'Enter the number: ' ))

while nIngresado_ != 0:
    if nIngresado_ > 0:
        cantPositv_ += 1
    else:
        cantNega_  +=  1
    if  nEntered_  %  2  ==  0 :
        cantPares_ += 1
    contPri_ = 0
    c = 1
    while c <= nIngresado_:
        if nIngresado_ % c == 0:
            contPri_ +=1
        c += 1
    if contPri_ == 2:
        cantPri_ += 1
    nEntered_  =  int ( input ( 'Enter the number: ' ))
else:
    print ( f''''The amount of:
            prime numbers: { cantPri_ } ,
            even numbers: { cantPares_ } ,
            positive numbers: { cantPositv_ } ,
            negative numbers: { cantNega_ } ''' )

#CYCLE FOR ----------------------------------------------- ------------------------------
# Make a program to display the numbers 1 to 10. It should not be done
# no request for data.
counter1  =  0

for x in range(10):
    counter1  +=  1
    print(contador1)

# Make a program to display the numbers from 10 to 1. It should not be done
# no request for data.
counter2  =  11

for x in range(10):
    counter2  -=  1
    print(contador2)

# iterate a range from 0 to 10 and print divisible numbers
# between 3

for  i  in  range ( 10 ):
    if i % 3 == 0:
        print(i)
else:
    print ( 'End of loop' )

# Write a program that asks for the entry of 10 numbers and that shows the
# largest of them per screen. Only ONE value should be output per screen.
numbers  = []
valor = None
largestNumber  =  0

for x in range(10):
    value  =  int ( input ( 'Enter value: ' ))
    numbers _ append ( value )
    if valor > numeroMayor:
        largestNumber  =  value

print ( f'The highest number is { highestNumber } , end of loop' )

# Make a program that asks for 20 numbers and calculates and outputs to the screen
# how many are positive (greater than zero). A single value should be displayed: the
# final countdown.
numerosEvaluar = []
positivecounter  =  0
valor1 = None

for x in range(20):
    value1  =  int ( input ( 'Enter value: ' ))
    numerosEvaluar.append(valor1)
    if valor1 > 0:
        positivecounter  +=  1

print ( f'The number of positive numbers are: { positivecounter } ' )

# Make a program that asks for ONE number and then calculates and outputs a billboard
# clarification if it is prime or not prime.

cont = 0
value =  int ( input ( 'Enter values: ' ))

for x in range(1, valor):
    if  valor % x == 0:
        cont += 1

if cont == 2:
    print ( 'The number is prime' )
else:
    print ( 'Not prime' )

# Make a program that requests 10 numbers and then display the
# maximum of them and the position in which it was entered.
numMayor  =  0
countPosition  =  0

for x in range(10):
    values  ​​=  int ( input ( 'Please enter the value: ' ))
    if valores > numMayor:
        nummajor  =  values
        contPosicion = x +1

print ( f' The largest number is { numMajor } and it was entered at position { contPosition } ' )

# Make a program that requests 20 numbers and then display the
# least of them and the position in which it was found.
numMen  =  None
minPosition  =  None

for x in range(20):
    minimumValues  ​​=  int ( input ( 'Please enter the value: ' ))
    if x == 0:
        numMen  =  valoresMinimos
    elif  valoresMinimos  <  numMen :
        numMen  =  valoresMinimos
        minPosition  =  x  +  1
else:
    print ( f'The smallest number is { numMenu } and it was entered in position { minimumPosition } ' )

# Make a program that asks for 20 ages and then calculates the average age
# of those over 18 years of age.
AverageCount_  =  0
addAges  =  0

for  z  in  range ( 20 ):
    ages_  =  int ( input ( 'Please enter ages: ' ))
    if edades_ > 18:
        addAges  =  addAges  +  ages_
        averageCount_  +=  1

averageAge_  =  sumAge  /  AverageCount_
print ( f'The average age is: { averageEdades_ } ' )

# Make a program that asks for 20 numbers and then output the number to the screen
# maximum of even numbers and minimum of odd numbers.
maxPar_ = 0
minOdd_  =  0

for m in range(20):
    parOImpar  =  int ( input ( 'Enter numbers: ' ))
    if  parOImpar  %  2  ==  0 :
        if  parOImpar  >  maxPar_ :
            maxPar_  =  parOImpar
    else:
        if parOImpar < minImpar_:
            minImpar_  =  parOImpar

print ( f' The maximum of even numbers is { maxEven_ } and the minimum of odd numbers is { minOdd_ } ' )

#FUNCTIONS ------------------------------------------------ -----------------------------

# Make a function called “product” that takes two integers and
# return the product of both. Then make a program that asks for the price
# of an item and the quantity sold and display the total amount to be sold.
# to pay. Use the function.
def  product ( nu1 , nu2 ):
    return   now1  *  now2

preProduc  =  float ( input ( 'Enter product price: ' ))
cantVen  =  int ( input ( 'Enter the quantity of products: ' ))

amTot  =  product ( preProduc , qtyVen )
print ( f'Total amount is $ { monTot } ' )

# Create a function to calculate the total of a payment including an applied tax.
# The function is called calculate_total, it receives two parameters:
## 1. payment_without_tax
## 2. tax (Ex. Value of 10 means 10% tax, value of 16 means 16% tax)
## The function should return the total payment including the percentage of tax provided.
## Ex. If we call the function calculate_total(1000, 16)
# should return the value 1,160.0
# The values ​​must be provided by the user and processed with the input function, converting them to float type.

def  calculate_total ( payment_without_taxes_ , taxes2 ):
    return  payment_without_taxes_  +  payment_without_taxes_  * ( taxes2 / 100 )

payment_without_taxes_  =  float ( input ( 'Please enter the amount to be paid without taxes: $ ' ))
tax2  =  float ( input ( 'Please enter the percentage of tax (%): ' ))

payment_with_tax_  =  calculate_total ( payment_without_tax_ , tax2 )

print ( f'Total payment is: $ { payment_with_tax_ } ' )

# Make a function called “greater” that takes two integers and
# return the largest of them or zero if they are equal.
def  mayor ( v_n1 , v_n2 ):
    if  v_n1  >  v_n2 :
        return v_n1
    elif  v_n1  ==  v_n2 :
        return 0
    else:
        return v_n2

no1  =  int ( input ( 'Enter the first value: ' ))
no2  =  int ( input ( 'Enter the second value: ' ))
res_ = mayor(no1, no2)
print(res_)

# Make a function called “even” that takes an integer and returns 1 if
# is even or zero if not. Write a program to enter 20 numbers and
# display how many are even.
def par(number_123):
    if number_123 % 2 == 0:
        return  1
    else:
        return 0

peer_count  =  0
numberIRequest  =  int ( input ( 'Enter the numeric value: ' ))

for g in range(20):
    if par(numeroQuePido) == 1:
        peer_count  +=  1
    g += 1
    numberIRequest  =  int ( input ( 'Enter the numeric value: ' ))
else:
    print ( f'The number of even numbers is: { counter_ofPairs } ' )

# Make a function called "prime" that takes an integer and returns 1
# if the number is prime or zero if it is not. Make a program to enter
# numbers. The batch cuts when a zero number is entered. report the
# average considering only prime numbers.
def  first ( ent ):
    acc = 0
    for x in range(1, ent + 1):
        if ent % x == 0:
            acc += 1
    if acc == 2:
        return  1
    else:
        return 0

integer_  =  int ( input ( 'Enter the number: ' ))
pNum_  =  0
with_cousins  ​​=  0

 while enter_  ! =  0 :
    res_do  =  prime ( integer_ )
    if  res_do  ==  1 :
        pNum_  +=  integer_
        with_cousins  ​​+=  1
    integer_  =  int ( input ( 'Enter the number: ' ))
    res_do = 0
else:
    pro_pr  =  pNum_  //  with_primes
    print ( f'The average with the prime numbers is { pro_pr } ' )

# Make a function called “payments” that receives an amount (float) and an amount
# of payments (integer) and return the amount of each payment. make a program for
# enter 10 sales. For each sale, the amount and amount of payments are known.
# The program should display the number of payments and the amount of the payment to
# each of the sales.
def pagos(mon, cuo):
    return mon / cuo

for m in range(10):
    amount_  =  float ( input ( 'Enter the amount: $ ' ))
    installments_  =  int ( input ( 'Enter the number of installments: ' ))
    total_quota  =  payments ( amount_ , installments_ )
    print ( f'The total amount is { amount_ } , it will be paid in { quotas_ } installments of $ { total_cuo } each' )

# Make a function called posNegZero” that receives a number for value and a variable for
# reference. That parse the number and write variable received by reference
# con:
# a. 1 if the number is positive.
# b. -1 if the number is negative.
# c. 0 if the number is zero.
# Make a main program that allows us to enter 100 numbers and issue by
# display how many are positive, how many are negative, and how many are zero.
def posNegCero(n, j):
    if n == 0:
        j = 0
    elif n > 0:
        j = 1
    else:
        j = -1
    return   j

accPos  =  0
accNeg  =  0
accCero  =  0
ban_dera = None

for  f  in  range ( 5 ):
    n  =  int ( input ( 'Enter a number: ' ))
    flag_flag  =  posNegZero ( n , flag_flag )
    if  ban_dera  ==  0 :
        accCero  + =  1
    elif  ban_dera  ==  1 :
        accPos  +=  1
    else:
        accNeg  +=  1
else:
    print ( f'number of positives { accPos } , number of negatives { accNeg } '
          f' and the number of zeros { accZero } ' )

# Write a program that allows you to enter a list of numbers that cuts
# when a zero is entered. Based on said data, report:
# a. The largest of the even numbers.
# b. The number of odd numbers.
# c. The smallest of the prime numbers.
# Make use of the previously developed functions.
number_n  =  int ( input ( 'Enter the number: ' ))
mayNum_pairs  =  0
accPrimos_0  =  0
menuNum_odd  =  0

while number_n !=0:
    if par(number_n) == 1:
        if mayNum_pares == 0:
            mayNum_pares = number_n
        elif number_n >mayNum_pares:
            mayNum_pares = number_n
    else:
        if  menuNum_odd  ==  0 :
            menuNum_odd  =  number_n
        elif  number_n  <  menNum_odd :
            menuNum_odd  =  number_n
    if primo(number_n) == 1:
        accPrimos_0  +=  1
    number_n  =  int ( input ( 'Enter the number: ' ))
else:
    print ( f'The greatest of the pairs is { mayNum_pares } , the least of the odds is { menNum_impares } '
          f' and the number of prime numbers is { accPrimos_0 } ' )

#LISTS ------------------------------------------------ ----------------------------
# Given the following tuple, create a list that only includes
# numbers less than 5 using a for loop.
double  = ( 13 , 1 , 8 , 3 , 2 , 5 , 8 )
list  = []

for  t  in  tupla :
    if t < 5:
        lista.append(t)
else:
    print ( f'Numbers less than 5 are: { list } ' )

# Transform each number of the list that was formed in the previous exercise
# , multiplying it by 2

for  o  in  range ( len ( list )):
    list [ o ] =  list [ o ] *  2
else:
    print ( f'The result of the values ​​of the list multiplied by 2 is: { list } ' )

# Make a program to enter five different numbers, form a list,
# and then display the largest and smallest of them.
list1_  = []
x = 0

while x in range(5):
    num_lista1_  =  int ( input ( 'Enter the number: ' ))
    lista1_.append(num_lista1_)
    x += 1
else:
    print ( f'The largest value is { max ( list1_ ) } and the smallest is { min ( list1_ ) } ' )

# Make a program to input four numbers, form a list
# and then show why they are greater than 100.
lista2_  = []
q = 0

for  q  in  range ( 4 ):
    numb_lista2 = int(input('Ingrese el numero: '))
    lista2_.append(numb_lista2)
    q += 1

def  mayor100 ( name ):
    return (nume > 100)

largest_numbers  =  list ( filter ( largest100 , list2_ ))
print ( f'numbers greater than 100 are: { greater_numbers } ' )

# Make a program to input four numbers, form a list
# and then display by how many are less than 100.
list_3 = []
s = 0

for  s  in  range ( 4 ):
    val_num  =  int ( input ( 'Enter the number: ' ))
    list_3.append(val_num)
    s += 1

def menor100_(numer):
    return  numer < 100

menores_100 = list(filter(menor100_, list_3))
print ( f'Numbers less than 100 are : { less_100 } ' )

# Make a program that requests 50 integers and stores them in a vector.
# Then loop through the vector and determine and report what the sum of the values ​​is
# of the same.
vector1 =[]

for d in range(50):
    num_vector1  =  int ( input ( 'Enter the number: ' ))
    vector1.append(num_vector1)
    d += 1

sumValVec = 0
for numerosVector in vector1:
    sumValVec += vector1[numerosVector]
else:
    print ( f'The sum of the values ​​gives a total of { sumValVec } ' )

# Make a program that requests 50 integers and stores them in a vector.
# Then iterate through all the elements of the vector and determine what the value is
# maximum and its position within the vector.
vector2 = []

for x1 in range(50):
    num_vector2  =  int ( input ( 'Enter the number: ' ))
    vector2.append(num_vector2)
    x1  +=  1

contIndiceVector2 = 1
valMaxVector2 = vector2[0]
posValMaxV2 = 0

for v2 in vector2:
    if v2 > valMaxVector2:
        valMaxVector2  =  v2
        posValMaxV2 = contIndiceVector2
    contIndiceVector2 += 1
else:
    print ( f'The largest number is { valMaxVector2 } and it was entered at position { posValMaxV2 } ' )

# Make a program that requests 100 integers and stores them in a
# vector. Then loop through that vector to compute the average. show by
# display the vector values ​​that are greater than the calculated average.
vector3 = []

for ab in range(100):
    numVector3  =  int ( input ( 'Enter value: ' ))
    vector3.append(numVector3)

sumVector3 = 0
for  v3  in  vector3 :
    sumVector3  +=  v3
promVector3 = sumVector3 / len(vector3)

vector3MayPro = []
for v3_ in vector3:
    if v3_ > promVector3:
        vector3MayPro.append(v3_)

print ( f'The average is: { avgVector3 } and the values ​​greater than the average are: { vector3MayPro } ' )

# Given a list of 10 integers, load them into a vector. Later,
# determine and report whether the vector is ordered in increasing order. By
# example the vector with the values ​​1, 3, 5, 7 and 9 is sorted; the vector 1, 5, 3, 7
# and 9 is not.
vector4 = []

for bc in range(10):
    numVector4  =  int ( input ( 'Enter value: ' ))
    vector4.append(numVector4)

banVector4 = 1
maxVector4 = vector4[0]

for v4 in vector4:
    if v4 >= maxVector4:
        maxVector4  =  v4
    else:
        banVector4 = 0
        break

if banVector4 == 1:
    print ( f'Values ​​are sorted: { vector4 } ' )
else:
    print ( f'Values ​​are out of order: { vector4 } ' )

# Make a program that requests a series of values ​​of type char (characters).
# Character is understood as each element that is obtained by pressing a
# key. For example the value “25” has two characters (if we wanted to save it
# in integer variables we are enough with one, but if we want to save it in
# char variables, we'll need two); the phrase "maxi program" has 13 (it
# includes the space as a character).
# The number of values ​​will be at most 50, but the program can cut
# before if the character “.” (point). Once the char vector is loaded,
# loop through it and replace all occurrences of the letter “a” with the letter “e”,
# for instance:
# Vector original char: “Hello girl how are you”.
# Modified char vector: "Hole muchechede how are you"
# Finally, display the result on the screen.
# Note: we'll need a char vector of 50, but we won't load it with a For.
vector5 =[]
cVector5 = input('Ingrese el caracter:')
pV = '.'

while cVector5 != pV and len(vector5) < 50:
    vector5.append(cVector5)
    cVector5 = input('Ingrese el caracter:')

letV5A = 'a'
contIndiV5 = 0

for v5 in vector5:
    if v5 == letV5A:
        vector5[contIndiV5] = 'e'
    contIndiV5 += 1
print(vector5)

# Given a list of 10 numbers, load them into a vector. Then detect if in the
# vector there is some repeated element. If there is, indicate it with a sign
# explanatory "There are duplicates", otherwise indicate "There are no duplicates".
vector6 = []

for cd in range(10):
    numVector6  =  int ( input ( 'Enter the number: ' ))
    vector6.append(numVector6)

banderaV6  =  0

for v6 in vector6:
    repeV6  =  v6
    contRepeV6 = 0
    for repeV6 in vector6:
        if  repeV6  ==  v6 :
            contRepeV6 += 1
    if contRepeV6 >= 2:
        banderaV6  =  1

if  banderaV6  ==  0 :
    print ( 'There are no duplicates' )
else:
    print ( 'There are repeated numbers' )

# A company sells 15 types of items and for each sale made
# generates a record with the following data:
# • Item number (1 to 15).
# • Quantity sold.
# There can be several records for the same item and the last one is indicated
# item number equal to zero.
# If you need to determine and inform:
# a. The item number that sold the most in total.
# b. The item numbers that did not record sales.
# c. The number of units sold for item number 10.
# Note: take into account the concept of "registry" and the structure proposal
# Main separate from slogans (see videos of combined cycles and exercises
# solved of combined cycles).
vector7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

itemNumber  =  int ( input ( 'Enter the item number (from 1 to 15): ' ))
qtySold_  =  int ( input ( 'Enter the quantity sold: ' ))

while numArticulo != 0:
    vector7[numArticulo-1] = vector7[numArticulo-1] + cantVendida_
    ItemNumber  =  int ( input ( 'Enter the item number: ' ))
    qtySold_  =  int ( input ( 'Enter the quantity sold: ' ))

maxVector7 = vector7[0]
artVector7 = 1

for  fg  in  range ( 15 ):
    if vector7[fg] >= maxVector7:
        maxVector7 = vector7[fg]
        artVector7 = fg + 1

unsoldIndex  = []

for  hi  in  range ( 15 ):
    if vector7[hi] == 0:
        indexNoSold _ append ( hi + 1 )

print ( f'The articles that did not register sales were: { indexNoSold } ' )
print ( f'The item that sold the most was { artVector7 } with { vector7 [ artVector7 - 1 ] } units sold' )
print ( f'Number of products sold for item 10 = { vector7 [ 9 ] } products' )

# A list of 20 numbers is entered into a vector. It is requested to order these
# numbers in decreasing form (highest to lowest). Show the list
# tidy.
vector8 = []

for  jk  in  range ( 20 ):
    numVector8  =  int ( input ( 'Enter the number: ' ))
    vector8.append(numVector8)

vector8.sort()
print(vector8)
