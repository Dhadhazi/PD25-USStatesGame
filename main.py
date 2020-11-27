import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
state_namelist = states_data.state.to_list()

guessed_list = [];

mrpen = turtle.Turtle()
mrpen.penup()
mrpen.hideturtle()


def state_exists(state):
    if state in state_namelist:
        return True
    else:
        return False


def get_state_data(state):
    return states_data[states_data.state == state]


def write_state(state):
    data = get_state_data(state)
    mrpen.goto(int(data.x), int(data.y))
    mrpen.write(state, True, align="center")


def missing_states():
    return [state for state in state_namelist if state not in guessed_list]


def write_csv(states):
    data = pandas.DataFrame(states)
    data.to_csv("states_to_learn.csv")


while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct",
                                    prompt="Give me a name of a state").title()
    if answer_state == "Exit":
        write_csv(missing_states())
        break

    if state_exists(answer_state) and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        write_state(answer_state)