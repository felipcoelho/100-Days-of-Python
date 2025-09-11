def turn_left():
    pass

def move():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def move_square(times):
    for time in range(times):
        move()
        square()

move_square(6)      


'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def square(times):
    for time in range(times):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

square(6)   
'''

'''
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

for step in range(6):
    jump()
'''
