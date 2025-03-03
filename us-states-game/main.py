import turtle, pandas
from correct_state import CorrectState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name").title()
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(guess)

screen.mainloop()


#What I've created
# data_dict = data.to_dict()
# guess = screen.textinput("Guess the State",prompt="What's another state's name").title()
#
# numbers = []
# for i in range(50):
#     numbers.append(i)
#
# for num in numbers:
#     if data_dict["state"][num] == guess:
#         correct_state = CorrectState(guess,(data_dict["x"][num],data_dict["y"][num]))
#         score += 1
#         numbers.remove(num)
#
# while len(numbers):
#     guess = screen.textinput("Guess the State", prompt=f"{50-len(numbers)}/50 States Correct")
#     guess = guess.title()
#     if guess == "Exit":
#         break
#     for num in numbers:
#         if data_dict["state"][num] == guess:
#             correct_state = CorrectState(guess, (data_dict["x"][num], data_dict["y"][num]))
#             score += 1
#             numbers.remove(num)
#
# screen.mainloop()
#
# #states to learn.csv
# states_to_learn = {"state" : []}
# for num in numbers:
#     states_to_learn["state"].append(data_dict["state"][num])
# file = pandas.DataFrame(states_to_learn)
# file.to_csv("learn.csv")
