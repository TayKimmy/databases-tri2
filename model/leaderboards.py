## Dillon's API for the custom car Builder (BAcKEND)
import json

leaderboard_data = []
leaderboard_list = [
    {"user": "Dillon", "Score": "400"},
    {"user": "Rohan", "Score": "300"},
    {"user": "Tay", "Score":  "200"},
    {"user": "Adi", "Score": "100"},
]

def addScore(user, score):
    leaderboard_data.append({"user": user, "score": score})
    leaderboard_data.sort(key=lambda x: x["score"], reverse=True)

def getLeaderboard():
    return leaderboard_data

if __name__ == "__main__":
    for item in leaderboard_list:
        addScore(item["user"], item["Score"])
    print(json.dumps(getLeaderboard(), indent=4))
