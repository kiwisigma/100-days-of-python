def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()




#main loop
while at_goal() != True:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()




