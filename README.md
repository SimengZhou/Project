Simeng Zhou: szhou31@stevens.edu

GitHub: https://github.com/SimengZhou/Project 

Estimated time: around 48 hours

How to test: I use 'python adventure.py testloop.map' to test my program.
Here are the commands and results: 
[
(base) C:\Users\12722\anaconda3\Assignments\Project>python adventure.py testloop.map
> A white room

You are in a simple room with white walls.

Exits: north south

What would you like to do? ?
Can't understand your command. You can use 'help'.
What would you like to do? help
You can run the following commands: 
  go ...
  get ...
  drop ...
  look
  inventory
  quit
  help
What would you like to do? go
Sorry, you need to 'go' somewhere.
What would you like to do? get
Sorry, you need to 'get' something.
What would you like to do? drop
Sorry, you need to 'drop' something.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? look
> A white room

You are in a simple room with white walls.

Exits: north south

What would you like to do? go north
You go north.

> A blue room

There is a pond in front of you.

Items: water

Exits: south east

What would you like to do? get water
You pick up the water.
What would you like to do? go east
You go east.

> A green room

This room is full of flowers.

Items: seeds

Exits: west

What would you like to do? get seeds
You pick up the seeds.
What would you like to do? inventory
Inventory:
  water
  seeds
What would you like to do? go east
There's no way to go east.
What would you like to do? look
> A green room

This room is full of flowers.

Exits: west

What would you like to do? get flowers
There's no flowers anywhere.
What would you like to do? go west
You go west.

> A blue room

There is a pond in front of you.

Exits: south east

What would you like to do? go south
You go south.

> A white room

You are in a simple room with white walls.

Exits: north south

What would you like to do? go south
A greenhouse is unlocked.
You go south.

> A greenhouse

You plant the seeds and roses grow up.

Items: roses

Exits: north down

What would you like to do? inventory
You're not carrying anything.
What would you like to do? get roses
You pick up the roses.
What would you like to do? go down
You go down.

> An empty room

You are in an empty room. There are three doors with different colors.

Exits: up brown grey purple down

What would you like to do? go up
You go up.

> A greenhouse

You plant the seeds and roses grow up.

Exits: north down

What would you like to do? go down
You go down.

> An empty room

You are in an empty room. There are three doors with different colors.

Exits: up brown grey purple down

What would you like to do? go brown
A rich room is locked. You should use shovel to unlock.
What would you like to do? go grey
You go grey.

> A warehouse

This room is piled with stuff. You find a shovel in the corner.

Items: shovel

Exits: out

What would you like to do? get shovel
You pick up the shovel.
What would you like to do? go out
You go out.

> An empty room

You are in an empty room. There are three doors with different colors.

Exits: up brown grey purple down

What would you like to do? go brown
A rich room is unlocked.
You go brown.

> A rich room

There is a pile of dirt. You use the shovel and find something.

Items: gold coins

Exits: out

What would you like to do? get gold coins
You pick up the gold coins.
What would you like to do? inventory
Inventory:
  roses
  gold coins
What would you like to do? go out
You go out.

> An empty room

You are in an empty room. There are three doors with different colors.

Exits: up brown grey purple down

What would you like to do? go purple
A myserious room is unlocked.
You go purple.

> A myserious room

You use gold coins to make magic appear.

Items: sword

Exits: out

What would you like to do? get sword
You pick up the sword.
What would you like to do? go out
You go out.

> An empty room

You are in an empty room. There are three doors with different colors.

Exits: up brown grey purple down

What would you like to do? go down
You go down.

> A safe room

You are in the safe room. It's very dangerous to go down. Don't do that!

Exits: up down east

What would you like to do? go east
You go east.

> A room for relaxation

Warning: you are close to the Boss!!! Please prepare yourself!

Exits: west east

What would you like to do? go east
The Boss room is locked. You should use key to unlock.
What would you like to do? go west
You go west.

> A safe room

You are in the safe room. It's very dangerous to go down. Don't do that!

Exits: up down east

What would you like to do? go down
You go down.

> A dangerous room

You are fooled! This room is actually not dangerous! You find a key.

Items: key

Exits: up

What would you like to do? get key
You pick up the key.
What would you like to do? inventory
Inventory:
  roses
  sword
  key
What would you like to do? go up
You go up.

> A safe room

You are in the safe room. It's very dangerous to go down. Don't do that!

Exits: up down east

What would you like to do? go east
You go east.

> A room for relaxation

Warning: you are close to the Boss!!! Please prepare yourself!

Exits: west east

What would you like to do? go east
The Boss room is unlocked.
You go east.

> The Boss room

There is a monster. You use the sword to kill it. During the fight, you drop your roses.

Exits: west

What would you like to do? drop roses
You drop the roses.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? go west
You go west.

> A room for relaxation

Warning: you are close to the Boss!!! Please prepare yourself!

Exits: west east

What would you like to do? go east
You go east.

> The Boss room

There is a monster. You use the sword to kill it. During the fight, you drop your roses.

Items: roses

Exits: west

What would you like to do? drop roses
You don't have roses.
What would you like to do?
Use 'quit' to exit.
What would you like to do? quit
Goodbye!

]

Issues: 
When I tpye Ctrl-D, the program can not catch EOFError. I tried a lot of methods to solve this problem, but I failed. I can't get the result like:
        What would you like to do? ^D
        Use 'quit' to exit.

Example of a bug or issue: 
At first, I didn't consider that once a room is unlocked, the player should go into it freely. It turned out to be like, I unlocked a room and the room was locked again after I went out. Then I cleared out the 'is_locked' list when the room is successfully unlocked and the problem was solved.

Extensions:
1. "drop": It's a new verb. 
If you just use 'drop', the program will return "Sorry, you need to 'drop' something.". 
If the item you want to drop is not in your inventory, it will return "You don't have {item}.".
If the command is correct, the program will remove the item from your inventory and add it to the current room.

2. "help": It's a new verb.
If you use 'help', the program will show all the verbs that players can use in this game.
It will also show which verbs need targets.
If you want to add new verbs, you can add the new one to the dictionary of verbs and the 'help' command will automatically add it to its texts.

3. "locked doors": It's a new parameter of Room class.
Some rooms are locked and some are not, so this parameter is free to be defined in the map file. 
The 'is_locked' parameter is a list of items to unlock a room.
If you use "go 'direction'" command, the program will check whether the 'is_locked' list of the direction's room is empty. 
If the list is not empty, the program will check whether each item that required to unlock the room is in the inventory.
If any required item is not in the inventory, the program will return a text to indicate that the direction's room is locked and which items are needed to unlock it.
If the list doesn't exist or the list is empty, you can go into the room. 
