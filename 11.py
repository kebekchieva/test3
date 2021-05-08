state = ["California", "Washington", "Florida", "Arkansas", "New York"]
generator = (element for i in state)

print(state)

# генератор может быть итератором, а итератор генератором не может быть.
