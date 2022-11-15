import json
import os

from pick import pick
from tabulate import tabulate

carList = []
soldList = []

class Car:
    def __init__(self, brand: str, year: int, color: str, price: int):
        self.brand = brand
        self.year = year
        self.color = color
        self.price = price
        self.available = "Disponible"

if os.path.exists('./data/data.json'):
    with open('data/data.json') as file:
        carList = json.load(file)
else:
    with open("data/data.json", 'w') as file:
        json.dump(carList, file, indent=4)


if os.path.exists('./data/sold.json'):
    with open('data/sold.json') as file:
        soldList = json.load(file)
else:
    with open("data/sold.json", 'w') as file:
        json.dump(soldList, file, indent=4)

# ------------------------=[UTILS]=------------------------

def saveToFile(name: str):
    if name == 'data':
        with open("data/data.json", 'w') as file:
            json.dump(carList, file, indent=4)
    elif name == 'sold':
        with open("data/sold.json", 'w') as file:
            json.dump(soldList, file, indent=4)
    

def findCar(brand: str, year: int, color: str, price: int):
    for i in carList:       
        if i['brand'] == brand and i['year'] == year and i['color'] == color and i['price'] == price:
            return i
        else:
            continue
    return False

def buyCar(car):  
    car['available'] = "Vendido"
    
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(carList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(carList)+1)))
    
    soldList.append(car)
    saveToFile('sold')

    for i in carList:
        if i['available'] == "Vendido":
            carList.pop(carList.index(i))
    saveToFile('data')
    addReturn()
       
def addReturn():
    button = input("Presiona ENTER para volver.")
    if button == '':
        os.system('cls')
        init()

# ------------------------=[MAIN FUNCTIONS]=------------------------

def sendCarRegistry():
    os.system('cls')
    print('\n                 ▄▀▄▀▄▀ REGISTRAR AUTO ▀▄▀▄▀▄')
    brand = str(input("Marca: "))
    year = int(input("Fecha de Fabricación: "))
    color = str(input("Color: "))
    price = int(input("Precio (s/.): "))

    while True:
        if price >= 0:
            newCar = Car(brand, year, color, price)
            carList.append(newCar.__dict__)
            saveToFile('data')
            sendCarList()
            break
        else:
            price = int(input("Precio (s/.): "))

def sendCarList():
    os.system('cls')
    orderList = sorted(carList, key=lambda dictionary: dictionary['brand'])

    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(orderList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(carList)+1)))
    addReturn()

def sendBuyCar():
    os.system('cls')
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(sorted(carList, key=lambda dictionary: dictionary['brand']), headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(carList)+1)))
    
    print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
    brand = str(input("Marca: "))
    year = int(input("Fecha de Fabricación: "))
    color = str(input("Color: "))
    price = int(input("Precio (s/.): "))
    
    car = findCar(brand, year, color, price)
    while True:
        if(car):
            buyCar(car)
            break
        else:
            print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
            brand = str(input("Marca: "))
            year = int(input("Fecha de Fabricación: "))
            color = str(input("Color: "))
            price = int(input("Precio (s/.): "))
            
            car = findCar(brand, year, color, price)

def sendSoldList():
    os.system('cls')
    orderList = sorted(soldList, key=lambda dictionary: dictionary['brand'])

    print('\n                 ▄▀▄▀▄▀ AUTOS VENDIDOS ▀▄▀▄▀▄')
    print(tabulate(orderList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(soldList)+1)))
    addReturn()

def sendMoneyTotal():
    os.system('cls')
    moneyTotal = 0

    for i in soldList:
        moneyTotal += i['price']
    
    print('\n                 ▄▀▄▀▄▀ GANANCIAS POR VENTAS ▀▄▀▄▀▄', end="")
    print('\n                            S/. ' + str(moneyTotal))
    addReturn()

def sendMainMenu():
    title = '                 ▄▀▄▀▄▀ VENTA AUTOS ▀▄▀▄▀▄'
    options = ['Registro de Automóvil', 'Ver Automóviles Disponibles', 'Comprar Automóvil', 'Ver Automóviles Vendidos', 'Cantidad de S/.']
    selected, index = pick(options=options, title=title, indicator='=>')

    return index

# ------------------------=[INIT]=------------------------

def init():
    menuSelection = sendMainMenu()

    match menuSelection:
        case 0:
            sendCarRegistry()
        case 1:
            sendCarList()
        case 2:
            sendBuyCar()
        case 3:
            sendSoldList()
        case 4:
            sendMoneyTotal()
init()