import random


# create a function for the random value
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

# check user input validity
while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("invalid input")
    
print(players)

# initialize scores
max_score = 50
standing_scores = [0 for i in range(players)]

#play the game
while max(standing_scores) < max_score:
    for player_id in range(players):
        print("\nPlayer ", player_id + 1, " has began play")
        print("current score: ", standing_scores[player_id], "\n")

        current_score = 0
        while True:
            response = input("Do you want to continue play: ")
            if response.lower() != "y":
                break

            value = roll()
            print("score", value)

            if value == 1:
               print("You lost.")
               current_score = 0
               break
            else:
               current_score += value
               print("Player ", player_id +1, " rolled ", current_score)

               standing_scores[player_id] += current_score
               print("Player ", player_id +1, " has score: ", standing_scores[player_id])

               if standing_scores[player_id] >= max_score:
                break

    max_score = max(standing_scores)
    winning_id = standing_scores.index(max_score)
    print("Player number", winning_id + 1,
          " is the winner with a score of: ", max_score)


