from tabulate import tabulate
import json

objList = []

# ------------------------=[CAR CLASS]=------------------------

class Car:
    def __init__(self, brand, year: int, color, price: int):
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

def saveToFile():
    with open("data/data.json", 'w') as file:        
        json.dump(objList, file, indent=4)

# ------------------------=[FIND CAR]=------------------------

def findCar(brand, year: int, color, price: int):
    i = 0
    while i < len(objList):
        if objList[i]['brand'] != brand or objList[i]['year'] != year or objList[i]['color'] != color or objList[i]['price'] != price:
            return False
        
        if objList[i]['brand'] == brand and objList[i]['year'] == year and objList[i]['color'] == color and objList[i]['price'] == price:
            return objList[i]
        i += 1

# ------------------------=[ADD RETURN BUTTON]=------------------------
       
def addReturn():
    button = input("Presiona ENTER para volver.")
    if button == '':
        init()

# ------------------------=[SEND CAR REGISTRY]=------------------------

def sendCarRegistry():
    print('\n                 ▄▀▄▀▄▀ REGISTRAR AUTO ▀▄▀▄▀▄')
    brand = input("Marca: ")
    year = int(input("Fecha de Fabricación: "))
    color = input("Color: ")
    price = int(input("Precio (s/.): "))

    while True:
        if price >= 0:
            car = Car(brand, year, color, price)
            objList.append(car.dict())
            saveToFile()
            sendCarList(False)
            break
        else:
            price = int(input("Precio (s/.): "))


# ------------------------=[SEND CAR LIST]=------------------------

def sendCarList(delete: bool):
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(objList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(objList)+1)))
    
    if delete:   
        for i in objList:
            if i['available'] == "Vendido":
                objList.pop(objList.index(i))
        saveToFile()
    addReturn()
    
# ------------------------=[SEND BUY CAR]=------------------------

def sendBuyCar():
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(objList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(objList)+1)))
    
    print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
    brand = input("Marca: ")
    year = int(input("Fecha de Fabricación: "))
    color = input("Color: ")
    price = int(input("Precio (s/.): "))
    
    car = findCar(brand, year, color, price)
    while True:
        if(car):
            car['available'] = "Vendido"
            sendCarList(True)
            break
        else:
            print('\n                 ▄▀▄▀▄▀ COMPRAR AUTO ▀▄▀▄▀▄')
            brand = input("Marca: ")
            year = int(input("Fecha de Fabricación: "))
            color = input("Color: ")
            price = int(input("Precio (s/.): "))
            
            car = findCar(brand, year, color, price)

# ------------------------=[INIT]=------------------------

def init():
    print('\n                 ▄▀▄▀▄▀ VENTA AUTOS ▀▄▀▄▀▄')
    print('\n1. Registro de Automóvil\n2. Ver Automóviles Disponibles\n3. Comprar Automóvil')
    
    index = int(input("\nSelecciona [1, 2, 3]: "))
    while True:
        if index not in [1, 2, 3]:
            index = int(input("\nSelecciona [1, 2, 3]: "))
        else:
            break

    match index:
        case 1:
            sendCarRegistry()
        case 2:
            sendCarList(False)
        case 3:
            sendBuyCar()

init()
