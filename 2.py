# convert the input into a list of dictionaries representing the draws
games = []
for line in open('2.txt'):
    draws = []
    for draw in line.strip().split(':')[1].split(';'):
        marbles = [marble.strip() for marble in draw.split(',')]
        draws.append({marble.split(' ')[1]: int(marble.split(' ')[0])
                      for marble in marbles})
    games.append(draws)


# part 1
def is_game_possible(game):
    for draw in game:
        if 'red' in draw and draw['red'] > 12:
            return False
        if 'green' in draw and draw['green'] > 13:
            return False
        if 'blue' in draw and draw['blue'] > 14:
            return False
    return True


possible_sum = 0
for i, game in enumerate(games):
    if is_game_possible(game):
        possible_sum += i + 1
print(possible_sum)

# part 2
power_sum = 0
for game in games:
    max_red = max(draw['red'] for draw in game if 'red' in draw)
    max_green = max(draw['green'] for draw in game if 'green' in draw)
    max_blue = max(draw['blue'] for draw in game if 'blue' in draw)
    power_sum += max_red * max_green * max_blue
print(power_sum)
