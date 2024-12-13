from tkinter import *
from tkinter.ttk import Combobox
from DB import is_id_valid
from tkinter import messagebox
from DB import add_user
name =''
email = ''
phone_number = ''
user_id = 0
intake_no = 0
major = ''
academic_year = 0
payment_status = ''

def create_student(create):
    response = messagebox.askyesno("Confirmation", "Are you sure you want to create user?")
    if response:
        global name, email, user_id, phone_number, email, major, intake_no, academic_year, payment_status
        if(user_id.get() == ''or name.get() =='' or phone_number.get() =='' or email.get() =='' or major.get() =='' or intake_no.get() =='' or academic_year.get() =='' or payment_status.get() ==''):
            messagebox.showerror('Missing data', "Fill all slots !")
            create.deiconify()
            create.lift()  # Bring the window to the front
            create.focus_force()
        elif is_id_valid(user_id.get()) == 1:
            messagebox.showerror('Duplicated Id', "ID already taken !")
            create.deiconify()
            create.lift()  # Bring the window to the front
            create.focus_force()

        else :
            user_data = [int(user_id.get()), name.get(), phone_number.get(), email.get(), major.get(), int(intake_no.get()),int(academic_year.get()), payment_status.get()]
            add_user(user_data)
            messagebox.showinfo('Done',"user created successfully !!")

    else:
        create.deiconify()
        create.lift()  # Bring the window to the front
        create.focus_force()


def display_create(root):
    global name,email,phone_number,user_id,intake_no,major,academic_year,payment_status
    create =Toplevel(root)
    create.title("Add Student")
    create.resizable(False,False)
    create.geometry("1000x550+400+80")
    Label(create,bg="#eed055",height=1,text = "Student Details",font="arial 18",anchor="center",fg="#06275c").place(relwidth = 1)
    create.config(bg="#06275c")
    Label(create,text = f"Name : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=120)
    Label(create,text = f"Email : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=160)
    Label(create,text = f"Phone Number : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=200)
    Label(create,text = f"ID : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=240)
    Label(create,text = f"intake No. : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=280)
    Label(create,text = f"Major : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=320)
    Label(create,text = f"Academic year : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=360)
    Label(create,text = f"Payment Status : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=400)
    name =StringVar()
    email = StringVar()
    phone_number = StringVar()
    user_id = StringVar()
    intake_no = StringVar()
    major = StringVar()
    academic_year = StringVar()
    payment_status = StringVar()





    entry_name = Entry(create,font ="arial 14",textvariable=name)
    entry_email = Entry(create,font ="arial 14",textvariable=email)
    entry_phone_number = Entry(create,font ="arial 14",textvariable=phone_number)
    entry_id = Entry(create,font ="arial 14",textvariable=user_id)
    entry_intake_no = Entry(create,font ="arial 14",textvariable=intake_no)
    entry_major = Combobox(create,font ="arial 14",values = ['Electrical Engineering','Mechanical Engineering','Civil Engineering','AI','Front-End','Back-End','Computer Science'],textvariable=major)
    entry_academic_year = Combobox(create,font ="arial 14",values=['1','2','3','4','5'],textvariable=academic_year)
    list_payment_status = Combobox(create, font ="arial 14",values=['paid','waiting','not set'],width=14,textvariable=payment_status)
    entry_name.place(x=180, y=120)
    entry_email.place(x=180, y=160)
    entry_phone_number.place(x=180,y=200)
    entry_id.place(x=180, y=240)
    entry_intake_no.place(x=180,y=280)
    entry_major.place(x=180, y=320)
    entry_academic_year.place(x=180, y=360)
    list_payment_status.place(x=180, y=400)

    Button(create, text="Close",font = "Arial 25",height=1,command=lambda:create.destroy(),bg = "#eed055").place(relx =0.4,y=480,anchor ="center")
    Button(create, text="ADD",font = "Arial 25",height=1,command=lambda :create_student(create),bg = "#eed055").place(relx =0.6,y=480,anchor="center")

    create.mainloop()