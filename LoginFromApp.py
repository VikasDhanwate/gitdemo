import tkinter as tk
from tkinter import messagebox

# Hardcoded valid credentials for demonstration
VALID_USERNAME = "user1234"
VALID_PASSWORD = "password1234"

def handle_login():
    """
    Checks the entered username and password against valid credentials.
    """
    username = entry_username.get()
    password = entry_password.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # Success message box
        messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful.")
        # Optional: Close the window after successful login
        root.destroy() 
    else:
        # Failure message box
        messagebox.showerror("Login Failed", "Invalid username or password.")
        # Clear the password field for security/usability
        entry_password.delete(0, tk.END)

# --- Set up the main application window ---
root = tk.Tk()
root.title("Simple Login Form")
root.geometry("300x200") # Set the window size (width x height)

# Center the widgets using padding
padding_options = {'padx': 10, 'pady': 5}

# --- Create and Place Widgets ---

# 1. Username Label and Entry Field
label_username = tk.Label(root, text="Username:")
label_username.pack(**padding_options)

entry_username = tk.Entry(root, width=25)
entry_username.pack(**padding_options)
entry_username.focus_set() # Puts the cursor here when the app starts

# 2. Password Label and Entry Field
label_password = tk.Label(root, text="Password:")
label_password.pack(**padding_options)

# The 'show="*"' option masks the password input
entry_password = tk.Entry(root, width=25, show="*")
entry_password.pack(**padding_options)

# 3. Login Button
# The 'command=handle_login' links the button click to our function
login_button = tk.Button(root, text="Login", command=handle_login, width=10)
login_button.pack(**padding_options)

# --- Start the Tkinter event loop ---
# This line keeps the window open and listens for user interactions
if __name__ == "__main__":
    root.mainloop()