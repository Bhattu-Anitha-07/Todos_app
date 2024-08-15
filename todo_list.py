from tkinter import*
import tkinter as tk
from tkinter import messagebox

root = Tk()
root.title("Todo List")
root.config(bg="lightblue") 
root.geometry('600x480+400+100')
root.resizable(width=False,height=False)

frame=Frame(root,bg="lightblue")
frame.pack()

todo = Label(frame,text = "Todos",bg="lightblue",font = ("Helvetica 26 bold"))
create_task = Label(frame,text = "Create Task",bg="lightblue",font = ("Helvetica 20 bold"))
my_tasks = Label(frame,text = "My Tasks",bg="lightblue",font = ("Helvetica 20 bold"))


todo.pack(side=TOP,padx=10,pady=15)
create_task.pack(pady=10)


entry = Entry(frame,font='times 14',bg='white',bd=5,width=30,fg='black')
entry.pack(pady=5)

def newTask():
    task = entry.get()
    if task != "":
        var=IntVar()
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


addTask_btn = Button(frame,text='  Add  ',font=('times 14'),bg='#4c63b6',fg='white',command=newTask) 
addTask_btn.pack(padx=3,pady=3)

def deleteTask():
    lb.delete(ANCHOR)

delTask_btn = Button(frame,text=' Delete ',font=('times 14'),bg='red',fg='white',command=deleteTask)
delTask_btn.pack(padx=3,pady=3)

my_tasks.pack(pady=1)

lb = Listbox(frame,width=50,bd=2,height=6,selectmode='SINGLE',bg='lightblue',fg='black',font=('Times', 16))
lb.pack(side=LEFT,fill=BOTH)

sb=Scrollbar(frame)    
sb.pack(side=RIGHT,fill='both')
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)


task_list = ['learn python','learn html','create a calci','take a nap','complete project','learn algorithms']
for task in task_list:
    lb.insert(END,task)

root.mainloop()