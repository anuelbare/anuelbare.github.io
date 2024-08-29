def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()


while at_goal() is False:
    if front_is_clear() is False:
        turn_left()
    else:
        move()
    if wall_on_right() is False:
        turn_right()
    # else:
    #   jump()