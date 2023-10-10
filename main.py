import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Function to send a message to the server
def send_message():
    message = entry.get()
    if message:
        full_message = f"{username}: {message}"  # Include the username
        client.send(full_message.encode('utf-8'))
        entry.delete(0, tk.END)

# Function to display a message received in the text area
def display_message(message):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, message + '\n')
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

# Function to handle receiving messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            display_message(message)
        except:
            print("Error")
            client.close()
            break

# Function to set the username
def set_username():
    global username
    username = username_entry.get()
    username_label.config(text=f"Username: {username}")
    username_entry.destroy()
    set_username_button.destroy()

# Socket configuration for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

# Interface creation using Tkinter
root = tk.Tk()
root.title("Chat Client")

chat_area = scrolledtext.ScrolledText(root, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Add functionality to set the username
username_label = tk.Label(root, text="Enter your username:")
username_label.pack(padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.pack(padx=10, pady=5)

set_username_button = tk.Button(root, text="Set Username", command=set_username)
set_username_button.pack(padx=10, pady=5)

# Start the thread to receive messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()