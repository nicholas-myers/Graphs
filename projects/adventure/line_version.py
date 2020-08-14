def get_path(starting_room):
    # get the total number of rooms
    total_rooms = len(world.rooms)
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
            if prev_dir != None:
                copy_rooms[cur_room.name].remove(prev_dir)
            print(copy_rooms[cur_room.name])
            ran_dir = random.randint(1, len(copy_rooms[cur_room.name])) - 1
            player.travel(copy_rooms[cur_room.name][ran_dir])
            traversal_path.append(copy_rooms[cur_room.name][ran_dir])
            cur_room = player.current_room
get_path(start_room)