#advent of code day 1

#part 1
#open file
with open('day1.txt') as f:
    data = f.read()

elves = data.split('\n\n')

#using list comprehension 
calories = sorted([sum(map(int,elf.split('\n'))) for elf in elves], reverse=True)


print(f"Part 1: {calories[0]}")
print(f"Part 2: {sum(calories[:3])}")