import subprocess
import tkinter as tk
from subprocess import CREATE_NEW_CONSOLE, Popen
import os
import signal




process = None


class ServerManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()
    process = None
    def initUI(self):
        global max_players_field
        global port_field
        global passwd_field
        global status_label
        global red_box
        global green_box
        # Create buttons to execute, stop, and restart the executable file
        execute_btn = tk.Button(self, text='Execute', command=self.execute)
        stop_btn = tk.Button(self, text='Stop', command=self.stop)
        restart_btn = tk.Button(self, text='Restart', command=self.restart)
        max_players_label = tk.Label(text="Max Players:")
        max_players_label.pack()
        max_players_field = tk.Entry()
        max_players_field.pack()

        port_label = tk.Label(text="Port:")
        port_label.pack()
        port_field = tk.Entry()
        port_field.pack()
        passwd_label = tk.Label(text="Password:")
        passwd_label.pack()
        passwd_field = tk.Entry()
        passwd_field.pack()
        red_box = tk.Label(bg="red", width=4, height=2)
        red_box.pack_forget()
        green_box = tk.Label(bg="green", width=4, height=2)
        green_box.pack_forget()
        # Create a text label to display the status of the server
        status_label = tk.Label(text="Server inactive")
        status_label.pack(side="left")




        # Set up the layout
        execute_btn.pack(side='top', fill='x')
        stop_btn.pack(side='top', fill='x')
        restart_btn.pack(side='top', fill='x')
    process = None
    def execute(self):
        print("su2")
        max_players = max_players_field.get()
        port = port_field.get()
        passwd = passwd_field.get()
        global process
        global pid
    # Replace "path/to/executable" with the actual path to the executable file
        process = subprocess.Popen(f'AMP_Server.exe {port} {max_players} {passwd}',  creationflags=CREATE_NEW_CONSOLE)
        status_label.config(text="Server active")
        red_box.pack_forget()
        green_box.pack(side="right")

        

    


    def stop(self):
        global process
        global pid
        print("su1")
        # Terminate the subprocess
        os.kill((process.pid), signal.SIGTERM)
        status_label.config(text="Server inactive")
        green_box.pack_forget()
        red_box.pack(side="right")


    def restart(self):
        print("su3")
        # Restart the executable by stopping it and then starting it again
        self.stop()
        self.execute()


if __name__ == '__main__':
    server_manager = ServerManager()
    server_manager.mainloop()
