# Goal Based Agent (University Scenario)

# current state
state = "Home"

# taking input from user
goal = input("Enter your goal location (University / Cafe / Park): ")

# possible actions
actions = ["go_to_university", "go_to_cafe", "go_to_park"]

# function to predict result of action
def predict(state, action):

    if state == "Home" and action == "go_to_university":
        return "University"

    elif state == "Home" and action == "go_to_cafe":
        return "Cafe"

    elif state == "Home" and action == "go_to_park":
        return "Park"

    return state


goal_found = False

# agent decision making
for action in actions:

    new_state = predict(state, action)

    print("\nTrying action:", action)
    print("Resulting state:", new_state)

    if new_state.lower() == goal.lower():
        print("Action selected:", action)
        print("Goal Achieved!")
        goal_found = True
        break


if goal_found == False:
    print("Goal cannot be achieved with available actions.")