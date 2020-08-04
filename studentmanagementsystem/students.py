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

        # Manage Frame===============================================================================================

        manage_frame = Frame(self.root, bd=4, relief=GROOVE, bg="white")
        manage_frame.place(x=20, y=100, height=550, width=410)

        m_title = Label(manage_frame, text="Students Profile", bg="white", fg="red",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_roll = Label(manage_frame, text="Roll No.", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_roll = Entry(manage_frame,  font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_name = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=10, sticky="w")