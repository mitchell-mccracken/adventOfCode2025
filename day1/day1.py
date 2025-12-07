import os
import math

# file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
file_path = os.path.join(os.path.dirname(__file__), 'sample.txt')

starting_position = 50
count = 0

with open(file_path, 'r') as file:
  lines = file.readlines()
  for line in lines:
    print(line.strip())
    direction = 1 if line[0] == 'R' else -1
    distance = int(line[1:]) * direction
    print(direction, distance)
    starting_position += distance
    print("Current Position:", starting_position)
    if starting_position%100 == 0:
      count += 1
    
    # if starting_position < 0:
    #   count += 1
    
    # rotations = math.floor(abs(starting_position) / 100)
    # count += rotations

    starting_position = starting_position % 100
    print("count is now:", count)

# print("Final Position:", starting_position)