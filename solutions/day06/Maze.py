from library import turn_right

move_in_circles = False
counter = 0

while not at_goal():
    if right_is_clear() and not move_in_circles :
        turn_right()
        move()
        counter += 1
        if counter >= 4:
            move_in_circles = True
    elif front_is_clear():
        move()
        counter = 0
        move_in_circles = False
    else:
        turn_left()
        counter = 0
        move_in_circles = False
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    for num in range(0,3):
        turn_left()
def movex(how_far: int):
    for num in range(0,how_far):
        move()
        
def turn_around():
    turn_left()
    turn_left()
        
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()