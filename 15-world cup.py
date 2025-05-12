teams = {
    "Iran": {"wins": 0, "loses": 0, "draws": 0, "gf": 0, "ga": 0, "points": 0},
    "Spain": {"wins": 0, "loses": 0, "draws": 0, "gf": 0, "ga": 0, "points": 0},
    "Portugal": {"wins": 0, "loses": 0, "draws": 0, "gf": 0, "ga": 0, "points": 0},
    "Morocco": {"wins": 0, "loses": 0, "draws": 0, "gf": 0, "ga": 0, "points": 0}
}

matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco"),
]

results = []
for _ in range(6):
    results.append(input())

for i in range(6):
    score = results[i]
    team1, team2 = matches[i]
    g1, g2 = map(int, score.split("-"))

    teams[team1]["gf"] += g1
    teams[team1]["ga"] += g2
    teams[team2]["gf"] += g2
    teams[team2]["ga"] += g1

    if g1 > g2:
        teams[team1]["wins"] += 1
        teams[team2]["loses"] += 1
        teams[team1]["points"] += 3
    elif g1 < g2:
        teams[team2]["wins"] += 1
        teams[team1]["loses"] += 1
        teams[team2]["points"] += 3
    else:
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

team_list = []
for name, data in teams.items():
    goal_diff = data["gf"] - data["ga"]
    team_list.append((data["points"], data["wins"], name, data["loses"], data["draws"], goal_diff))

team_list.sort(key=lambda x: (-x[0], -x[1], x[2]))

for item in team_list:
    name = item[2]
    data = teams[name]
    gd = data["gf"] - data["ga"]
    print("{}  wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(
        name, data["wins"], data["loses"], data["draws"], gd, data["points"]
    ))
