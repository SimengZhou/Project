import sys
import json

def validate_map(map_data):
    try:
        # Check if map_data is a dictionary
        if not isinstance(map_data, dict):
            raise ValueError("Map must be a JSON object")

        # Check if "start" and "rooms" keys exist
        if "start" not in map_data or "rooms" not in map_data:
            raise ValueError("Map must contain 'start' and 'rooms' keys")

        rooms = set()
        exits = set()

        # Check each room
        for room in map_data["rooms"]:
            # Check if room is a dictionary
            if not isinstance(room, dict):
                raise ValueError("Each room must be a JSON object")

            # Check if room has name, desc, and exits
            if "name" not in room or "desc" not in room or "exits" not in room:
                raise ValueError("Each room must have 'name', 'desc', and 'exits' keys")

            # Check if name is unique
            room_name = room["name"]
            if room_name in rooms:
                raise ValueError("Room names must be unique")
            rooms.add(room_name)

            # Check exits
        for exit_dir, exit_room in room["exits"].items():
            # Check if exit_room is a string
            if not isinstance(exit_room, str):
                raise ValueError("Exit room IDs must be strings")

            # Check if exit_room ID is valid
            if exit_room not in rooms:
                raise ValueError(f"Invalid exit room ID '{exit_room}' in room '{room_name}'")

            # Check if exit direction is unique
            exit_key = f"{room_name}:{exit_dir}"
            if exit_key in exits:
                raise ValueError(f"Duplicate exit '{exit_dir}' in room '{room_name}'")
            exits.add(exit_key)

        # If all checks pass, map is valid
        return True
    except ValueError as e:
        print(e, file=sys.stderr)
        return False
    
class Room:
    def __init__(self, name, desc, exits, items=None):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items if items else []
    
    def __str__(self):
        exits_str = ' '.join(self.exits.keys())
        items_str = ', '.join(self.items) if self.items else "None"
        return f"{self.name}\n\n{self.desc}\n\nItems: {items_str}\n\nExists: {exits_str}\n"

class Player:
    def __init__(self):
        self.cur_room = None
        self.inventory = []
        
    def print_info(self):
        print(f"> {self.cur_room.name}\n\n{self.cur_room.desc}\n")

        # print items (if the current room has items)
        if self.cur_room.items:
            print_items = ', '.join(self.cur_room.items)
            print(f"Items: {print_items}\n")
        else:
            print_items = "None"

        # print exits
        print_exits = ' '.join(self.cur_room.exits.keys())
        print(f"Exits: {print_exits}\n")

    def go(self, direction):
        if direction in self.cur_room.exits:
            print(f"You go {direction}.\n")
            self.cur_room = self.cur_room.exits[direction]
            self.print_info()
        else:
            print(f"There's no way to go {direction}.")
    
    def look(self):
        self.print_info()

    def get(self, item):
        if item in self.cur_room.items:
            print(f"You pick up the {item}.")
            self.cur_room.items.remove(item)
            self.inventory.append(item)
        else:
            print(f"There's no {item} anywhere.")
              
    def drop(self, item):
        if item in self.inventory:
            print(f"You drop the {item}.")
            self.inventory.remove(item)
            self.cur_room.items.append(item)
        else:
            print(f"You don't have {item}.")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"  {item}")

    def help(self):
        print("You can run the following commands: ")
        for verb, target in verbs.items():
            if target:
                print(f"  {verb} ...")
            else:
                print(f"  {verb}")

def main():
    # Play the game
    while True:
        try:
            answer = input("What would you like to do? ").strip().lower().split()

            if not answer:
                continue

            verb = answer[0]
            if verb == "go":                     # go somewhere
                if len(answer) < 2:
                    print("Sorry, you need to 'go' somewhere.")
                    continue
                direction = answer[1]
                player.go(direction)

            elif verb == "look":                 # look around the room
                player.look()

            elif verb == "get":                  # get an item from a room
                if len(answer) < 2:
                    print("Sorry, you need to 'get' something.")
                    continue
                item = answer[1]
                player.get(item)

            elif verb == "drop":                 # Extension: drop an item
                if len(answer) < 2:
                    print("Sorry, you need to 'drop' something.")
                    continue
                item = answer[1]
                player.drop(item)

            elif verb == "inventory":            # show the inventory
                player.show_inventory()

            elif verb == "quit":                 # quit the game
                print("Goodbye!")
                break

            elif verb == "help":                 # Extension: show help
                player.help()
        except (EOFError, KeyboardInterrupt):
            print("\nUse 'quit' to exit.")

def load_map(mapfile):
    with open(mapfile, "r") as file:
        map_data = json.load(file)
    return map_data

if __name__ == "__main__":
    # Read the map data
    try:
        map_data = load_map(sys.argv[1])
    except FileNotFoundError:
        print("File not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format", file=sys.stderr)
        sys.exit(1)

    # Validate map
    if not validate_map(map_data):
        sys.exit(1)

    # Create the Room objects
    rooms = {}              # use a dict to store room objects
    for room in map_data["rooms"]:
        room_data = Room(room["name"], room["desc"], room["exits"], room.get("items", []))
        rooms[room["name"]] = room_data
    
    # link rooms
    for room in map_data["rooms"]:
        cur_room = rooms[room["name"]]
        for direction, name in room["exits"].items():
            cur_room.exits[direction] = rooms[name]

    # Create a Player object
    player = Player()
    # Initialize the player's room 
    player.cur_room = rooms[map_data["start"]]
    # print the initial room's information
    player.print_info()

    verbs = {
        "go": "direction",
        "get": "item",
        "drop": "item",
        "look": None,
        "inventory": None,
        "quit": None,
        "help": None
    } 

    main()

    sys.exit(0)