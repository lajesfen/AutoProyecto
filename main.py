import json
import os

from pick import pick
from tabulate import tabulate

objList = []

class Car:
    def __init__(self, brand: str, year: int, color: str, price: int):
        self.brand = brand
        self.year = year
        self.color = color
        self.price = price
        self.available = "Disponible"

if os.path.exists('./data/data.json'):
    with open('data/data.json') as file:
        objList = json.load(file)
else:
    with open("data/data.json", 'w') as file:
        json.dump(objList, file, indent=4)

# ------------------------=[UTILS]=------------------------

def saveToFile():
    with open("data/data.json", 'w') as file:
        json.dump(objList, file, indent=4)

def findCar(brand: str, year: int, color: str, price: int):
    for i in objList:       
        if i['brand'] == brand and i['year'] == year and i['color'] == color and i['price'] == price:
            return i
        else:
            continue
    return False
       
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
            objList.append(newCar.__dict__)
            saveToFile()
            sendCarList(False)
            break
        else:
            price = int(input("Precio (s/.): "))


def sendCarList(delete: bool):
    os.system('cls')
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(objList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(objList)+1)))
    
    if delete:   
        for i in objList:
            if i['available'] == "Vendido":
                objList.pop(objList.index(i))
        saveToFile()
    addReturn()


def sendBuyCar():
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(objList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(objList)+1)))
    
    print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
    brand = str(input("Marca: "))
    year = int(input("Fecha de Fabricación: "))
    color = str(input("Color: "))
    price = int(input("Precio (s/.): "))
    
    car = findCar(brand, year, color, price)
    while True:
        if(car):
            car['available'] = "Vendido"
            sendCarList(True)
            break
        else:
            print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
            brand = str(input("Marca: "))
            year = int(input("Fecha de Fabricación: "))
            color = str(input("Color: "))
            price = int(input("Precio (s/.): "))
            
            car = findCar(brand, year, color, price)


def sendMainMenu():
    title = '                 ▄▀▄▀▄▀ VENTA AUTOS ▀▄▀▄▀▄'
    options = ['Registro de Automóvil', 'Ver Automóviles Disponibles', 'Comprar Automóvil']
    selected, index = pick(options=options, title=title, indicator='=>')

    return index

# ------------------------=[START]=------------------------

def init():
    menuSelection = sendMainMenu()

    match menuSelection:
        case 0:
            sendCarRegistry()
        case 1:
            sendCarList(False)
        case 2:
            sendBuyCar()
init()
