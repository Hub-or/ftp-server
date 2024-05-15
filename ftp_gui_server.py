import os
import re
import sys
import psutil
import socket
import tkinter as tk

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from threading import Thread


class LocateProgramAndFiles:
    def get_router_ip(self):
        route_info = os.popen("route print -4").read()
        pattern = re.compile(r"0\.0\.0\.0\s+0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)")
        match = pattern.search(route_info)
        if match:
            return match.group(1)
        else:
            return None
        
    def get_access_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            s.connect(('8.8.8.8', 1))
            ip_addr = str(s.getsockname()[0])
        except Exception:
            ip_addr = None
        finally:
            s.close()
        return ip_addr
        
    def get_avbl_port(self, start=0, end=65536):
        used_ports = {conn.laddr.port for conn in psutil.net_connections()}
        free_ports = [port for port in range(start, end) if port not in used_ports]
        command_port = 21
        while True:
            if command_port in free_ports:
                return command_port
            else:
                command_port += 2
        
    def get_location(self):
        ip_addr = self.get_access_ip()
        if ip_addr is None:
            print("WLAN disconnected.")
            sys.exit()
        return [self.get_access_ip(), str(self.get_avbl_port())]
        

class SimpleFTPServer:
    def __init__(self, host="127.0.0.1", port=21, user="user", password="12345", directory='.'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.directory = directory

    def start(self):
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.user, self.password, self.directory, perm='elradfmw')
        handler = FTPHandler
        handler.passive_ports = range(60000, 65535)
        handler.masquerade_address = self.host
        handler.authorizer = authorizer
        self.server = FTPServer(('0.0.0.0', self.port), handler)
        self.server.serve_forever()

    def stop(self):
        if self.server:
            self.server.close_all()
        

class FTPServerGUI:
    def __init__(self, root, server_build_info: list):
        self.server = None
        self.root = root
        self.root.title("FTP Server")

        self.host_label = tk.Label(root, text="Host:")
        self.host_label.pack()
        self.host_entry = tk.Entry(root)
        self.host_entry.insert(0, server_build_info[0])
        self.host_entry.pack()

        self.port_label = tk.Label(root, text="Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.insert(0, server_build_info[1])
        self.port_entry.pack()

        self.user_label = tk.Label(root, text="Username:")
        self.user_label.pack()
        self.user_entry = tk.Entry(root)
        self.user_entry.insert(0, "user")
        self.user_entry.pack()

        self.pass_label = tk.Label(root, text="Password:")
        self.pass_label.pack()
        self.pass_entry = tk.Entry(root)
        self.pass_entry.insert(0, "12345")
        self.pass_entry.pack()

        self.dir_label = tk.Label(root, text="Directory:")
        self.dir_label.pack()
        self.dir_entry = tk.Entry(root)
        self.dir_entry.insert(0, server_build_info[2])
        self.dir_entry.pack()

        self.start_button = tk.Button(root, text="Start Server", command=self.start_server)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack()

    def start_server(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        user = self.user_entry.get()
        password = self.pass_entry.get()
        directory = self.dir_entry.get()

        self.server = SimpleFTPServer(host, port, user, password, directory)
        self.server_thread = Thread(target=self.server.start)
        self.server_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_server(self):
        if self.server:
            self.server.stop()
            self.server_thread.join()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)


def main(location):
    root = tk.Tk()
    app = FTPServerGUI(root, location)
    root.mainloop()


if __name__ == "__main__":
    path_of_current_folder = os.getcwd()
    if not (path_of_current_folder.endswith('/') or \
        path_of_current_folder.endswith('\\')):
        path_of_file_storage_folder = path_of_current_folder + '/Files'
    else:
        path_of_file_storage_folder = path_of_current_folder + 'Files'
    os.makedirs(path_of_file_storage_folder, exist_ok=True)
    
    locate_in_internet_and_files = LocateProgramAndFiles()
    my_location = locate_in_internet_and_files.get_location()
    my_location.append(path_of_file_storage_folder)
    
    main(my_location)
    
