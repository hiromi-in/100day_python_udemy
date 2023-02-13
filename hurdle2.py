#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def to_the_right():
    turn_right()
    move()

def one_hurdle():
    move()
    turn_left()
    move()
    to_the_right()
    to_the_right()
    turn_left()

while at_goal() != True:
    one_hurdle()




