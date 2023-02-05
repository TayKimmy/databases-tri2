import random

cars_data = []
car_list = [
    "Tesla Model S",
    "Tesla Model Y",
    "Tesla Model X",
    "Tesla Model 3",
    "Tesla Semi",
    "Tesla Roadster",
    "Rivian R1S",
    "Rivian R1T",
    "Lucid Air Grand Touring",
    "Lucid Air Grand Touring Performance",
    "NIO ET7",
    "NIO ET5",
    "NIO ES8",
    "NIO ES7",
    "NIO ES6",
    "NIO EC7",
    "NIO EC6"
]

def initRankings():
    item_id = 0
    for item in car_list:
        cars_data.append({"id": item_id, "car": item, "like": 0, "dislike": 0})
        item_id += 1
    for i in range(10):
        id = getRandomCar()['id']
        addCarLike(id)
    for i in range(5):
        id = getRandomCar()['id']
        addCarDislike(id)
        
def getCars():
    return(cars_data)

def getCar(id):
    return(cars_data[id])

def getRandomCar():
    return(random.choice(cars_data))

def favoriteCar():
    best = 0
    bestID = -1
    for car in getCars():
        if car['like'] > best:
            best = car['like']
            bestID = car['id']
    return cars_data[bestID]
    
def leastfavoriteCar():
    worst = 0
    worstID = -1
    for car in getCars():
        if car['dislike'] > worst:
            worst = car['dislike']
            worstID = car['id']
    return cars_data[worstID]

def addCarLike(id):
    cars_data[id]['like'] = cars_data[id]['like'] + 1
    return cars_data[id]['like']

def addCarDislike(id):
    cars_data[id]['dislike'] = cars_data[id]['dislike'] + 1
    return cars_data[id]['dislike']

def printCar(car):
    print(car['id'], car['car'], "\n", "like:", car['like'], "\n", "dislike:", car['dislike'], "\n")

def countCars():
    return len(cars_data)

if __name__ == "__main__": 
    initRankings() 
    
    best = favoriteCar()
    print("Most liked", best['like'])
    printCar(best)
    worst = leastfavoriteCar()
    print("Most disliked", worst['dislike'])
    printCar(worst)
    
    print("Random car")
    printCar(getRandomCar())
    
    print("Cars Count: " + str(countCars()))