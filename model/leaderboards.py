## Dillon's API for the custom car Builder (BAcKEND)
import json

leaderboard_data = []
leaderboard_list = [
    {"user": "Dillon", "Score": "400"},
    {"user": "Rohan", "Score": "300"},
    {"user": "Tay", "Score":  "200"},
    {"user": "Adi", "Score": "100"},
]

def initleaderboard():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in leaderboard_list:
        leaderboard_data.append({"id": item_id, "results": item})
        item_id += 1

def addScore(user, score):
    leaderboard_data.append({"user": user, "score": score})
    leaderboard_data.sort(key=lambda x: x["score"], reverse=True)

def getLeaderboard():
    return leaderboard_data

if __name__ == "__main__":
    for item in leaderboard_list:
        addScore(item["user"], item["Score"])
    print(json.dumps(getLeaderboard(), indent=4))
