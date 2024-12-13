from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from DB import get_by_id, update_user

name =''
email = ''
phone_number = ''
user_id = 0
intake_no = 0
major = ''
academic_year = 0
payment_status = ''

def update_student(update):
    response = messagebox.askyesno("Confirmation", "Are you sure you want to update user?")
    if response:
        global name, email, user_id, phone_number, email, major, intake_no, academic_year, payment_status
        if name.get() == '' or phone_number.get() == '' or email.get() == '' or major.get() == '' or intake_no.get() == '' or academic_year.get() == '' or payment_status.get() == '':
            messagebox.showerror('Missing data', "Fill all slots !")
            update.deiconify()
            update.lift()  # Bring the window to the front
            update.focus_force()

        else :
            user_data = [int(user_id.get()), name.get(), phone_number.get(), email.get(), major.get(),
                         int(intake_no.get()),
                         int(academic_year.get()), payment_status.get()]
            update_user(user_data)
            messagebox.showinfo('Done',"user updated successfully !!")
            update.destroy()
            return 0

    else:
        update.deiconify()
        update.lift()  # Bring the window to the front
        update.focus_force()


def display_update(root,__user_id__):
    if __user_id__ == 0:
        messagebox.showerror("Select user","Select a user first !")
        return 0
    global name,email,phone_number,user_id,intake_no,major,academic_year,payment_status
    old_user_data=get_by_id(__user_id__)

    update =Toplevel(root)
    update.title("Update Student")
    update.resizable(False,False)
    update.geometry("1000x550+400+80")
    Label(update,bg="#eed055",height=1,text = "Student Details",font="arial 18",anchor="center",fg="#06275c").place(relwidth = 1)
    update.config(bg="#06275c")
    Label(update,text = f"Name : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=120)
    Label(update,text = f"Email : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=160)
    Label(update,text = f"Phone Number : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=200)
    Label(update,text = f"ID : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=240)
    Label(update,text = f"intake No. : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=280)
    Label(update,text = f"Major : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=320)
    Label(update,text = f"Academic year : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=360)
    Label(update,text = f"Payment Status : ",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=400)
    name =StringVar()
    email = StringVar()
    phone_number = StringVar()
    user_id = StringVar()
    intake_no = StringVar()
    major = StringVar()
    academic_year = StringVar()
    payment_status = StringVar()
    name.set(old_user_data[1])
    email.set(old_user_data[3])
    phone_number.set(old_user_data[2])
    user_id.set(old_user_data[0])
    intake_no.set(old_user_data[5])
    major.set(old_user_data[4])
    academic_year.set(old_user_data[6])
    payment_status.set(old_user_data[7])

    entry_name = Entry(update,font ="arial 14",textvariable=name)
    entry_email = Entry(update,font ="arial 14",textvariable=email)
    entry_phone_number = Entry(update,font ="arial 14",textvariable=phone_number)
    entry_id = Entry(update,font ="arial 14",textvariable=user_id, state = 'readonly')
    entry_intake_no = Entry(update,font ="arial 14",textvariable=intake_no)
    entry_major = Combobox(update,font ="arial 14",values = ['Electrical Engineering','Mechanical Engineering','Civil Engineering','AI','Front-End','Back-End','Computer Science'],textvariable=major)
    entry_academic_year = Combobox(update,font ="arial 14",values=['1','2','3','4','5'],textvariable=academic_year)
    list_payment_status = Combobox(update, font ="arial 14",values=['paid','waiting','not set'],width=14,textvariable=payment_status)
    entry_name.place(x=180, y=120)
    entry_email.place(x=180, y=160)
    entry_phone_number.place(x=180,y=200)
    entry_id.place(x=180, y=240)
    entry_intake_no.place(x=180,y=280)
    entry_major.place(x=180, y=320)
    entry_academic_year.place(x=180, y=360)
    list_payment_status.place(x=180, y=400)

    Button(update, text="Close",font = "Arial 25",height=1,command=lambda:update.destroy(),bg = "#eed055").place(relx =0.4,y=480,anchor ="center")
    Button(update, text="Update",font = "Arial 25",height=1,command=lambda:update_student(update),bg = "#eed055").place(relx =0.6,y=480,anchor="center")

    update.mainloop()
