from tabulate import tabulate
import json

objList = []

# ------------------------=[CAR DEFINITION]=------------------------

def car(brand, year: int, color, price: int):
        return {'brand': brand, 'year': year, 'color': color, 'price': price, 'available': "Disponible"}

# ------------------------=[JSON: LOAD DATA]=------------------------

with open('data/data.json') as file:
    objList = json.load(file)

# ------------------------=[JSON: WRITE TO FILE]=------------------------

def saveToFile():
    with open("data/data.json", 'w') as file:        
        json.dump(objList, file, indent=4)

# ------------------------=[FIND CAR]=------------------------

def findCar(brand, year: int, color, price: int):
    for i in objList:       
        if i['brand'] == brand and i['year'] == year and i['color'] == color and i['price'] == price:
            return i
        else:
            continue
    return False

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
            newCar = car(brand, year, color, price)
            objList.append(newCar)
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
