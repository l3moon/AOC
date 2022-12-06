#advent of code day2 

with open('day2.txt') as f:
    data = f.readlines()
#get the 9 possiblities 
possibilities = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

total = sum([possibilities[edx.strip()] for edx in data])

print(f"total: {total}")

