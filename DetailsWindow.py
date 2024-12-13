from tkinter import *
from DB import get_data
from tkinter import messagebox

def display_details(user_id,root):
    if user_id == 0:
        messagebox.showerror("Select user","Select a user first !")
        return 0
    user_data = get_data(f'SELECT * FROM students WHERE id = {user_id}')
    details =Toplevel(root)
    details.title("Student details")
    details.resizable(False,False)
    details.geometry("1000x550+400+80")
    Label(details,bg="#eed055",height=1,text = "Student Details",font="arial 18",anchor="center",fg="#06275c").place(relwidth = 1)
    details.config(bg="#06275c")
    Label(details,text = f"Name : {user_data[0][1]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=120)
    Label(details,text = f"Email : {user_data[0][3]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=160)
    Label(details,text = f"Phone Number : {user_data[0][2]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=200)
    Label(details,text = f"ID : {user_data[0][0]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=240)
    Label(details,text = f"intake No. : {user_data[0][5]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=280)
    Label(details,text = f"Major : {user_data[0][4]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=320)
    Label(details,text = f"Academic year : {user_data[0][6]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=360)
    Label(details,text = f"Payment Status : {user_data[0][7]}",bg="#06275c",fg='white',font="arial 14").place(x = 5,y=400)
    Button(details, text="Close",font = "Arial 25",height=1,command=lambda:details.destroy(),bg = "#eed055").place(relx =0.5,y=450,anchor="center")
    details.mainloop()
