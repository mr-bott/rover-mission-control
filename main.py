from plateau import Plateau
from rover import Rover


def main():

    # print("Enter Plateau size and Coordinates and commands: \n")

    #Take map size and store it (lower side assumed to be 0,0 )
    max_x, max_y = map(int, input().split())
    plateau = Plateau(max_x, max_y) #create plateau of given size 

    # Store final results of all rovers
    results = []

    try:

        while True:
            
            # Take rover initial position (x, y, and direction)
            position_input = input().strip()

            # Stop if no more input provided
            if not position_input:
                break

            x, y, direction = position_input.split()
            x, y = int(x), int(y)

            # Take movement commands (L, R, M)
            commands = input().strip()

            # Create a rover instance with provided details
            rover = Rover(x, y, direction, plateau)

            # Execute all commands
            rover.execute_commands(commands)

            #Save final position
            results.append(rover.get_position())

    except EOFError:
        # Handle end-of-file (useful when input is piped from file)
        pass
    
    print("Final Coordinates: \n")
    # Print final positions of all rovers
    for result in results:
        print(result)


if __name__ == "__main__":
    # Entry point of the program
    main()