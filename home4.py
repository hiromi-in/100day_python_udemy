#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else:
        turn_right()
