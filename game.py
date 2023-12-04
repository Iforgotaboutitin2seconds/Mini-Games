import tkinter as tk

# Function to display character based on selection
def display_character(character):
    label.config(text=f"You selected {character}!")

# Create a new window
window = tk.Tk()

# Set the window size and position
window.geometry("300x200")
window.eval('tk::PlaceWindow . center')

# Create a label widget with the text
label = tk.Label(window, text="Hello, World!")
label.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Create the play button
play_button = tk.Button(button_frame, text="Play", command=lambda: display_character("Play"))
play_button.pack(side=tk.LEFT)

# Create the settings button
settings_button = tk.Button(button_frame, text="Settings", command=lambda: display_character("Settings"))
settings_button.pack(side=tk.LEFT)

# Create the exit button
exit_button = tk.Button(button_frame, text="Exit", command=window.quit)
exit_button.pack(side=tk.LEFT)

# Start the main event loop
window.mainloop()
