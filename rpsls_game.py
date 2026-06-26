import random

s = input("enter your move in lowercase : ")

p = random.choice(("rock", "paper", "scissors", "lizard", "spock"))

valid_moves = {"rock", "paper", "scissors", "lizard", "spock"}

wins = {
    "rock": {"scissors", "lizard"},
    "paper": {"rock", "spock"},
    "scissors": {"paper", "lizard"},
    "lizard": {"spock", "paper"},
    "spock": {"scissors", "rock"}
}

winner = "NOT DECIDED"
round_type = "No Round"

print("your move :", s)
print("pc move :", p)



if type(s) != str:
    winner = "INVALID MOVE"
elif s.islower() == False:
    winner = "INVALID MOVE"
elif s not in valid_moves:
    winner = "INVALID MOVE"
elif type(p) != str:
    winner = "INVALID MOVE"
elif p.islower() == False:
    winner = "INVALID MOVE"
elif p not in valid_moves:
    winner = "INVALID MOVE"
else:

    if s == p:
        winner = "Draw"

    elif p in wins[s]:
        winner = "Player 1 Wins"

    elif s in wins[p]:
        winner = "Player 2 Wins"

    else:
        winner = "GAME STATE CORRUPTED"

A = "rock"
B = "scissors"
C = "paper"

transitive = True

if B in wins[A]:
    if C in wins[B]:
        if C not in wins[A]:
            transitive = False
        else:
            transitive = True
    else:
        transitive = True
else:
    transitive = True


player1_wins = False
player2_wins = False
draw = False

if winner != "INVALID MOVE":
    if s == p:
        draw = True
    elif p in wins[s]:
        player1_wins = True
    elif s in wins[p]:
        player2_wins = True
    else:
        winner = "GAME STATE CORRUPTED"

    if player1_wins == True:
        if player2_wins == True:
            winner = "GAME STATE CORRUPTED"

    if draw == True:
        if s != p:
            winner = "GAME STATE CORRUPTED"


if winner == "Player 1 Wins":
    if s == "rock":
        round_type = "Power Win"
    elif s == "spock":
        round_type = "Power Win"
    elif s == "scissors":
        round_type = "Sharp Win"
    elif s == "paper":
        round_type = "Logic Win"
    elif s == "lizard":
        round_type = "Poison Win"

elif winner == "Player 2 Wins":
    if p == "rock":
        round_type = "Power Win"
    elif p == "spock":
        round_type = "Power Win"
    elif p == "scissors":
        round_type = "Sharp Win"
    elif p == "paper":
        round_type = "Logic Win"
    elif p == "lizard":
        round_type = "Poison Win"

elif winner == "Draw":
    round_type = "Draw Round"




print("Winner:", winner)

if winner != "INVALID MOVE":
    if winner != "GAME STATE CORRUPTED":
        print("Round Type:", round_type)
        print("Transitive system:", transitive)