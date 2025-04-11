import tkinter as tk
import time

# Function to update the time
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    # Schedule the update_time function to be called again after 1000 milliseconds
    clock_label.after(1000, update_time)

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=("Arizona", 50), bg="Green", fg="Maroon")
clock_label.pack(anchor='center')

# Start the clock
update_time()

# Run the application
root.mainloop()
