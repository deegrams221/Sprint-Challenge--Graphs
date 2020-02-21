from room import Room
from player import Player
from world import World
# Import Queue and Stack from util
from util import Queue, Stack

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Notes from README:
# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal.
# You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.
# 1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.
# 2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Graph as a dict
mapDictionary = {}


# trying with bfs to search for shortest path
def bfs(starting_room_id):
    # Create an empty queue
    # Add a path to the starting room to the queue
    # Create an empty set to store visited
    # While the queue is not empty...
        # Dequeue the first path
        # Grab the last room from the path
        # add current_room to visited
        # For each direction in the map graph's current room...
            # check if the current room's direction is a '?'...
                # if it is, return path
            # check else if the current room's direction is not visited...
                # if not, create a new path, add the direction


# using dft to create the maze
def dft(starting_room):
    # reverse the directions
    # create counter for rooms the player has been to
    # while the len of mapDictionary is not equal to the len of the graph...
        # see the room currently in
        # find the room id of the current room
        # create a dict for the rooms
        # check if the room id is not in the mapDictionary...
            # then find the possible exits
                # add the '?' into the room_dict
            # update the room
                # find the previous room
                # add the previous room to the room counter and the room_dict
            #  add the unexplored rooms to the room id
        # otherwise...
            # add the room id from mapDictionary to the inner room dict
        # create an empyt list of possible exits
        # iterate throuogh the room dict
            # check if '?' is at the index direction...
                # if so, add the direction to the possible exxits list
        # check if there is an unknown direction...
            # use random and shuffle the possible exits
            # set the direction to the zero index of possible exits
            # add the direction to the traversal path
            # to move the player in that direction, use travel function
            # Next, replace mapDictionary's '?' with next discovered room id
            # Grab player's current room
            # set mapDictionary current room id and direction to player room id
            # now set the current room id to the visited room id
        # otherwise...
            # going to use bfs to search for next exit or possible rooms
            # check if the path of the next room is not None and if len of next room not None...
                # find index in the range of the len on the next room - 1 (not include current room)...
                    # find direction in mapDictionary of index of next room
                        # check if the mapDictionary's index of next room and direction is equal to the index + 1 of next room
                            # if so, then add the direction to traversal path
                            # then move the player to that room
            # otherwise, break




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