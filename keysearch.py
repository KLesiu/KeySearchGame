import sys
import random

#Declare variables which will contain coordinates for key and player position
key_coordinates = [0,0]
player_coordinates = [0,0]

#Declare variable which will contain how many times user moves his player
move_counter = 0

#Function that gives random coordinates to key and player
def get_random_coordinates():
    global key_coordinates
    global player_coordinates
    key_coordinates[0] = random.randint(1,8)
    key_coordinates[1] = random.randint(1,8)
    player_coordinates[0] = random.randint(1,8)
    player_coordinates[1] = random.randint(1,8)

#Function that moves our player position
def player_move(button):
    global move_counter
    if button == "W" or button == "w":
        if player_coordinates[1] == 8:
            return print("You cant move up because you are at the highest Y coordinate (8)")
        player_coordinates[1] += 1
    elif button == "S" or button == "s":
        if player_coordinates[1] == 1:
            return print("You cant move up because you are at the lowest Y coordinate (1)")
        player_coordinates[1] -= 1
    elif button == "A" or button == "a":
        if player_coordinates[0] == 1:
            return print("You cant move up because you are at the lowest X coordinate (1)")

        player_coordinates[0] -= 1
    elif button == "D" or button == "d":
        if player_coordinates[0] == 8:
            return print("You cant move up because you are at the highest X coordinate (8)")
        player_coordinates[0] += 1
    else:
        return print("You can use only W/S/A/D buttons!")
    move_counter += 1
    

#Function that shows how far from the target we are 
def show_result(button):
    if button == "w" or button == "W" or button == "s" or button == "S" or button == "a" or button == "A" or button == "d" or button == "D": 
        global key_coordinates
        global player_coordinates
        if key_coordinates[0] == player_coordinates[0] and key_coordinates[1] == player_coordinates[1]:
            print("Congratulations! You found a key!")
            
        elif key_coordinates[0] == player_coordinates[0] or key_coordinates[1] == player_coordinates[1]:
            print("Nice move! You are close to the key.")
        else:
            print("Oh dear!, Keep looking.")
    else:
        return



get_random_coordinates()

#Get different coordinates when both pairs are identical
while player_coordinates[0] == key_coordinates[0] and player_coordinates[1] == key_coordinates[1]:
    get_random_coordinates()

#Show information about a rules of our game
print(f'So, your coordinates are [{player_coordinates[0]},{player_coordinates[1]}]. You have to find a key if you want to win the game! You can move your player with W/S/A/D. W and S are responsible for coordinate y, S/D are responsible for coordinate x')


while player_coordinates[0] is not key_coordinates[0] or player_coordinates[1] is not key_coordinates[1]:
    move = input("Move your player! ")
    player_move(move)
    show_result(move)


print(f"Key coordinates: [{key_coordinates[0]},{key_coordinates[1]}]")
print(f"You won the game in {move_counter} moves!")
sys.exit(0)




