#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def to_the_right():
    turn_right()
    move()

def one_hurdle():
    turn_left()
    move()
    to_the_right()
    to_the_right()
    turn_left()
    
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and right_is_clear():
        to_the_right()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and right_is_clear():
        to_the_right()
       
    
    
