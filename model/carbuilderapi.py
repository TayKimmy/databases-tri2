## Rohan's API for the Custom Car Builder (BACKEND)
import json

carbuilder_data = []
carbuilder_list = [
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1T", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$73,000"},
    {"Car": "Tesla Model S", "Range": "400 miles", "Seating": "5 people", "0-60": "2 Seconds", "Price": "$95,000"},
    {"Car": "Tesla Model 3", "Range": "300 miles", "Seating": "5 people", "0-60": "3 Seconds", "Price": "$43,000"},
    {"Car": "Tesla Model X", "Range": "350 miles", "Seating": "6 people", "0-60": "4 Seconds", "Price": "$110,000"},
    {"Car": "Tesla Model Y", "Range": "300 miles", "Seating": "5 people", "0-60": "3.5 Seconds", "Price": "$52,000"},
    {"Car": "Tesla Semi", "Range": "500 miles", "Seating": "1 people", "0-60": "20 Seconds", "Price": "$150,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
    {"Car": "Rivian R1S", "Range": "300 miles", "Seating": "7 people", "0-60": "3 Seconds", "Price": "$78,000"},
]

def initfact():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in carbuilder_list:
        carbuilder_dataappend({"id": item_id, "results": item})
        item_id += 1

def getfact():
    return (carbuilder_data)

def getfact_c():
    return (carbuilder_data[id])

def printfact(car):
    print(car['id'], car['question'], "\n")


def countcarbuilder():
    return len(carbuilder_data)


if __name__ == "__main__": 
    initfact()  # initialize jokes

    # Random joke
    print("Random fact")
    printfact(getrandom())
    
    # Count of Jokes
    print("Jokes Count: " + str(countcarbuilder()))  