def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    if wall_on_right() != True:
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear()
        move()
    turn_left()

#main loop
while at_goal() != True:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()




