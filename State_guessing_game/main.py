import turtle
import pandas

#Font of the writing that will be on the map
FONT = ('Courier', 10, 'normal')

#Create the background using an gif
screen = turtle.Screen()
screen.title("State Guessing Game")
background_image = "blank_states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)


#Read the data file on the us states
states_data = pandas.read_csv("50_states.csv")

#Extract the names of each state into a list
state_names = states_data["state"].to_list()

#Set starting guesses to 0 
correct_guesses = 0
#Create empty list to be filled with correct guesses
correct_guessed_states = []
states_to_learn = []

#while loop to allow for multiple guesses
#Once corrrect_guesses = 50 they would have guessed every state
while correct_guesses < 50:

    #guessed_state saved as a variable
    guessed_state = screen.textinput(title=f"{correct_guesses} / 50", prompt="Whats another States name?").title()
    
    if guessed_state == "Exit":
        for state in state_names:
            if state not in correct_guessed_states:
                states_to_learn.append(state)
        states_to_learn = pandas.DataFrame(states_to_learn)
        states_to_learn.to_csv("States_to_learn.csv")
        
        break


    #check if guessed state is in the state name list
    for state in state_names:
        
        #If guessed state is correct and its not already been guessed
        if guessed_state == state and guessed_state not in correct_guessed_states:
            #add to the guessed state list
            correct_guessed_states.append(guessed_state)
            #create a turtle, lift pen up and hide turtle
            correct_answer = turtle.Turtle()
            correct_answer.penup()
            correct_answer.hideturtle()

            #Extract the data for the correct state
            guessed_state_data = states_data[states_data.state == f"{guessed_state}"]
            
            #get the x and y coordinate of the correct state
            x_cor = int(guessed_state_data["x"])
            y_cor = int(guessed_state_data["y"])
            
            #send turtle to the location of the correct state
            correct_answer.goto(x_cor, y_cor)
            #write the state name
            correct_answer.write(f"{guessed_state}", align="center",font= FONT)
            #add one to the correct guesses counter
            correct_guesses += 1
            
        else:
            pass


turtle.mainloop()


