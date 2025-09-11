def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until hitting a wall
while front_is_clear():
    move()
turn_left()

# Now follow the right-hand rule
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()