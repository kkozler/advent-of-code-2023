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
# print(sum(int(m.group()) for li, l in enumerate(lines) for m in re.finditer('[0-9]+', l) if l[max(m.start() - 1, 0)] not in ('.', '\n') and not l[max(m.start() - 1, 0)].isalnum() or l[min(m.end(), len(lines[0]) - 1)] not in ('.', '\n') and not l[min(m.end(), len(lines[0]) - 1)].isalnum() or (li > 0 and any([(c not in ('.', '\n') and not c.isalnum()) for c in lines[li - 1][max(m.start() - 1, 0):(min(m.end(), len(lines[0]) - 1) + 1)]])) or (li < (len(lines) - 1) and any([(c not in ('.', '\n') and not c.isalnum()) for c in lines[li + 1][max(m.start() - 1, 0):(min(m.end(), len(lines[0]) - 1) + 1)]]))))

def get_adjacent_numbers(line: str, gear: re.Match):
    return [int(n.group()) for n in re.finditer('[0-9]+', line) if n.start() <= gear.start() + 1 and n.end() >= gear.start()]
        
def get_gear_ratio(line: str, line_index: int, gear_match: re.Match):
    adj = get_adjacent_numbers(line, gear_match) + (get_adjacent_numbers(lines[line_index - 1], gear_match) if line_index > 0 else []) + (get_adjacent_numbers(lines[line_index + 1], gear_match) if line_index < len(lines) - 1 else [])
    return adj[0] * adj[1] if len(adj) == 2 else 0

print(sum(get_gear_ratio(line, line_index, gear_match) for line_index, line in enumerate(lines) for gear_match in re.finditer('[*]', line)))  

# for funzies
# print(sum((lambda a: a[0] * a[1] if len(a) == 2 else 0)([int(n.group()) for n in re.finditer('[0-9]+', l) if n.start() <= g.start() + 1 and n.end() >= g.start()] + ([int(n.group()) for n in re.finditer('[0-9]+', lines[li - 1]) if n.start() <= g.start() + 1 and n.end() >= g.start()] if li > 0 else []) + ([int(n.group()) for n in re.finditer('[0-9]+', lines[li + 1]) if n.start() <= g.start() + 1 and n.end() >= g.start()] if li < len(lines) - 1 else [])) for li, l in enumerate(lines) for g in re.finditer('[*]', l)))  
