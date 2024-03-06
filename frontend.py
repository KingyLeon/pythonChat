from tkinter import *
import tkinter as tk
import socket
import subprocess


class Client:
    def __init__(self):
        self.socket_server = socket.socket()
        self.server_host = socket.gethostname()
        self.ip = socket.gethostbyname(self.server_host)
        self.sport = 8080

        print("This is your IP address:", self.ip)
        self.server_host = input("Enter Friend's IP address:")
        self.name = input('Enter Your name')
        self.socket_server.connect((self.server_host, self.sport))

        self.socket_server.send(self.name.encode())
        server_name = self.socket_server.recv(1024)
        self.server_name = server_name.decode()

        print(self.server_name, ' has joined...')

    def send_message(self, message):
        self.socket_server.send(message.encode())

    def receive_message(self):
        return self.socket_server.recv(1024).decode()


class ChatGUI:
    def submit(self):
        message = self.textEnter.get()
        Client.message = message
        Client.socket_server.send(Client.message.encode())

    def __init__(self, window):
        self.window = window
        self.textBox = tk.Text(window, bd=20)
        self.textBox.grid(row=0, column=1)
        self.textBox.config(state=tk.DISABLED)

        self.textEnter = Entry(window, text="Message", bd=5)
        self.textEnter.grid(row=1, column=2)

        self.send_button = tk.Button(window, text="Send", command=self.submit)
        self.send_button.grid(row=2, column=2)

        window.title('Chatroom')
        window.geometry("300x200+10+10")

        # Schedule the refresh function to be called every 1 second
        self.schedule_refresh()

    def refresh(self):
        try:
            with open('History.txt', 'r') as file:
                content = file.read()
                self.textBox.config(state=tk.NORMAL)
                self.textBox.delete("1.0", tk.END)  # Clear the Textbox
                self.textBox.insert(tk.END, content)  # Insert file text
                self.textBox.config(state=tk.DISABLED)
        except FileNotFoundError:
            print("History.txt not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Refresh function to be called after 1 second
        self.schedule_refresh()

    def schedule_refresh(self):
        self.window.after(1000, self.refresh)

if __name__ == "__main__":
    root = Tk()
    chat_app = ChatGUI(root)
    root.mainloop()