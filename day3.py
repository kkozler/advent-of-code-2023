import re

input = open('input/day3.txt', 'r')
lines = input.readlines()

line_length = len(lines[0])

part_number_sum = 0

def is_symbol(char: str) -> bool:
    return char != '.' and not char.isalpha() and not char.isnumeric() and char != '\n'

def is_adjacent_to_symbol(match: re.Match, line_index: int, line: str) -> bool:
    start_search = max(match.start() - 1, 0)
    end_search = min(match.end(), line_length - 1)
    
    # look left
    if is_symbol(line[start_search]):
        return True
    
    # look right
    if is_symbol(line[end_search]):
        return True
        
    # look up
    if line_index > 0 and any([is_symbol(c) for c in lines[line_index - 1][start_search:(end_search + 1)]]):
        return True
        
    # look down
    if line_index < (len(lines) - 1) and any([is_symbol(c) for c in lines[line_index + 1][start_search:(end_search + 1)]]):
        return True
        
    return False
    
for line_index, line in enumerate(lines):
    for match in re.finditer('[0-9]+', line):
        if is_adjacent_to_symbol(match, line_index, line):
            part_number_sum += int(match.group())

print(part_number_sum)

# for funzies
# print(sum(int(match.group()) for line_index, line in enumerate(lines) for match in re.finditer('[0-9]+', line) if line[max(match.start() - 1, 0)] not in ('.', '\n') and not line[max(match.start() - 1, 0)].isalnum() or line[min(match.end(), len(lines[0]) - 1)] not in ('.', '\n') and not line[min(match.end(), len(lines[0]) - 1)].isalnum() or (line_index > 0 and any([(c not in ('.', '\n') and not c.isalnum()) for c in lines[line_index - 1][max(match.start() - 1, 0):(min(match.end(), len(lines[0]) - 1) + 1)]])) or (line_index < (len(lines) - 1) and any([(c not in ('.', '\n') and not c.isalnum()) for c in lines[line_index + 1][max(match.start() - 1, 0):(min(match.end(), len(lines[0]) - 1) + 1)]]))))

def get_adjacent_numbers(line: str, gear: re.Match):
    return [int(n.group()) for n in re.finditer('[0-9]+', line) if n.start() <= gear.start() + 1 and n.end() >= gear.start()]
        
def get_gear_ratio(line: str, line_index: int, gear_match: re.Match):
    adj = get_adjacent_numbers(line, gear_match) + (get_adjacent_numbers(lines[line_index - 1], gear_match) if line_index > 0 else []) + (get_adjacent_numbers(lines[line_index + 1], gear_match) if line_index < len(lines) - 1 else [])
    return adj[0] * adj[1] if len(adj) == 2 else 0

print(sum(get_gear_ratio(line, line_index, gear_match) for line_index, line in enumerate(lines) for gear_match in re.finditer('[*]', line)))  

# for funzies
# print(sum((lambda adj: adj[0] * adj[1] if len(adj) == 2 else 0)([int(n.group()) for n in re.finditer('[0-9]+', line) if n.start() <= gear_match.start() + 1 and n.end() >= gear_match.start()] + ([int(n.group()) for n in re.finditer('[0-9]+', lines[line_index - 1]) if n.start() <= gear_match.start() + 1 and n.end() >= gear_match.start()] if line_index > 0 else []) + ([int(n.group()) for n in re.finditer('[0-9]+', lines[line_index + 1]) if n.start() <= gear_match.start() + 1 and n.end() >= gear_match.start()] if line_index < len(lines) - 1 else [])) for line_index, line in enumerate(lines) for gear_match in re.finditer('[*]', line)))  
