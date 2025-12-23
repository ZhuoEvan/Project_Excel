# ================================= #
# Description                       #
# File Name: main.py                #
# ==================================#

# ================================= #
# Module Import                     #
# ================================= #
# Python Modules ------------------ #


# Python Library ------------------ #
import tkinter as tk
import pandas as pd


# ================================= #
# Tkinter Construct                 #
# ================================= #
#Initialize Application
def main(master):
    #Initial Settings
    root.title("Project Excel")
    root.geometry("1440x900")

    #Build Main Menu
    WIN.MainWindow(master)

    #Start Application
    root.mainloop()
    
#Build Application
if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    

#Application Ideas