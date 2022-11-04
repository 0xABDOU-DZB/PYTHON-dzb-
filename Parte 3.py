# LOAD BATCHES AND PROCESSES -------------------------------------------- ------------------
# 1. A company that manufactures 20 items has the following information for each item:
# - Item Code (4 digits, non-correlative).
# - Unit price.
# This first batch is not ordered.
# On the other hand, it has a batch of records with the sales of the previous year. Each record contains
# the next information:
# - Customer Number (1 to 300).
# - Item Code (4 non-correlative digits).
#       - Mes (1 a 12).
# - Day (1 to 31).
# - Quantity sold.
# There can be more than one record for the same item. The batch ends with a record with number
Customer # equal to zero.
# Request:
# a) A list with the following format:
# Article Code 999
# Total Quantity Sold 999
# This list must be ordered from highest to lowest by total quantity sold.
# b) Inform, if any, the names of the months in which there were no sales.
# c) Inform the codes of the articles whose sales in quantity are greater than the average.
codigo1 = []
price1  = []

for x in range(20):
    codenum1  =  int ( input ( 'Enter the code number (4 digits): ' ))
    numPrice1  =  float ( input ( 'Enter the price of the product: $ ' ))
    codigo1.append(numcodigo1)
    precio1.append(numPrice1)

accCantTotalVend = []

for d in range(20):
    accCantTotalVend.append(0)

mes = []

abc = 0
for  a  in  range ( 12 ):
    m_ = abc + 1
    mes.append(m_)
    abc += 1

accVentMes = []

for  r  in  range ( 12 ):
    accVentMes.append(0)

soliClientNumber  =  int ( input ( 'Enter the client number: ' ))
requestItemCode  =  int ( input ( 'Enter the item code (4 digits): ' ))
solMonth  =  int ( input ( 'Enter the month (from 1 to 12): ' ))
solDay  =  int ( input ( 'Enter the day (from 1 to 31): ' ))
solCantVend  =  int ( input ( 'Enter the amount: ' ))

while soliNumCliente != 0:
   for k in range(20):
        if  soliCodArticulo  ==  codigo1 [ k ]:
            accCantTotalVend[k] += solCantVend
        if solMes == mes[k]:
            accVentMes[k] += solCantVend

   soliClientNumber  =  int ( input ( 'Enter the client number: ' ))
   requestItemCode  =  int ( input ( 'Enter the item code (4 digits): ' ))
   solMonth  =  int ( input ( 'Enter the month (from 1 to 12): ' ))
   solDay  =  int ( input ( 'Enter the day (from 1 to 31): ' ))
   solCantVend  =  int ( input ( 'Enter the amount: ' ))

# Bubble method:
i = 0
while i < len(accCantTotalVend):
    j = i + 1
    while j < len(accCantTotalVend):
        if accCantTotalVend[i] < accCantTotalVend[j]:
            aux  =  accCantTotalVend [ i ]
            accCantTotalVend[i] = accCantTotalVend[j]
            accCantTotalVend [ j ] =  aux
            aux  =  codigo1 [ i ]
            code1 [ i ] =  code1 [ j ]
            codigo1 [ j ] =  aux
        j += 1
    i += 1

z = 0
for g in range(5):
    print(f'''
Item Code: { code1 [ z ] }
Total Quantity Sold: { accCantTotalVend [ z ] } ''' )
    z += 1

mesSinVentas = []
monthName  = [ 'January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' ,
             'September' , 'October' , 'November' , 'December' ]

auxMes  =  0

for  v  in  range ( 12 ):
    if accVentMes[v] == 0:
        mSinVent  =  mesNombre [ v ]
        mesSinVentas.append(mSinVent)
        auxMes  =  1

if auxMes == 1:
    print ( f'The months without sales were: { monthWithoutSales } ' )
else:
    print ( f'There were sales every month' )

sumValoresArticulo  =  0
for  j  in  accCantTotalVend :
    sumValoresArticulo += j

promVenArticulos = sumValoresArticulo / len(accCantTotalVend)
print(promVenArticulos)

ind_ = 0
for art in accCantTotalVend:
    if art > promVenArticulos:
        print ( f'The article { codigo1 [ ind_ ] } , exceeds the average sales ( { promVenArticulos } ), with { art } sales.' )
    ind_ += 1

# 2. You have a batch of 300 records (one per item), each of which has the
# Next information:
# - Item number (4 non-correlative digits).
# - Number of units in stock.
# - Unit price.
# The batch is out of order.
# Another batch of records is available, each of which corresponds to a sale with the following
# information:
# - Customer number (1 to 300).
# - Article number (4 digits, not consecutive).
# - Number of units sold.
# The last record in this batch has customer number zero and should not be processed. develop the
# program that determines and prints:
# a) A list of the sales made, in the following format:
# Sales list
# Customer No. 99
# Item No. 99
# Quantity Sold 999
# Import Total 999.99
# b) Inform which is the customer number that bought the most in total (in pesos).
# c) Inform each one of the numbers of the articles that have not registered sales.
numArt2  = []
cantUnidStock = []
precioUnit = []

for  q  in  range ( 300 ):
    nA2  =  int ( input ( 'Enter the article number (4 digits): ' ))
    cUS2  =  int ( input ( 'Enter the number of units in stock for the item: ' ))
    pU2  =  float ( input ( 'Enter the price of the item: $ ' ))
    numArt2.append(nA2)
    cantUnidStock . append ( cUS2 )
    precioUnit.append(pU2)

CustomerNumber2  =  int ( input ( 'Enter the customer number: ' ))
Article number  =  int ( input ( 'Enter the article number (4 digits): ' ))
qtyUnidSold2  =  int ( input ( 'Enter the number of units sold: ' ))

nCli2 = []
accCantVen2 = []
impClien2 = []

for  read  in  range ( 300 ):
    accCantVen2.append(0)

indi_2 = 0
while numCliente2 != 0:
    indi_2 = 0
    for  nr  in  numArt2 :
        if  numberItem  ==  nr :
            importeAAbonar2  =  precioUnit [ indi_2 ] *  cantUnidVendidas2
            print ( f''''Sales list:
            Client No.:        { numCliente2 }
            No.Item:        { numberItem }
            Quantity Sold:    { unitQuantitySold2 }
            Importe Total:      ${importeAAbonar2}
            ''')
            nCli2.append(numCliente2)
            accCantVend2 [ indi_2 ] +=  cantUnidVendidas2
            impClien2.append(importeAAbonar2)
        indi_2 += 1
    CustomerNumber2  =  int ( input ( 'Enter the customer number: ' ))
    Article number  =  int ( input ( 'Enter the article number (4 digits): ' ))
    qtyUnidSold2  =  int ( input ( 'Enter the number of units sold: ' ))

maxPago = impClien2[0]
clienteMasPago = nCli2[0]

for d in range(len(impClien2)):
    if maxPago < impClien2[d]:
        maxPago = impClien2[d]
        clienteMasPago = nCli2[d]

print ( f'The customer who paid the most is the number: { clientMasPago } , with an amount of $ { maxPago } ' )

for w in range(len(accCantVen2)):
    if accCantVen2[w] == 0:
        print ( f' The article number { numArt2 [ w ] } , I do not register sales' )

# 3. A trucking freight company has 20 different rates depending on the destination
# of shipments to be made. You have a batch of logs with the following information:
# - Rate Number (Number of 4 figures, not correlative).
# - Amount per KM.
# This lot does not come ordered. You then have a second batch of records with the
# information of the shipments that were made during the past week, containing each one of
# them the following fields:
# - Truck Number (1 to 100).
# - Rate Number.
# - Kilometers traveled.
# This batch ends with a record with a negative truck number. We are asked to make a program
# that determine and report:
# a) The total collected for each rate.
# b) A list like the following:
# Truck number xxx
# Total raised xxx
vecNumTarifa3  = []
vecImpXKm  = []

def  cargarLote1 ( v1 , v2 , tam ):
    for  h  in  range ( tam ):
        a_  =  int ( input ( 'Enter the rate number: ' ))
        b_  =  float ( input ( 'Enter the amount per KM: $ ' ))
        v1.append(a_)
        v2.append(b_)

loadLote1 ( vecNumTarifa3 , vecImpXKm , 20 )

def  initializeEn0 ( vector , tam ):
    for  b  in  range ( tam ):
        vector.append(0)

vectorNumCamion = []
vectorKilometrosRecorridosSegunTarifa =[]
vectorKmPorCamion = []
vectorTarifaCamion =[]

initializeIn0 ( vectorKilometersTravelsAccording to Fare , 20 )

numTruck  =  int ( input ( 'Enter the truck number (from 1 to 100): ' ))
numTarifaIngresado  =  int ( input ( 'Enter the rate number: ' ))
KilometersTraveled  =  float ( input ( 'Enter the kilometers traveled: ' ))

while numCamion > 0:
    vectorNumCamion.append(numCamion)
    vectorKmPorCamion.append(kilometrosRecorridos)
    vectorTarifaCamion.append((numTarifaIngresado))
    for  e  in  range ( len ( vecNumTarifa3 )):
        if numTarifaIngresado == vecNumTarifa3[e]:
            vectorKilometersTravelsAccording to Tariff [ e ] =  kilometersTravels
    numTruck  =  int ( input ( 'Enter the truck number (from 1 to 100): ' ))
    numTarifaIngresado  =  int ( input ( 'Enter the rate number: ' ))
    KilometersTraveled  =  float ( input ( 'Enter the kilometers traveled: ' ))

def  totalcollected ():
    for  t  in  range ( len ( vecNumTarifa3 )):
        totalRecaud = vecImpXKm[t] * vectorKilometrosRecorridosSegunTarifa[t]
        print ( f'For the rate { vecNumTarifa3 [ t ] } a total of $ { totalRecaud } ' was collected )

totalrecaudado()

def  list ( v9 , v8 ):
    c = 0
    while c < len(vectorTarifaCamion):
        d = c
        while d < len(vecNumTarifa3):
            if  vectorTarifaTruck [ c ] ==  vecNumTarifa3 [ d ]:
                auxPrice  =  vecImpXKm [ d ]
                e = 0
                while e < len(v9):
                    totalRecaudadoCamion  =  v8 [ e ] *  auxPrecio
                    print(f'''
                    Truck number:    { v9 [ e ] }
                    Total collected: $ { totalCollectedTruck }
                    ''')
                    e += 1
            d += 1
        c += 1

list ( vectorNumTruck , vectorKmPerTruck )

#4. A company that transports fragile products has a fleet of 30 trucks.
# A batch of records was generated with the following data for each truck:
# - Truck number (1 to 30).
# - Driver code (3 digits, not consecutive).
# This lot is ordered by truck number in ascending order (from smallest to largest).
# Each driver code drives one and only one truck.
# There is a second batch with the information on the trips made by trucks in the month of
# above, each record contains:
# - Day (1 to 31).
# - Driver code (3 digits, not consecutive).
# - Number of kilometers traveled on that trip (integer).
# - Number of broken pieces in that trip (integer).
# This batch ends with a record with day equal to zero. A record was generated for each trip made,
# therefore, there may be more than one record for the same day and for the same driver code.
# If you need to determine and inform:
# a) For each day of the month, inform which was the driver code that totaled the least
# number of pieces broken in a single trip. Bear in mind that drivers who did not perform
# trips that day, should not be considered.
# b) Inform which is the number of the truck with which the greatest total number of
# kilometers in the FULL month and what driver code drives it.
# c) Inform for each driver code the average number of breakages among all the trips made
# in the first fortnight (days 1 to 15) and those carried out in the second fortnight (days 16 to 31). The
# format will be:
# Driver Code 999
# Average Q1 999
# Q2 average 999
vectorNumCamion4 = []
vectorCodigoChofer4 = []

def  cargarLote4 ( v1 , v2 , tam ):
    for  h  in  range ( tam ):
        a_  =  int ( input ( 'Enter the truck number (1 to 30): ' ))
        b_  =  float ( input ( 'Enter the driver code (3 digits): ' ))
        v1.append(a_)
        v2.append(b_)

cargarLote4(vectorNumCamion4, vectorCodigoChofer4, 30)

def  SortAscending ( vecASort ):
    h = 0
    while h in range(len(vecAOrdenar)):
        k = h +1
        while  k  <  len ( vecAOrdenar ):
            if vecAOrdenar[k] < vecAOrdenar[h]:
                aux_numCa  =  vecAOrdenar [ h ]
                vecAOrdenar[h] = vecAOrdenar[k]
                vecAOrdenar [ k ] =  aux_numCa
            k += 1
        h += 1

AscendingOrder ( vectorNumCamion4 )
AscendingOrder ( vectorCodigoChofer4 )

vectorDia = []
vectorKmViaje_ = []
VectorBrokenPieces  = []
vectorCantidadViajes_driver  = []

initializeTo0 ( driver_TripsAmountvector , 30 )

def  loadbatch5 ():
    day_  =  int ( input ( 'Enter the day: ' ))
    cod_driver  =  int ( input ( 'Enter the driver code: ' ))
    cant_kmTraveled  =  float ( input ( 'Enter the number of km traveled: ' ))
    broken_pieces  =  int ( input ( 'Number of broken pieces: ' ))
    while dia_ != 0:
        vectorDia.append(dia_)
        vectorKmViaje_.append(cant_kmRecorridos)
        VectorBrokenPieces . append ( #BrokenPieces )
        cont_er  =  0
        for  efg  in  VectorCantidadViajes_driver :
            if efg == cod_chofer:
                vectorCantidadViajes_driver [ cont_er ] +=  1
                cont_er  +=  1
            cont_er  +=  1
        day_  =  int ( input ( 'Enter the day: ' ))
        cod_driver  =  int ( input ( 'Enter the driver code: ' ))
        cant_kmTraveled  =  float ( input ( 'Enter the number of km traveled: ' ))
        broken_pieces  =  int ( input ( 'Number of broken pieces: ' ))

loadlot5 ()

smaller_cantTravels  =  vectorCantidadTravias_driver [ 0 ]

#for dia in vectorDia:

# 5. A car rental company has different agencies from where it makes its
# operations. For this, it has several batches of records. A first batch contains the data of the
# cars, each record is made up of:
# - Car code (4 non-correlative digits).
# - Category of the car (1 to 10).
# - Rental amount per km.
# - Agency number (1 to 20).
# This batch is ordered by car code and contains 400 records.
# There is a second batch with the information on the rentals that were made during the past month.
# Each record contains:
# - Car code (4 non-correlative digits).
# - Customer number that made the rental (1 to 200).
# - Total rental days.
# - Kms. tours.
# This batch ends with a record with a customer number equal to zero. There may be more than one record
# for the same car and for the same customer.
# Finally, a third batch contains the data of the agencies of this company.
# - Agency number (1 to 20).
# - Location of the agency (1=Ezeiza Airport, 2=Airpark, 3=City Center).
# From these batches it is requested to determine and report:
# a) A list with the following format:
# Customer Number 99
# Total pesos paid for rent 999
# b) The total accumulated collection for each of the three locations.
# c) The total number of cars for each of the twenty agencies.
# d) The car category most times rented by customers.
# e) The numbers of the agencies, if any, that have carried out in the month less than ten
# rentals in total. To calculate the amount of a car rental, you must multiply the
# amount in pesos per kilometer for the number of kilometers traveled.

# xxxxxxxxxxxxxxxxxx ------------------------------------------------ ----------------------------
