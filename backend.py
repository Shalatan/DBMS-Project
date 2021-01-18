import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#--------------------------------------Book copies--------------------------------------

def LiBBranch():

    def addDetail():

        mydb = pymysql.connect(host="localhost",
                        user="root", password="shalatan", database="music")
        cur = mydb.cursor()
        add = "insert into BOOK_COPIES values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"')"
        cur.execute(add)
        mydb.commit()
        mydb.close()
        list1.delete(0, END)
        list1.insert(END, (e1.get(),e2.get(),e3.get()))

    def viewBook():
        mydb = pymysql.connect(host="localhost",
                        user="root", password="shalatan", database="music")
        cur = mydb.cursor()
        view = "select * from BOOK_COPIES"
        cur.execute(view)
        rows=cur.fetchall()
        mydb.close()
        list1.delete(0,END)
        for row in rows:
            list1.insert(END, row)
    def quit_me():
        print('quit')
        window.quit()
        window.destroy()
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", quit_me)
    l1 = Label(window, text="Quantity")
    l1.grid(row=0, column=0)
    l2 = Label(window, text="Book ID")
    l2.grid(row=0, column=2)
    l3 = Label(window, text="Branch ID")
    l3.grid(row=0, column=4)

    qquantity_txt = StringVar()
    e1 = Entry(window, textvariable=qquantity_txt, fg='blue')
    e1.grid(row=0, column=1)
    qbookId_txt = StringVar()
    e2 = Entry(window, textvariable=qbookId_txt, fg='blue')
    e2.grid(row=0, column=3)
    qbranchid_txt = StringVar()
    e3 = Entry(window, textvariable=qbranchid_txt, fg='blue')
    e3.grid(row=0, column=5)

    list1 = Listbox(window, height=10, width=45)
    list1.grid(row=1, column=1, rowspan=6, columnspan=3)

    b1 = ttk.Button(window, text="View data",
                    width=12, command=viewBook)
    b1.grid(row=1, column=5)
    b2 = ttk.Button(window, text="Add Entry", width=12, command=addDetail)
    b2.grid(row=2,column=5)
    b3 = ttk.Button(window, text="Done", width=12, command=quit_me)
    b3.grid(row=3,column=5)

    window.mainloop()

#--------------------------------------error Block--------------------------------------

def errorMessage(error):

    root = Tk()
    root.withdraw()

    if(error==1):
        messagebox.showerror("Depulicate entry",
        "this book is already been added")

        MsgBox = messagebox.askquestion ('Add Book Quantity',
        'Do you want to add book copies in another branch',icon = 'warning')
        if MsgBox == 'yes':
            LiBBranch()
            root.destroy()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
    elif(error==2):
        messagebox.showwarning("Unknow Publisher",
        """Publisher name not yet added in\nthe publisher data.
        Go to: View->Publisher->Add Publisher""")
    root.quit()
    root.destroy()
    root.mainloop()

def connect():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    mydb.close()


#--------------------------------------Artist Details--------------------------------------

# Done
def insertArtist(name,number):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    insertArtist = "insert into artists values('"+name+"','"+number+"')"
    cur.execute(insertArtist)
    mydb.commit()
    mydb.close()

# Done
def viewArtistData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    viewArtists = "select * from artists"
    cur.execute(viewArtists)
    row = cur.fetchall()
    mydb.close()
    return row

# Done
def deleteArtist(name):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    deleteArtist="delete from artists where ARTIST_NAME ='"+name+"'"
    cur.execute(deleteArtist)
    mydb.commit()
    mydb.close()

#--------------------------------------Customer Details--------------------------------------

# Done
def insertCustomer(id,name,address):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    insertLab = "insert into customer values('"+id+"','"+name+"','" +address+"')"
    cur.execute(insertLab)
    mydb.commit()
    mydb.close()

# Done
def viewCustomerData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    viewLab = "select * from customer"
    cur.execute(viewLab)
    row = cur.fetchall()
    mydb.close()
    return row

# Done
def deleteCustomerData(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    deleteLab="delete from customer where CUSTOMER_ID ='"+str(id)+"'"
    cur.execute(deleteLab)
    mydb.commit()
    mydb.close()

"--------------------------------------add book details---------------------------------------"


def insert(Branch_id,id, title, author, year, publisher,quantity):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    insertBooks = "insert into Book values('"+id+"','"+title+"','" + \
        author+"','" + publisher+"','"+year+"')"
    insertBookCopies= "insert into BOOK_COPIES values('"+str(quantity)+"','"+str(id)+"','"+ \
        str(Branch_id)+"')"
    try:
        cur.execute(insertBooks)
        cur.execute(insertBookCopies)
    except pymysql.err.IntegrityError as e:
        if(e.args[0]==1062):
            errorMessage(1)
        elif(e.args[0]==1452):
            errorMessage(2)

    mydb.commit()
    mydb.close()

# Done
def viewAllAlbums():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    viewAlbums = "select * from album"
    cur.execute(viewAlbums)
    row = cur.fetchall()
    mydb.close()
    return row

#Done
def searchAlbumData(id="", title="", author="", year="", publisher=""):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    searchBook = ("select * from album where ALBUM_ID = '"+id+"' or ALBUM_NAME = '"+title +
                  "' or ARTIST_NAME = '"+author+"' or RELEASE_DATE = '"+year+"'")
    cur.execute(searchBook)
    row = cur.fetchall()
    mydb.close()
    return row

# Done
def deleteAlbumData(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    deleteAlbumData = ("delete from album where ALBUM_ID = '"+str(id)+"'")
    cur.execute(deleteAlbumData)
    mydb.commit()
    mydb.close()

# Done
def updateAlbumData(id, title, author, year, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    updateBook = ("update album set ALBUM_NAME = '"+title+"', ARTIST_NAME = '" +
                  author+"', RELEASE_DATE = '"+year+"' where ALBUM_ID = '"+str(id)+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()


"--------------------------------------BOOK ISSUE---------------------------------------"


def viewData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    cur.execute("select * from BOOK_LENDING")
    rows = cur.fetchall()
    mydb.close()
    return rows

def searchCards(cardNo):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    searchcard = ("select * from BOOK_LENDING where CARD_NO  = '"+cardNo+"'")
    cur.execute(searchcard)
    row = cur.fetchall()
    mydb.close()
    return row

def insertIssue(dateo,ddate,bookId,branchId,cardNumber):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    insertdata = "insert into BOOK_LENDING values('" + \
        str(dateo) + "','"+ddate+"','"+str(bookId)+"','"+str(branchId)+"','"+str(cardNumber)+"')"
    cur.execute(insertdata)
    mydb.commit()
    mydb.close()

def updateIssueBook(bId,braId, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()
    updateBook = ("update BOOK_COPIES set NoOfCopies = '" +
                  str(int(quantity)-1)+"' where bookId='"+str(bId)+"' and branchID='"+str(braId)+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()

def deleteIssueBook(BId,BraId,cardNumber):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="shalatan", database="music")
    cur = mydb.cursor()

    # to obtain book quantity from books table
    showData1 = ("select NoOfCopies from BOOK_COPIES where bookId = '" +
                 str(BId)+"' and branchId = '" +
                 str(BraId)+"'")
    cur.execute(showData1)          # ((2),)
    row1 = cur.fetchall()
    bookQuantity = (row1[0][0])
    bookQuantity += 1

    deleteBook = ("delete from BOOK_LENDING where CARD_NO = '" +
                  str(cardNumber)+"'and BOOK_ID = '" +
                  str(BId)+"' and BRANCH_ID = '" +
                  str(BraId)+"'")
    updateBook = ("update BOOK_COPIES set NoOfCopies = '" +
                  str(bookQuantity) + "' where bookId='"+str(BId)+"' and branchId='"+str(BraId)+"'")
    cur.execute(updateBook)
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()


connect()
