from tkinter import *
from tkinter.font import Font

todo = Tk()
todo.title("To-Do-List")
todo.geometry("400x700+200+20")
todo.resizable(False, False)

#font
my_font = Font(family="Times New Roman", size=16, weight="bold")

task_list = []

#Add
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
            task_list.append(task)
            listbox.insert(END, task)

#delete
def deleteTask():
    try:
        selected_task = listbox.get(ANCHOR)
        if selected_task:
            task_list.remove(selected_task)
            with open("tasklist.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(f"{task}\n")
            listbox.delete(ANCHOR)
    except:
        print("No task selected for deletion.")

#Edit Task
def editTask():
    try:
        selected_task = listbox.get(ANCHOR)
        if selected_task:
            task_entry.delete(0, END)  # Clear the entry box
            task_entry.insert(0, selected_task)  #Insert the selected task into entry
            task_list.remove(selected_task)  #Remove it temporarily from the list
            listbox.delete(ANCHOR)  # Remove it from the listbox
    except:
        print("No task selected for editing.")


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                task = task.strip()
                if task:
                    task_list.append(task)
                    listbox.insert(END, task)
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            pass

#Icon
todo.iconphoto(False, PhotoImage(file="img/task.png"))

#Top bar
TopImage = PhotoImage(file="img/topbar.png")
Label(todo, image=TopImage).pack()

heading = Label(todo, text="To-Do List", font="Helvetica 25 bold", fg="white", bg="#283747")
heading.place(x=110, y=20)


frame = Frame(todo, width=400, height=50, bg="light blue")
frame.place(x=0, y=180)

task_entry = Entry(frame, width=18, font="arial 20", bd=0, fg="#283747", highlightthickness=2, highlightbackground="#5a95ff")
task_entry.place(x=10, y=7)
task_entry.focus()

add_button = Button(frame, text="ADD", font="arial 12 bold", width=7, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

#listbox
frame1 = Frame(todo, bd=3, width=700, height=280, bg="#283747")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 14), width=40, height=16, bg="#34495e", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Buttons
button_frame = Frame(todo, bg="#283747")
button_frame.pack(pady=10)

delete_button = Button(button_frame, text="DELETE", font="arial 12 bold", width=10, bg="#e74c3c", fg="#fff", command=deleteTask)
delete_button.grid(row=0, column=0, padx=10)

edit_button = Button(button_frame, text="EDIT", font="arial 12 bold", width=10, bg="#f1c40f", fg="#fff", command=editTask)
edit_button.grid(row=0, column=1, padx=10)

openTaskFile()

todo.mainloop()