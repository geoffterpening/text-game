# Room stuff in separate file to make it easier to keep track of / edit / add features / keep app clean
class Room:
    def __init__(self, name, lat, lon, desc):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.desc = desc

# each room has to have unique & contiguous coordinates. Mechanic does not support non-rectangular maps at this point
# if you add to this list, adjust the functions in app.py to allow for higher coords.
room_list = {
    Room("Room1", 1, 1, "You are standing in a room, the floor has a number 1 carved into it"),
    Room("Room2", 1, 2, "You are standing in a room, the floor has a number 2 carved into it"),
    Room("Room3", 1, 3, "You are standing in a room, the floor has a number 3 carved into it"),
    Room("Room4", 2, 1, "You are standing in a room, the floor has a number 4 carved into it"),
    Room("Room5", 2, 2, "You are standing in a room, the floor has a number 5 carved into it"),
    Room("Room6", 2, 3, "You are standing in a room, the floor has a number 6 carved into it"),
    Room("Room7", 3, 1, "You are standing in a room, the floor has a number 7 carved into it"),
    Room("Room8", 3, 2, "You are standing in a room, the floor has a number 8 carved into it"),
    Room("Room9", 3, 3, "You are standing in a room, the floor has a number 9 carved into it")
}
