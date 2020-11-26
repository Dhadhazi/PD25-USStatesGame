import turtle

screen = turtle.Screen()
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess a State", prompt="Give me a name of a state")

turtle.mainloop()