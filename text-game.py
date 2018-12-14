from Room import *


# ---------------Variables

player_lat = 2
player_lon = 2
player_exit = "n"
current_room = room1
room_desc = ""
test = ""

# # game loop
# while player_exit != "y":
#     # Intro
#     print("Welcome to Adventuretron you fucking bitch. It's the best game in the world!")
#     print("You find yourself standing in a room. What the fuck do you do?")
#     input("Press enter to begin:")
#     print("\n Enter a command below:")
#
#     while True:
#         # input
#         command = input('>  ')
#         Room.command_dict[command]()
#         print(str(player_lat) + " Lat, " + str(player_lon) + " Lon")
#         find()
#     # play again


# Get the description from the current room when player enters 'look'
command = input("> ")
# print(command_dict[room_dict[command]].desc)

print(command_dict[command])
test = room_dict['room1'].desc
print(test)


