from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

def search_command():
    list1.delete(0,END)
    for row in backend.search(word_text.get()):
        list1.insert(END,row)

window=Tk()

window.wm_title("Interactive Dictionary")

l1=Label(window,text="Enter the Word to search")
l1.grid(row=0,column=0)

word_text=StringVar()
e1=Entry(window,textvariable=word_text)
e1.grid(row=0,column=1)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=1,column=1)

list1=Listbox(window, height=6,width=150)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
