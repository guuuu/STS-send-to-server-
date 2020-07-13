import shutil
import os
import sys

__author__ = "Gustavo Nascimento"

server_path = "F:\\xampp\\htdocs\\Python Share"

def clear(): return os.system('cls')

def menu():
    print("How you want to choose the path:")
    print("1 - Text")
    print("2 - GUI")
    print("0 - Quit")

    while True:
        try:
            op = int(input("=>"))

            if isinstance(op, int):
                if op == 1:
                    text()
                elif op == 2:
                    gui()
                elif op == 0:
                    sys.exit(0)
                else:
                    continue
        except Exception as ex:
            pass

def text():
    clear()

    try:
        while True:
            path = str(input("Where is the file => "))

            if os.path.exists(path):
                break
            else:
                continue
        shutil.copy(path, server_path) 
        os.startfile(server_path)
        sys.exit(0)
    except Exception as ex:
        pass

def gui():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(initialdir=os.getcwd())

    try:
        while True:
            if os.path.exists(path):                
                break
            else:
                continue
        shutil.copy(path, server_path)
        os.startfile(server_path)
        sys.exit(0)
    except Exception as ex:
        pass
menu()