#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

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
    if not front_is_clear():
        one_hurdle()
    elif front_is_clear():
        move()
        
#while not at_goal():
#     if wall_in_front():
#        one_hurdle()
#     else:
#        move()
        
    
