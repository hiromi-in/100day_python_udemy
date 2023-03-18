import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Get state locations
#def get_mouse_click_coor(x, y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
correct_guess = []
missing_state = []

while len(correct_guess) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        if answer_state in correct_guess:
            continue
        else:
            correct_guess.append(answer_state)
            state_index = state_list.index(answer_state)
            state_turtle = turtle.Turtle()
            state_turtle.pu()
            state_turtle.hideturtle()
            state_turtle.goto(x=state_data.iloc[state_index]["x"], y=state_data.iloc[state_index]["y"])
            state_turtle.write(answer_state)

for checked_state in state_list:
    if checked_state not in correct_guess:
        missing_state.append(checked_state)

missing_data = pandas.DataFrame(missing_state)
missing_data.to_csv("missing_states.csv")
