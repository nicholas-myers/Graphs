from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

start_room = world.starting_room
opposites = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
}

copy_rooms = {}

for r in world.rooms:
    copy_rooms[world.rooms[r].name] = world.rooms[r].get_exits()
# print(copy_rooms)


def get_path(starting_room):
    # get the total number of rooms
    total_rooms = len(world.rooms)
    print(total_rooms)
    visited = []
    # keep track of the last room with unvisited paths
    # create a copy of the last room visited with unvisited paths
    cur_room = starting_room
    prev_dir = None
    
    while len(visited) != total_rooms:
        print(cur_room.name)
        if cur_room.name not in visited:
            visited.append(cur_room.name)
        print(visited)
        dirs = cur_room.get_exits()
        if len(dirs) == 1:
            player.travel(dirs[0])
            traversal_path.append(dirs[0])
            prev_dir = opposites[dirs[0]]
            cur_room = player.current_room
            print(cur_room.name)
        else:
            print(dirs)
            print(prev_dir)
            if prev_dir != None:
                copy_rooms[cur_room.name].remove(prev_dir)
            print(copy_rooms[cur_room.name])
            ran_dir = random.randint(1, len(copy_rooms[cur_room.name])) - 1
            player.travel(copy_rooms[cur_room.name][ran_dir])
            traversal_path.append(copy_rooms[cur_room.name][ran_dir])
            cur_room = player.current_room
get_path(start_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# print(visited_rooms)
#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
