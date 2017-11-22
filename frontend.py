from tkinter import *
import backend as bd



def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        print(selected_tuple)
        title_e.delete(0,END)
        title_e.insert(END, selected_tuple[1])
        author_e.delete(0,END)
        author_e.insert(END, selected_tuple[2])
        year_e.delete(0,END)
        year_e.insert(END, selected_tuple[3])
        ISBN_e.delete(0,END)
        ISBN_e.insert(END, selected_tuple[4])
    except IndexError:
        pass
def view_command():
    list1.delete(0,END)
    for books in bd.view():
        list1.insert(END, books)

def search_command():
    list1.delete(0,END)
    for search in bd.search(title_e_value.get(), author_e_value.get(), year_e_value.get(), ISBN_e_value.get()):
        list1.insert(END, search)

def insert_command():
    bd.insert(title_e_value.get(), author_e_value.get(), year_e_value.get(), ISBN_e_value.get())
    list1.delete(0,END)
    list1.insert(END, (title_e_value.get(), author_e_value.get(), year_e_value.get(), ISBN_e_value.get()))

def delete_command():
    bd.delete(selected_tuple[0])

def update_command():
    bd.update(selected_tuple[0],title_e_value.get(), author_e_value.get(), year_e_value.get(), ISBN_e_value.get())

def quit_command():
    quit()



window = Tk()

window.wm_title("Book Store")

#Section 1 == GUI front_end
#All tkinter.Label functions are below
title_l = Label(window, text="Title")
title_l.grid(row=0, column=0)

author_l = Label(window, text="Author")
author_l.grid(row=0, column=2)

year_l = Label(window, text="Year")
year_l.grid(row=1, column=0)

ISBN_l = Label(window, text="ISBN")
ISBN_l.grid(row=1, column=2)

#All tkinter.Entry functions are below
title_e_value = StringVar()
title_e = Entry(window, textvariable=title_e_value)
title_e.grid(row=0, column=1)

author_e_value = StringVar()
author_e = Entry(window, textvariable=author_e_value)
author_e.grid(row=0, column=3)

year_e_value = StringVar()
year_e = Entry(window, textvariable=year_e_value)
year_e.grid(row=1, column=1)

ISBN_e_value = StringVar()
ISBN_e = Entry(window, textvariable=ISBN_e_value)
ISBN_e.grid(row=1, column=3)

#All tkinter.Button functions are below
view_all = Button(window,text="View all", width=12, command=view_command)
view_all.grid(row=2, column=3)

view_all = Button(window,text="Search entry", width=12, command=search_command)
view_all.grid(row=3, column=3)

view_all = Button(window,text="Add entry", width=12, command=insert_command)
view_all.grid(row=4, column=3)

view_all = Button(window,text="Update selected", width=12, command=update_command)
view_all.grid(row=5, column=3)

view_all = Button(window,text="Delete selected", width=12, command=delete_command)
view_all.grid(row=6, column=3)

view_all = Button(window,text="Close", width=12, command=window.destroy)
view_all.grid(row=7, column=3)

#all tkinter.Text functions are below
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#all tkinter.Scrollbar functions are below
scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6, columnspan=None)

list1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()
#End of Section 1
