from contextlib import nullcontext
from tkinter import *
from tkinter import ttk
from DB import *
from datetime import datetime
from PIL import Image, ImageTk
from DetailsWindow import display_details
from CreateWindow import display_create
from UpdateWindow import display_update
from tkinter import messagebox

def on_key_press(event):
    if event.keysym == "Escape":
        root.destroy()
        print("Page Closed")
    else:
        print(event.keysym)

def update_time():
    label_date.config(text =f"{datetime.now().strftime("%Y-%m-%d")}")
    label_time.config(text =f"{datetime.now().strftime("%I:%M:%S %p")}")
    root.after(1000, update_time)

search_item = "name"  #--important variable--
table_object_Selected = 0 #--important variable--

search_entry_placeholder = f"Enter {search_item}"
def search_entry_on_focus_in(event):
    if search_entry.get() == search_entry_placeholder:
        search_entry.delete(0, END)  # Clear the placeholder when the entry gets focus
def search_entry_on_mouse_enter(event):
    if search_entry.get() == search_entry_placeholder:
        search_entry.delete(0, END)  # Clear the placeholder when the entry gets focus
def search_entry_on_mouse_leave(event):
    if search_entry.get() == "":
        search_entry.insert(0, search_entry_placeholder)  # Reinsert the placeholder text when focus is lost
def search_entry_on_key_press(event):
    if search_entry.get() == search_entry_placeholder:
        search_entry.delete(0, END)  # Clear the placeholder when the entry gets focus
def on_item_click(event):
    table_region = table.identify_region(event.x, event.y)
    if table_region == "cell":
        global table_object_Selected
        # Get the item row number
        item_id = table.identify_row(event.y)
        table_object_Selected = table.item(item_id)['values'][1]
#variable to choose what we will search for
def search_item_buttons_handler(option):
    global search_item
    global search_entry_placeholder
    search_item = option
    search_entry.delete(0, END)  # Clear the placeholder when the entry gets focus
    search_entry_placeholder = f"Enter {search_item}"
    search_entry.insert(0, search_entry_placeholder)
    entry_search_name.config(bg="lightblue" if option == "name" else "SystemButtonFace")
    entry_search_phone.config(bg="lightblue" if option == "phone number" else "SystemButtonFace")
    entry_search_intake.config(bg="lightblue" if option == "intake" else "SystemButtonFace")
    entry_search_id.config(bg="lightblue" if option == "id" else "SystemButtonFace")

def update_table():
    for item in table.get_children():
        table.delete(item)
    data = get_data('SELECT ID, Name, Phone_Number, "Intake_No" FROM students')
    numbered_data = [(i + 1, *row) for i, row in enumerate(data)]
    for i in numbered_data:
        table.insert("", END, values=i)

def delete_user():
    #global table_object_Selected
    user_data = get_by_id(table_object_Selected)
    response = messagebox.askyesno("Confirmation", f"Are you sure you want to delete user :{user_data[1]}?")
    if response:
        delete_by_id(table_object_Selected)
        messagebox.showinfo('Done',"user deleted successfully !!")
    else:
        pass

root = Tk()
root.title("Home")
root.geometry("1536x864+0+0")
root.bind('<KeyPress>', on_key_press)
root.state("zoomed")
root.config(bg="#06275c")


######################  Date & Time    ######################
Label(root,bg="#eed055",width =1536,height=3).place(x = 0, y = 0)
label_date = Label(root,bg = "#eed055" , font = "Arial 15")
label_date.place(x = 5,y = 12)
label_time = Label(root,bg = "#eed055" , font = "Arial 15")
label_time.place(x = 1411,y = 12)
update_time()
#############################################################



######################  Search Button & handling its events    ######################
search_entry = Entry(root,width = 50,font = "arial 15")
search_entry.place(relx=0.5, y = 80 ,anchor='center')
# Bind events to handle the focus in and out behavior
search_entry.bind("<FocusIn>", search_entry_on_focus_in)
search_entry.bind("<Key>", search_entry_on_key_press)
search_entry.bind("<Enter>", search_entry_on_mouse_enter)
search_entry.bind("<Leave>", search_entry_on_mouse_leave)

search_entry.insert(0, search_entry_placeholder)
######################################################################################


######################  Search Buttons    ######################
Label(root,text = "Search By:",bg ="#06275c",font ="arial 8",fg ="white").place(x = 491,y=100)
entry_search_name = Button(root, text="Name",font = "Arial 8",height=1,command=lambda:search_item_buttons_handler("name"))
entry_search_phone = Button(root, text="Phone Number",command=lambda:search_item_buttons_handler("phone number"))
entry_search_intake = Button(root, text="Intake", command=lambda:search_item_buttons_handler("intake"))
entry_search_id = Button(root, text="ID", command=lambda:search_item_buttons_handler("id"))

entry_search_name.place(x = 561,y = 100)
entry_search_phone.place(x = 607,y = 100)
entry_search_intake.place(x = 709,y = 100)
entry_search_id.place(x = 762,y = 100)
################################################################


######################  Table Components    ######################
table = ttk.Treeview(root, columns=("S","ID", "Name", "Phone_Number", "Intake_No."), show="headings")
table.heading("S",text="S")
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Phone_Number", text="Phone Number")
table.heading("Intake_No.", text="Intake No.")
table.column("S",width=100)
table.column("ID", width=100)
table.column("Name", width=250)
table.column("Phone_Number", width=200)
table.column("Intake_No.", width=150)
table.place(relx = 0.5, y = 400,anchor='center')

style = ttk.Style()
style.configure(
    "Treeview",
    background="#eed055",  # Row background color
    foreground="#06275c",    # Text color
    rowheight=35,          # Row height
    fieldbackground="#e6f7ff",  # Background color of the entire table
    font=("Arial", 12),    # Font for rows
)
table.bind("<ButtonRelease-1>", on_item_click) #to return the user number selected
########################################################################################


######################  CRUD operations buttons    ######################
button_create = Button(text = "Create",font="arial 30",fg="#06275c",bg="#eed055",command =lambda: display_create(root))
button_Details = Button(text = "Details",font="arial 30",fg="#06275c",bg="#eed055",command=lambda: display_details(table_object_Selected,root))
button_Update = Button(text = "Update",font="arial 30",fg="#06275c",bg="#eed055",command= lambda:display_update(root,table_object_Selected))
button_Delete = Button(text = "Delete",font="arial 30",fg="#06275c",bg="#eed055",command = delete_user)
button_create.place(x=450,y=680,anchor = "center")
button_Details.place(x=662,y=680,anchor = "center")
button_Update.place(x=874,y=680,anchor = "center")
button_Delete.place(x=1086,y=680,anchor = "center")
#########################################################################



######################  Reload Table Button    ######################
reload_icon = ImageTk.PhotoImage(Image.open("Images/reload.png").resize((50,50)))
button_reload = Button(text = "Reload",font="arial 30",fg="#06275c",bg="#eed055",image = str(reload_icon),command =update_table)
button_reload.place(x=1180,y=210)
#######################################################################


######################  Load DataBase Data    ######################
update_table()
####################################################################



root.mainloop()
root.resizable(False, False)