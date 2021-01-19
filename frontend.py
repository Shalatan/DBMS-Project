from backend import viewData
import backend
from tkinter import ttk
from tkinter import Toplevel, Button, Tk, Menu
from tkinter import *
from tkinter import messagebox
import datetime
from datetime import timedelta, date,datetime


def guiPy():

    "////////////////////////////////////////////////////////////////////////////////////"
    #----------------------------------CUSTOMER WINDOW---------------------------------
    "////////////////////////////////////////////////////////////////////////////////////"

    def customerWindow():

        def selectRow2(Event):
            global gVar
            index = customerList.curselection()
            gVar = customerList.get(index)
            be1.delete(0, END)
            be1.insert(END, gVar[0])
            be2.delete(0, END)
            be2.insert(END, gVar[1])
            be3.delete(0, END)
            be3.insert(END, gVar[2])

        def addCustomer():
            backend.insertCustomer(customer_id.get(),name.get(),address.get())
            customerList.delete(0,END)
            customerList.insert(END,(customer_id.get(),name.get(),address.get()))

        def viewCustomer():
            customerList.delete(0,END)
            for row in backend.viewCustomerData():
                customerList.insert(END,row)

        def deleteCustomer():
            backend.deleteCustomerData(gVar[0])
            viewCustomer()

        brawindow = Toplevel(window)

        l1 = Label(brawindow, text="Customer Id").grid(row=1,column=5)
        customer_id = StringVar()
        be1 = Entry(brawindow,textvariable=customer_id)
        be1.grid(row=1,column=6)

        l2 = Label(brawindow, text="Customer Name").grid(row=2,column=5)
        name = StringVar()
        be2 = Entry(brawindow,textvariable=name)
        be2.grid(row=2,column=6)

        l3 = Label(brawindow, text="Customer Phone").grid(row=3,column=5)
        address = StringVar()
        be3 = Entry(brawindow,textvariable=address)
        be3.grid(row=3,column=6)

        customerList = Listbox(brawindow, height=10, width=45)
        customerList.grid(row=1, column=2, rowspan=6, columnspan=2)
        customerList.bind('<<ListboxSelect>>', selectRow2)

        b1 = ttk.Button(brawindow, text="View All Customers",width=17,command=viewCustomer)
        b1.grid(row=1, column=0)
        b2 = ttk.Button(brawindow, text="Add New Customer", width=17,command=addCustomer)
        b2.grid(row=2, column=0)
        b3 = ttk.Button(brawindow, text="Delete Customer", width=17,command=deleteCustomer)
        b3.grid(row=3, column=0)
        b4 = ttk.Button(brawindow, text="Done", width=17, command=brawindow.destroy)
        b4.grid(row=4, column=0)

        brawindow.mainloop()

    "////////////////////////////////////////////////////////////////////////////////////"
    #----------------------------------ARTIST WINDOW---------------------------------
    "////////////////////////////////////////////////////////////////////////////////////"

    def artistWindow():

        def selectRow1(Event):
            global gVar1
            index = artistList.curselection()
            gVar1 = artistList.get(index)
            ee1.delete(0, END)
            ee1.insert(END, gVar1[0])
            ee2.delete(0, END)
            ee2.insert(END, gVar1[1])
            ee3.delete(0, END)
            ee3.insert(END, gVar1[2])

        def addArtist():
            backend.insertArtist(name.get(),number.get())
            artistList.delete(0,END)
            artistList.insert(END,(name.get(),number.get()))

        def viewArtist():
            artistList.delete(0,END)
            for row in backend.viewArtistData():
                artistList.insert(END,row)

        def deleteArtist():
            print(gVar1[0])
            backend.deleteArtist(gVar1[0])
            viewArtist()

        pubwindow = Toplevel(window)

        l1 = Label(pubwindow, text="Artist Name").grid(row=1,column=5)
        name = StringVar()
        ee1 = Entry(pubwindow,textvariable=name)
        ee1.grid(row=1,column=6)

        l2 = Label(pubwindow, text="Artist Phone Number").grid(row=2,column=5)
        number = StringVar()
        ee2 = Entry(pubwindow,textvariable=number)
        ee2.grid(row=2,column=6)

        artistList = Listbox(pubwindow, height=10, width=45)
        artistList.grid(row=1, column=2, rowspan=6, columnspan=2)

        artistList.bind('<<ListboxSelect>>', selectRow1)

        b1 = ttk.Button(pubwindow, text="View All Artists",width=17,command=viewArtist)
        b1.grid(row=1, column=0)
        b2 = ttk.Button(pubwindow, text="Add New Artist", width=17,command=addArtist)
        b2.grid(row=2, column=0)
        b3 = ttk.Button(pubwindow, text="Delete Artist", width=17,command=deleteArtist)
        b3.grid(row=3, column=0)
        b4 = ttk.Button(pubwindow, text="Done", width=17, command=pubwindow.destroy)
        b4.grid(row=4, column=0)

        pubwindow.mainloop()

    "////////////////////////////////////////////////////////////////////////////////////"
    #----------------------------------ALBUM WINDOW---------------------------------
    "////////////////////////////////////////////////////////////////////////////////////"

    #Done
    def selectRow(Event):
        global gVar2
        index = list1.curselection()
        gVar2 = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, gVar2[0])
        e2.delete(0, END)
        e2.insert(END, gVar2[1])
        e3.delete(0, END)
        e3.insert(END, gVar2[2])
        e4.delete(0, END)
        e4.insert(END, gVar2[3])
        e5.delete(0, END)
        e5.insert(END, gVar2[4])
        e6.delete(0, END)
        e6.insert(END, gVar2[6])
        e0.delete(0, END)
        e0.insert(END, gVar2[5])

    #Done
    def viewAlbum():
            list1.delete(0, END)
            for row in backend.viewAllAlbums():
                list1.insert(END, row)

    #Done
    def searchAlbum():
        list1.delete(0, END)
        for row in backend.searchAlbumData(albumId_txt.get(),
         title_txt.get(), author_txt.get(), year_txt.get()):
            list1.insert(END, row)

    def addBook():
        backend.insert(albumId_txt.get(), title_txt.get(),
        author_txt.get(),year_txt.get())
        list1.delete(0, END)
        list1.insert(END, (albumId_txt.get(), title_txt.get(),
        author_txt.get(),year_txt.get()))
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

    #Done
    def deleteAlbum():
        backend.deleteAlbumData(gVar2[0])
        viewAlbum()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)

    #Done
    def updateAlbum():
        backend.updateAlbumData(albumId_txt.get(), title_txt.get(), author_txt.get(),
                       year_txt.get(), quantity_txt.get())
        viewAlbum()


    "////////////////////////////////////////////////////////////////////////////////////"
    #----------------------------------MAIN WINDOW---------------------------------
    "////////////////////////////////////////////////////////////////////////////////////"

    window = Tk()
    #window.geometry("500x100+300+300")
    # create a toplevel menu
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Artists",command=artistWindow)
    filemenu.add_command(label="Customers",command=customerWindow)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)

    menubar.add_cascade(label="View", menu=filemenu)
    # display the menu
    window.config(menu=menubar)

    # l0 = Label(window,text="customer_id")
    # l0.grid(row=0,column=9)
    l1 = Label(window, text="Album Id")
    l1.grid(row=1, column=9)
    l2 = Label(window, text="Album Name")
    l2.grid(row=2, column=9)
    l3 = Label(window, text="Artist")
    l3.grid(row=3, column=9)
    # l4 = Label(window, text="Publisher")
    # l4.grid(row=4, column=9)
    l5 = Label(window, text="Released")
    l5.grid(row=4, column=9)
    l6 = Label(window, text="Copies Available")
    l6.grid(row=6, column=9)


    albumId_txt = StringVar()
    e1 = Entry(window, textvariable=albumId_txt, fg='red')
    e1.grid(row=1, column=10)

    title_txt = StringVar()
    e2 = Entry(window, textvariable=title_txt, fg='red')
    e2.grid(row=2, column=10)

    author_txt = StringVar()
    e3 = Entry(window, textvariable=author_txt, fg='red')
    e3.grid(row=3, column=10)
    
    year_txt = StringVar()
    e4 = Entry(window, textvariable=year_txt, fg='red')
    e4.grid(row=4, column=10)
    # quantity_txt = StringVar()
    # e6 = Entry(window, textvariable=quantity_txt, fg='red')
    # e6.grid(row=6, column=10)

    list1 = Listbox(window, height=10, width=45)
    list1.grid(row=1, column=3, rowspan=6, columnspan=6)

    list1.bind('<<ListboxSelect>>', selectRow)

    b1 = ttk.Button(window, text="View All Albums",width=20, command=viewAlbum)
    b1.grid(row=1, column=0)
    b2 = ttk.Button(window, text="Search Albums", width=20, command=searchAlbum)
    b2.grid(row=2, column=0)
    b3 = ttk.Button(window, text="Add Album", width=20, command=addBook)
    b3.grid(row=3, column=0)
    b4 = ttk.Button(window, text="Update Album",
                    width=20, command=updateAlbum)
    b4.grid(row=4, column=0)
    b5 = ttk.Button(window, text="Delete Album",
                    width=20, command=deleteAlbum)
    b5.grid(row=5, column=0)
    b6 = ttk.Button(window, text="Close", width=20, command=window.destroy)
    b6.grid(row=6, column=0)

    "////////////////////////////////////////////////////////////////////////////////////"
    #----------------------------------ALBUM PURCHASE WINDOW---------------------------------
    "////////////////////////////////////////////////////////////////////////////////////"

    #Done
    def selectRow1(Event):
        global sidd
        index1 = list2.curselection()
        sidd = list2.get(index1)
        e7.delete(0, END)
        e7.insert(END, sidd[4])
        e8.delete(0, END)
        e8.insert(END, sidd[0])
        e9.delete(0, END)
        e9.insert(END, sidd[1])
        e0.delete(0, END)
        e0.insert(END, sidd[3])

    #Done
    def viewData():
        list2.delete(0, END)
        for row in backend.viewData():
            list2.insert(END, row)

    def issueBook():
        if (len(branchId_txt.get()) == 0 ):
            root = Tk()
            root.withdraw()
            messagebox.showerror("Branch ID","BRANCH ID MISSING")
            root.destroy()
            root.mainloop()
        else:
            backend.insertIssue(dateOut.get(), dueDate.get(),
                albumId_txt.get(),branchId_txt.get(),card_number.get())
            list2.delete(0, END)
            list2.insert(
                END, (dateOut.get(), dueDate.get(),
                albumId_txt.get(),branchId_txt.get(),card_number.get()))
            updateIsBook()

    def returnBook():
        backend.deleteIssueBook(sidd[2], sidd[3],sidd[4])
        viewData()
        viewBook()

    def updateIsBook():
        backend.updateIssueBook(albumId_txt.get(),branchId_txt.get(),quantity_txt.get())
        viewBook()

    def searchCard():
        list2.delete(0,END)
        for rows in backend.searchCards(card_number.get()):
            list2.insert(END,rows)

    def checkFine():
        print(dueDate.get(),dateIn.get())
        date1 = datetime.strptime(dueDate.get(), "%Y-%m-%d").date()
        date2 = datetime.strptime(dateIn.get(), "%Y-%m-%d").date()
        diff=date2-date1
        if(diff.days<=0):
            e11.delete(0,END)
            e11.insert(END,"no fine")
        else:
            e11.delete(0,END)
            e11.insert(END,diff.days * 5)

    l7 = Label(window, text="Customer ID")
    l7.grid(row=11, column=8)
    l8 = Label(window, text="Puchase Date")
    l8.grid(row=12, column=8)
    # l9 = Label(window, text="Due Date")
    # l9.grid(row=11, column=8)
    # l10 = Label(window, text="Date In")
    # l10.grid(row=12, column=8)
    # l11 = Label(window, text="Fine")
    # l11.grid(row=13, column=8)


    card_number = StringVar()
    e7 = Entry(window, textvariable=card_number, fg='red')
    e7.grid(row=11, column=9)
    dateOut = StringVar()
    e8 = Entry(window, textvariable=dateOut, fg='red')
    e8.grid(row=12, column=9)
    # dueDate = StringVar()
    # e9 = Entry(window, textvariable=dueDate, fg='red')
    # e9.grid(row=11, column=9)
    # dateIn = StringVar()
    # e10 = Entry(window, textvariable=dateIn, fg='red')
    # e10.grid(row=12, column=9)
    # fine = StringVar()
    # e11 = Entry(window, textvariable=fine, fg='red')
    # e11.grid(row=13, column=9)
    e8.delete(0, END)
    e8.insert(END, date.today())
    # e9.delete(0, END)
    # e9.insert(END,date.today()+timedelta(days=15))
    # e10.delete(0, END)
    # e10.insert(END, date.today())
    list2 = Listbox(window,height=10, width=30)
    list2.grid(row=9, column=3, rowspan=6, columnspan=2)

    list2.bind('<<ListboxSelect>>', selectRow1)

    b7 = ttk.Button(window, text="View Purchase Data", width=20, command=viewData)
    b7.grid(row=10, column=0)
    b8 = ttk.Button(window, text="Purchase Album", width=20, command=issueBook)
    b8.grid(row=11, column=0)
    b9 = ttk.Button(window, text="Return Album", width=20, command=returnBook)
    b9.grid(row=12, column=0)
    b9 = ttk.Button(window, text="Search", width=20, command=searchCard)
    b9.grid(row=13, column=0)
    # b9 = ttk.Button(window, text="Check", width=8, command=checkFine)
    # b9.grid(row=13, column=10)
    window.mainloop()


#---------------------------------Login id block----------------------------------
def validateLogin():
    if(username.get() == "s" and password.get() == "s"):
        tkWindow.destroy()
        guiPy()
    else:
        ll1 = Label(tkWindow, text="Incorrect username or password"
        ,fg="white",bg="red").grid(row=2, column=1)


tkWindow = Tk()
tkWindow.geometry('150x150')
tkWindow.title('Music Store Database')

usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=0)

passwordLabel = Label(tkWindow, text="Password").grid(row=2, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,
                      show='*').grid(row=3, column=0)

loginButton = ttk.Button(tkWindow, text="Login",
                         command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
