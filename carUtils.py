import json

from tabulate import tabulate

def saveToFile(carList:list, soldList:list, name: str):
    if name == 'data':
        with open("data/data.json", 'w') as file:
            json.dump(carList, file, indent=4)
    elif name == 'sold':
        with open("data/sold.json", 'w') as file:
            json.dump(soldList, file, indent=4)
    
def findCar(carList:list, brand: str, year: int, color: str, price: int):
    for i in carList:       
        if i['brand'] == brand and i['year'] == year and i['color'] == color and i['price'] == price:
            return i
        else:
            continue
    return False

def buyCar(carList:list, soldList:list, car):  
    car['available'] = "Vendido"
    
    print('\n                 ▄▀▄▀▄▀ AUTOS DISPONIBLES ▀▄▀▄▀▄')
    print(tabulate(carList, headers={"brand": "Marca", "year": "Año de Fabric.", "color": "Color", "price": "Precio", "available": "Disponible"}, tablefmt='fancy_grid', showindex=range(1, len(carList)+1)))
    
    soldList.append(car)
    saveToFile(carList, soldList, 'sold')

    for i in carList:
        if i['available'] == "Vendido":
            carList.pop(carList.index(i))
    saveToFile(carList, soldList, 'data')