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
    
def print_info(cur_room, map_data):
    room_info = next((room for room in map_data.get("rooms", []) if room["name"] == cur_room), {})
    print("> " + room_info["name"] + "\n")
    print(room_info["desc"] + "\n")
    if "items" in room_info and room_info["items"]:
        print("Items:", end = " ")
        [print(item, end = " ") for item in room_info["items"]]
        print("\n")
    print("Exits:", end = " ")
    for key in room_info["exits"]:
        print(key, end = " ")  
    print("\n")

def main():
    try:
        path = "C:\\Users\\12722\\anaconda3\\Assignments\\Project\\"
        with open(path + "loop.map.json", "r") as file:
            map_data = json.load(file)
    except FileNotFoundError:
        print("File not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format", file=sys.stderr)
        sys.exit(1)

    # Validate map
    if not validate_map(map_data):
        sys.exit(1)

    # Print the first room
    start_room = map_data["start"]
    print_info(start_room, map_data)

    # preparation
    cur_room = start_room
    inventory = []
    verbs = {
        "go": "direction",
        "get": "item",
        "drop": "item",
        "look": None,
        "inventory": None,
        "quit": None,
        "help": None
    } 
    
    # loop
    while True:
        try:
            answer = input("What would you like to do?").strip().lower()
            if answer.startswith("go"):                 # go somewhere
                parts = answer.split(" ", 1)
                if len(parts) < 2 or not parts[1]:
                    print("Sorry, you need to 'go' somewhere.")
                    continue
        
                direction = parts[1]
                room_info = next((room for room in map_data.get("rooms", []) if room["name"] == cur_room), {})
                exits = room_info.get("exits", {})
                if direction not in exits:
                    print(f"There's no way to go {direction}.")
                    continue
                
                print(f"You go {direction}")
                cur_room = room_info["exits"].get(direction)
                print_info(cur_room, map_data)

            elif answer.startswith("look"):                 # look in the room
                print_info(cur_room, map_data)

            elif answer.startswith("get"):                  # get an item from a room
                parts = answer.split(" ", 1)
                if len(parts) < 2 or not parts[1]:
                    print("Sorry, you need to 'get' something.")
                    continue

                get_item = parts[1]
                room_info = next((room for room in map_data.get("rooms", []) if room["name"] == cur_room), {})
                if "items" not in room_info or not room_info["items"]:
                    print(f"There's no {get_item} anywhere.")
                    continue

                print(f"You pick up the {get_item}")
                inventory.append(get_item)
                room_info["items"].remove(get_item)

            elif answer.startswith("drop"):                 # drop an item
                if not inventory:
                    print("You don't have any item.")
                    continue

                parts = answer.split(" ", 1)
                if len(parts) < 2 or not parts[1]:
                    print("Sorry, you need to 'drop' something.")
                    continue

                drop_item = parts[1]
                if drop_item not in inventory:
                    print(f"You don't have {drop_item}")
                    continue

                room_info = next((room for room in map_data.get("rooms", []) if room["name"] == cur_room), {})
                if "items" not in room_info:
                    room_info["items"] = []

                print(f"You drop the {drop_item}")
                inventory.remove(drop_item)
                room_info["items"].append(drop_item)

            elif answer.startswith("inventory"):                    # check inventory
                print("Inventory: ")
                for item in inventory:
                    print("  " + item, end = "\n")

            elif answer.startswith("quit"):                 # quit the game
                print("Goodbye!")
                break

            elif answer.startswith("help"):                 # get help
                print("You can run the following commands: ")
                for verb, target in verbs.items():
                    if target:
                        print(f"  {verb} ...")
                    else:
                        print(f"  {verb}")

        except (EOFError, KeyboardInterrupt):
            print("\nUse 'quit' to exit.")
        
    sys.exit(0)

if __name__ == "__main__":
    main()