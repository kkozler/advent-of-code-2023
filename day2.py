input = open('input/day2.txt', 'r')
lines = input.readlines()

summed_ids = 0
target = { 'red': 12, 'green': 13, 'blue': 14 }

def is_possible(draw: str) -> bool:
    return all(int(color.split()[0]) <= target[color.split()[1]] for color in draw.split(','))

for line in lines:
    game, draws = line.split(':')
    if all(is_possible(draw) for draw in draws.split(';')):
        summed_ids += int(game.split()[1])
        
print(summed_ids)

def get_power(line: str) -> int:
    max_by_color = { 'red': float('-inf'), 'blue': float('-inf'), 'green': float('-inf') }
    for draw in [x.strip() for x in line.split(':')[1].split(';')]:
        for number, color in [x.strip().split() for x in draw.split(',')]:
            max_by_color[color] = max(max_by_color[color], int(number))
    return max_by_color['red'] * max_by_color['blue'] * max_by_color['green']    
    
print(sum([get_power(line) for line in lines]))