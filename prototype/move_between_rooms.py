"""Module Six Milestone starter for the simplified movement prototype."""

# Dictionary linking each room to valid movement directions and destination rooms
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},

}

def main():
    """Run the simplified room movement and exit loop."""
    # Set the player's starting room
    current_room = "Great Hall"

    # Gameplay loop continues until the player enters 'exit'
    while current_room != "exit":
        # 1. Display the player's current room
        print(f"n\You are in the {current_room}.")

        # 2. Prompt for a movement command or 'exit'
        commmand = input("Enter a direction (north, south, east, west) or 'exit': ").strip().lower()

        # 3. Branch based on 'exit', valid move, or invalid input
        if command == "exit":
            current_room = "exit"
            print("Exiting the game. Goodbye!")
        elif command in rooms[current_room]:
            # 4. Update current_room only after a valid movement command
            current_room = rooms[current_room][command]
        else:
            # Input validation error message for unavailable directions or bad commands
            print("Invalid command or unvailable direction. Please try again.")

if __name__ == "__main__":
    main()
