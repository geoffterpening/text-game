from Room import *

# ---------------Variables

player_lat = 2
player_lon = 2
player_exit = "n"

# the following 2 variables create a list, but since there is only one object that (should) fit the parameters, they
# will only have one item, allowing you to call them as need be
current_room_name = [room.name for room in room_list if room.lat == player_lat and room.lon == player_lon]
current_room_description = [room.desc for room in room_list if room.lat == player_lat and room.lon == player_lon]


# --------------Functions

def south():
    global player_lat
    global current_room_description
    global current_room_name
    if player_lat < 3:
        player_lat += 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def north():
    global player_lat
    global current_room_description
    global current_room_name
    if player_lat > 1:
        player_lat -= 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def west():
    global player_lon
    global current_room_description
    global current_room_name
    if player_lon < 3:
        player_lon += 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def east():
    global player_lon
    global current_room_description
    global current_room_name
    if player_lon > 1:
        player_lon -= 1
        current_room_description = [room.desc for room in room_list if
                                    room.lat == player_lat and room.lon == player_lon]
    else:
        print("There is no door there")


def look():
    global current_room_description
    print(current_room_description[0])


def exit_program():
    global player_exit
    player_exit = "y"


# this dict converts strings to non strings
command_dict = {
    'north': north,
    'south': south,
    'east': east,
    'west': west,
    'look': look,
    'exit': exit_program,
    'quit': exit_program
}

# -------------------game loop
while player_exit != "y":
    # Intro
    print("Welcome to Adventuretron. It's the best game in the world!")
    print("You find yourself standing in a room. What do you do?")
    input("Press enter to begin:")
    # the below could be worded better (commands not obvious)
    print("\n Enter a command below:")

    while player_exit != "y":
        try:
            # input
            command = input("> ")
            command_dict[command]()
            print(str(player_lat) + " Lat, " + str(player_lon) + " Lon")
            # find()
        except KeyError:
            print("I don't recognize that command.")


print("Goodbye!")
input('press any key to exit')