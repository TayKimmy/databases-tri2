## Rohan's API for the custom car Builder (BAcKEND)
import json

carbuilder_data = []
carbuilder_list = [
    {"car": "Rivian R1S", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "Rivian R1T", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$73,000"},
    {"car": "Tesla Model S", "range": "400 miles", "seating": "5 people", "zero": "2 Seconds", "price": "$95,000"},
    {"car": "Tesla Model 3", "range": "300 miles", "seating": "5 people", "zero": "3 Seconds", "price": "$43,000"},
    {"car": "Tesla Model X", "range": "350 miles", "seating": "6 people", "zero": "4 Seconds", "price": "$110,000"},
    {"car": "Tesla Model Y", "range": "300 miles", "seating": "5 people", "zero": "3.5 Seconds", "price": "$52,000"},
    {"car": "Tesla Semi", "range": "500 miles", "seating": "1 people", "zero": "20 Seconds", "price": "$150,000"},
    {"car": "Tesla Roadster", "range": "250 miles", "seating": "2 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "Lucid Air Grand Touring", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "Lucid Air Grand Touring Performance", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO ET7", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO ET5", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO ES8", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO ES7", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO ES6", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO EC7", "range": "300 miles", "seating": "7 people", "zero": "3 Seconds", "price": "$78,000"},
    {"car": "NIO EC6", "range": "300 miles", "seating": "7 peole", "zero": "3 Seconds", "price": "$78,000"},
]

def initcarbuilder():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in carbuilder_list:
        carbuilder_data.append({"id": item_id, "results": item})
        item_id += 1

def getcarbuilder():
    return (carbuilder_data)

def getfact_c():
    return (carbuilder_data[id])

def printfact(car):
    print(car['id'], car['question'], "\n")


def countcarbuilder():
    return len(carbuilder_data)


if __name__ == "__main__": 
    initfact()  # initialize jokes

    
    
    # count of Jokes
    print("Jokes count: " + str(countcarbuilder()))  