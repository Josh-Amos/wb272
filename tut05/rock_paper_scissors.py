import sys

def winner(p1, p2):
    if ((p1 == "R") or (p1 == "P") or (p1 == "S")) and ((p2 == "R") or (p2 == "P") or (p2 == "S")):
        if p1 == "R":
            if p2 == "S":
                return "Player 1 wins"
            elif p2 == "P":
                return "Player 2 wins"
            else:
                return "It's a Draw"

        elif p1 == "P":
            if p2 == "R":
                return "Player 1 wins"
            elif p2 == "S":
                return "Player 2 wins"
            else:
                return "It's a Draw"

        elif p1 == "S":
            if p2 == "P":
                return "Player 1 wins"
            elif p2 == "R":
                return "Player 2 wins"
            else:
                return "It's a Draw"
    else:
        return "Incorrect Inputs"

if __name__ == "__main__":
    winner(sys.argv[1], sys.argv[2])
