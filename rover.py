from plateau import Plateau
from constants import DIRECTIONS, MOVE_MAP


class Rover:

    """
    Creaates a single rover on the plateau.

    Handles:
    - Direction changes (L, R), Movement (M) and command execution.
    """

    def __init__(self, x: int, y: int, direction: str, plateau: Plateau):
        #Current position of the rover
        self.x = x
        self.y = y

        #Current facing directionn of the rover (N, E, S, W)
        self.direction = direction

        # plateau for boundary validation
        self.plateau = plateau

    def turn_left(self):
        # Rotate rover 90 degrees to left.
        idx = DIRECTIONS.index(self.direction)

        # Rotate left: decrement index and use modulo to wrap (N -> W)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def turn_right(self):
        # Rotate rover 90 degrees to Right.
        idx = DIRECTIONS.index(self.direction)

        # Rotate Right: increment index and use modulo to wrap (N -> S)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def move(self):
        # Move rover one step forward in the current direction.
        dx, dy = MOVE_MAP[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        #Validate new position coordiantes with the boundary and updates
        if self.plateau.is_within_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def execute_commands(self, commands: str):
        #Execute sequence of commands of string containing - "LRM"
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()
            else:
                 #Handle invalid commands
                raise ValueError(f"Invalid command: {command}")

    def get_position(self) -> str:
        # Get current position and direction as string
        return f"{self.x} {self.y} {self.direction}"