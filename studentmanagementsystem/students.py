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

        # Variable==================================================================================================

        self.rollno_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Manage Frame===============================================================================================

        manage_frame = Frame(self.root, bd=4, relief=GROOVE, bg="white")
        manage_frame.place(x=20, y=100, height=550, width=410)

        m_title = Label(manage_frame, text="Students Profile", bg="white", fg="red",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_roll = Label(manage_frame, text="Roll No.", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_roll = Entry(manage_frame,textvariable=self.rollno_var,font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_name = Entry(manage_frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_email = Label(manage_frame, text="Email Id", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_email = Entry(manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var, width=19, state="readonly",
                                    font=("times new roman", 14, "bold"))
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=4, column=1, pady=5, padx=10)

        lbl_contact = Label(manage_frame, text="Contact No.", bg="white", fg="red",
                            font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        txt_contact = Entry(manage_frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        txt_dob = Entry(manage_frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        lbl_address = Label(manage_frame, text="Address", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        self.txt_address = Text(manage_frame, bd=3, relief=RIDGE, width=30, height=3, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        # Button Frame================================================================================================
        btn_frame = Frame(manage_frame, bg="white", bd=2, relief=GROOVE)
        btn_frame.place(x=0, y=490, width=430)

        addbtn = Button(btn_frame, command=self.add_student, text="Add", width=10)
        addbtn.grid(row=0, column=0, padx=10, pady=10)

        update_btn = Button(btn_frame, command=self.update, text="Update", width=10)
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        clear_btn = Button(btn_frame, command=self.clear, text="Clear", width=10)
        clear_btn.grid(row=0, column=2, padx=10, pady=10)

        delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=10)
        delete_btn.grid(row=0, column=3, padx=10, pady=10)

        # Detail Frame================================================================================================

        detail_frame = Frame(self.root, bd=4, relief=GROOVE, bg="white")
        detail_frame.place(x=450, y=100, height=550, width=800)

        lbl_search = Label(detail_frame, text="Search By", bg="white", fg="red", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(detail_frame, width=5, textvariable=self.search_by, state="readonly",
                                    font=("times new roman", 14, "bold"))
        combo_search['values'] = ("roll", "name", "contact")
        combo_search.grid(row=0, column=1, padx=10, pady=10)

        txt_search = Entry(detail_frame, bd=3, width=10, textvariable=self.search_txt, relief=RIDGE,
                           font=("times new roman", 14, "bold"))
        txt_search.grid(row=0, column=2, padx=10, pady=10)

        search_btn = Button(detail_frame, command=self.search_data, text="Search", width=10)
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        show_btn = Button(detail_frame, command=self.fetch_data, text="Show All", width=10)
        show_btn.grid(row=0, column=4, padx=10, pady=10)


        # DetailFrame====================================================================================

        table_frame = Frame(detail_frame, bg="white")
        table_frame.place(x=10, y=60, width=800, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=("roll", "name", "Email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'

        self.student_table.column("roll", width=90)
        self.student_table.column("name", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=180)

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def fetch_data(self):
        con = psycopg2.connect(host="localhost", database="student", user="postgres", password="Infinity06", port=5432)
        cur = con.cursor()
        cur.execute("select * from stm order by roll ")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def add_student(self):
        con = psycopg2.connect(host="localhost", database="student", user="postgres", password="Infinity06", port=5432)
        cur = con.cursor()
        cur.execute("insert into stm values(%s,%s,%s,%s,%s,%s,%s)", (
            self.rollno_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(), self.txt_address.get('1.0', END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def clear(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.dob_var.set("")
        self.contact_var.set("")
        self.txt_address.delete("1.0", END)

    def update(self):
        con = psycopg2.connect(host="localhost", database="student", user="postgres", password="Infinity06", port=5432)
        cur = con.cursor()
        cur.execute("update stm set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s", (
            self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(),
            self.dob_var.get(), self.txt_address.get('1.0', END), self.rollno_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        con = psycopg2.connect(host="localhost", database="student", user="postgres", password="Infinity06", port=5432)
        cur = con.cursor()
        cur.execute(
            "select * from stm where " + str(self.search_by.get()) + " LIKE '% " + str(self.search_txt.get() + " %'"))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def delete_data(self):
        con = psycopg2.connect(host="localhost", database="student", user="postgres", password="Infinity06", port=5432)
        cur = con.cursor()
        cur.execute("delete from stm where roll =%s", self.rollno_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()




root = Tk()
ob = Student(root)
root.mainloop()
