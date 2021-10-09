letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#1
letter_to_points = {key:value for key, value in zip(letters, points)}
#print(letter_to_points)

#2
letter_to_points[" "] = 0
#print(letter_to_points)

#3-6
def score_word(value):
  point_total = 0
  for number in value:
    point_total += letter_to_points.get(number,0)
  return point_total

#7
brownie_points = score_word('BROWNIE')

#8
#print(brownie_points)

#9
player_to_words = {
  "Player Lonely": ["WISHING", "FOR", "FRIENDS"], 
  "wordNerd": ["EARTH", "ERASER", "FRIENDS"], 
  "Lexi Con": ["EYES", "BELLY", "HUSKY"], 
  "Prof Reader": ["MACHINE", "COMA", "PERIOD"]
  }

#10
player_to_points = {}

#11-13 & #15B
def update_point_totals():
  for key, values in player_to_words.items():
    player_points = 0
    for value in values:
      player_points += score_word(value)
    player_to_points[key] = player_points

#14
#print(player_to_points)

#15A
def play_word(player, word):
  player_to_words[player].append(word)
play_word('Player Lonely', "It's leg day".upper())
#print(player_to_words)
#print(player_to_points)