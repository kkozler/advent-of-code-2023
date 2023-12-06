types = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

values = []
mapped = []

for line in open('input/day5.txt', 'r').readlines():
    if line == '\n':
        continue
    
    if line.startswith('seeds:'):
        values = [int(x) for x in line.split(':')[1].strip().split()]
        mapped = [False] * len(values)
        continue
    
    if line.endswith('map:\n'):
        mapped = [False] * len(values)
        continue

    destination, source, length = [int(x) for x in line.split()]
    
    for i, value in enumerate(values):
        if mapped[i]:
            continue            
        if source <= value <= (source + length):
            values[i] = destination + (value - source)
            mapped[i] = True
        
print(min(values))
