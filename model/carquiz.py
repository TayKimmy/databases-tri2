## API for Quiz
import json

quiz_data = []
quiz_list = [
    {"Question": "What is the price of a Tesla Model 3?", "Answer": "40000" },
    {"Question": "What is the range of a Tesla Model X?", "Answer": "330"},
    {"Question": "How many cars are in the Tesla lineup? ", "Answer": "4" },
    {"Question": "What is the range of the Rivian R1S?", "Answer": "350"},
    {"Question": "What is the towing capacity of a Rivian R1T?", "Answer": "11000"},
    {"Question": "What is the starting price of a Rivian R1S?", "Answer": "78,000"},
    {"Question": "What is the starting price of a Lucid Air?", "Answer": "87000"},
    {"Question": "What is the range of the NIO EC7?", "Answer": "300"},
    {"Question": "True or False: The Tesla Model S is completely electric.", "Answer": "True"},
    {"Question": "True or False: The Tesla Model 3 is more expensive than the Model X.", "Answer": "False"},
    {"Question": "True or False: The Tesla Model X is the most expensive Tesla.", "Answer": "True"},
    {"Question": "True or False: The NIO EC5 is a sedan.", "Answer": "True"},
    {"Question": "What is the range of the NIO EC5?", "Answer": "600"},
    {"Question": "How many seats does the Tesla Model X have?", "Answer": "7"},
    {"Question": "True or False: the Lucid Air is an SUV.", "Answer": "False"},
    {"Question": "When was the Tesla Model Y released?", "Answer": "2020"},
    {"Question": "When was the Lucid Air released?", "Answer": "2021"},
    {"Question": "What is the range of a Tesla Model X?", "Answer": "330"},
    {"Question": "What is the range of a Tesla Model X?", "Answer": "330"},
    {"Question": "What is the range of a Tesla Model X?", "Answer": "330"},
]

def initquiz():

    item_id = 0
    for item in quiz_list:
        quiz_data.append({"id": item_id, "results": item})
        item_id += 1

def getquiz():
    return (quiz_data)

def getfact_c():
    return (quiz_data[id])

def printfact(Question):
    print(Question['id'], Question['question'], "\n")


def countquiz():
    return len(quiz_data)


if __name__ == "__main__": 
    initfact() 

    
    
    # count of 
    print("count: " + str(countquiz()))  