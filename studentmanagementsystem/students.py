from tkinter import *
from tkinter import ttk
import psycopg2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Students Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)
