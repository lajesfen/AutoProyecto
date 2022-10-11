from pick import pick
from tabulate import tabulate
import click
import json

objList = []

# ------------------------=[CAR CLASS]=------------------------

class Car:
    def __init__(self, brand, year, color, price):
        self.brand = brand
        self.year = year
        self.color = color
        self.price = price
        self.available = "Disponible"

    def dict(self):
        return self.__dict__

# ------------------------=[JSON: LOAD DATA]=------------------------

with open('data/data.json') as file:
    objList = json.load(file)

# ------------------------=[JSON: WRITE TO FILE]=------------------------

def writeToFile():
    with open("data/data.json", 'w') as file:        
        json.dump(objList, file, indent=4)

# ------------------------=[FIND CAR]=------------------------

def findCar(brand, year, color, price):
    i = 0
    while i < len(objList):  
        if objList[i]['brand'] == brand and objList[i]['year'] == year and objList[i]['color'] == color and objList[i]['price'] == price:
            return objList[i]
        i += 1

# ------------------------=[SEND MAIN MENU]=------------------------

def sendMainMenu():
    title = '       VENTA AUTOS'
    options = ['Registro de Automóvil', 'Ver Automóviles Disponibles', 'Comprar Automóvil']
    selected, index = pick(options, title, indicator='=>')

    return index

# ------------------------=[SEND CAR REGISTRY]=------------------------

def sendCarRegistry():
    click.clear()
    print('       REGISTRAR AUTO')
    brand = input("Marca: ")
    year = input("Fecha de Fabricación: ")
    color = input("Color: ")
    price = input("Precio (s/.): ")

    car = Car(brand, year, color, price)
    objList.append(car.dict())
    writeToFile()
    sendCarList()

# ------------------------=[SEND CAR LIST]=------------------------

def sendCarList():
    click.clear()
    table = tabulate(objList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(objList)+1))
    print(table)

# ------------------------=[SEND BUY CAR]=------------------------

def sendBuyCar():
    click.clear()
    print('       COMPRAR AUTO')
    brand = input("Marca: ")
    year = input("Fecha de Fabricación: ")
    color = input("Color: ")
    price = input("Precio (s/.): ")
    
    car = findCar(brand, year, color, price)
    if(car):
        car['available'] = "Vendido"
    writeToFile()

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

init()
