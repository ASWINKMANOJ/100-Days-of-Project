import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.listen()
guessed = []
while len(guessed) < 50:

    answer_state = screen.textinput(title=f"{len(guessed)}/50", prompt="What the another the state?").title()

    if answer_state == "Exit":
        missed_state = [state for state in states if state not in guessed]
        new_data = pandas.DataFrame(missed_state)
        new_data.to_csv("States to Learn.csv")
        break

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed.append(answer_state)
