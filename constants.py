#Ordered directions for rotation logic
DIRECTIONS = ['N', 'E', 'S', 'W']

#Movement vectors for each direction:
#change in x and y when moving forward
MOVE_MAP = {
    'N': (0, 1),   # Move up
    'E': (1, 0),   # Move right
    'S': (0, -1),  # Move down
    'W': (-1, 0)   # Move left
}