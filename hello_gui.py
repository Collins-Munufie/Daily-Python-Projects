import tkinter as tk

window = tk.Tk()  #initialize the main window
window.title("my GUI app")  #Title of the window
window.geometry("300x200")  #Size of the window

Label = tk.Label(window, text = "click the button below")

# Step 3: Define a function that updates the label
def say_hello():
    Label.config(text="Hello, World!")

# Step 4: Create a button that calls the say_hello function when clicked
button = tk.Button(window, text="Click Me", command=say_hello) 

# Step 5: Pack the label and button into the window
Label.pack(pady=10)  # Add some vertical padding
button.pack(pady=10)  # Add some vertical padding

window.mainloop
