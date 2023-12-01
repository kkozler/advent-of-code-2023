import re

input = open('input/day1.txt', 'r')
lines = input.readlines()
 
sum = 0
for line in lines:
    digits = re.findall(r'[0-9]', line)
    sum += int(digits[0] + digits[len(digits) - 1])

print(sum)

all_digit_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0   

for line in lines:    
    first_digit = None
    last_digit = None
    
    for char_ix, char in enumerate(line):
        if char.isnumeric():
            if first_digit is None:
                first_digit = char
            else:
                last_digit = char
            continue

        for digit_ix, digit in enumerate(all_digit_strings):
            if (line.find(digit, char_ix) - char_ix) == 0:
                if first_digit is None:
                    first_digit = str(digit_ix)
                else:
                    last_digit = str(digit_ix)

    if first_digit is None and last_digit is not None:
        first_digit = last_digit
    if last_digit is None and first_digit is not None:
        last_digit = first_digit
        
    number = int(first_digit + last_digit)
    sum += number
    
print(sum)    