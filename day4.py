input = open('input/day4.txt', 'r')

lines = input.readlines()

def get_points(line: str):
    card, numbers = [x.strip() for x in line.split(':')]
    winning, given = [x.strip().split() for x in numbers.split('|')]
    points = 0
    for number in given:
        if number in winning:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

print(sum(get_points(line) for line in lines))

def get_number_of_scratchcards_recursive(line_index: int) -> int:
    winning, given = [x.strip().split() for x in lines[line_index].split(':')[1].split('|')]
    scorecards = len([number for number in given if number in winning])
    if scorecards == 0:
        return scorecards
    start = min(line_index + 1, len(lines) - 1)
    stop = min(line_index + scorecards, len(lines) - 1)
    for i in range(start, stop + 1):
        scorecards += (get_number_of_scratchcards_recursive(i) or 0)
    return scorecards

print(sum([get_number_of_scratchcards_recursive(i) + 1 for i in range(len(lines))]))