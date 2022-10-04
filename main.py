from pick import pick
import click
import json

objList = []

# ------------------------=[CAR CLASS]=------------------------

class Car:
    def __init__(self, brand, fabrication, color, price):
        self.brand = brand
        self.fabrication = fabrication
        self.color = color
        self.price = price
        self.available = "Disponible"

    def dict(self):
        return self.__dict__

# ------------------------=[JSON: LOAD DATA]=------------------------

with open('data.json') as file:
    objList = json.load(file)

# ------------------------=[JSON: WRITE TO FILE]=------------------------

def writeToFile(car):
    with open("data.json", 'w') as json_file:
        objList.append(car.dict())
        
        json.dump(objList, json_file, indent=4)
        json_file.close()

# ------------------------=[SEND MAIN MENU]=------------------------

def sendMainMenu():
    title = '       VENTA AUTOS'
    options = ['Registro de Automóvil',
               'Ver Automóviles Disponibles', 'Comprar Automóvil']
    selected, index = pick(options, title, indicator='=>')

    return index

# ------------------------=[SEND CAR REGISTRY]=------------------------

def sendCarRegistry():
    click.clear()
    print('       REGISTRAR AUTO')
    brand = input("Marca: ")
    fabrication = input("Fecha de Fabricación: ")
    color = input("Color: ")
    price = input("Precio (S/.): ")

    car = Car(brand, fabrication, color, price)
    writeToFile(car)

# ------------------------=[SEND CAR LIST]=------------------------

def sendCarList():
    click.clear()
    print(objList[0])
    pass

# ------------------------=[SEND BUY CAR]=------------------------

def sendBuyCar():
    click.clear()
    pass

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
