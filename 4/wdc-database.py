from tkinter import *
import mysql.connector
from decimal import Decimal
from datetime import date


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.products = []
        self.prices = []
        self.shipdays = {"1 Day": 20.00,
                         "2 Days": 15.00,
                         "3 Days": 10.00}

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd12!",
            database="wwproducts")

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SELECT product, price FROM products")
        self.row = self.mycursor.fetchone()
        while self.row is not None:
            self.products.append(self.row[0])
            self.prices.append(self.row[1])
            self.row = self.mycursor.fetchone()
        self.mydb.close()

        self.lblproduct = list(self.products)
        self.lblprice = list(self.prices)
        self.entry = list(self.products)
        self.create_widgets()

    def create_widgets(self):
        line = 1
        self.label2 = Label(self, text='Order Wood Products:')
        self.label2.grid(row=line, column=1, sticky=W)

        for i in range(len(self.products)):
            line += 1
            self.lblproduct[i] = Label(self, text=self.products[i])
            self.lblprice[i] = Label(self,
                                     text=str("{0:.2f}".format(self.prices[i])))
            self.entry[i] = Entry(self, width=3)
            self.entry[i].grid(row=line, column=0)
            self.lblproduct[i].grid(row=line, column=1, sticky=W)
            self.lblprice[i].grid(row=line, column=2, sticky=W)

        self.label1 = Label(self, text="Shipping:")
        line += 1
        self.label1.grid(row=line, column=0, sticky=W)

        self.ship = StringVar()
        line += 1

        self.radio1 = Radiobutton(self,
                                  text="1 Day",
                                  variable=self.ship,
                                  value="1 Day")
        self.radio1.grid(row=line, column=0, sticky=W)
        self.radio1.select()

        self.radio2 = Radiobutton(self,
                                  text="2 Days",
                                  variable=self.ship,
                                  value="2 Days")
        self.radio2.grid(row=line, column=1)

        self.radio3 = Radiobutton(self,
                                  text="3 Days",
                                  variable=self.ship,
                                  value="3 Days")
        self.radio3.grid(row=line, column=2, sticky=W)

        line += 1
        self.button1 = Button(self, text="Reset", command=self.reset)
        self.button1.grid(row=line, column=0)
        self.button2 = Button(self, text="Calculate Price", command=self.calculate)
        self.button2.grid(row=line, column=1)

        line += 1
        self.label3 = Label(self, text="")
        self.label3.grid(row=line, column=0)

        line += 1
        self.label4 = Label(self, text="Total:")
        self.label4.grid(row=line, column=0, sticky=E)
        self.result = Entry(self, width=10)
        self.result.grid(row=line, column=1, sticky=W)

        line += 1
        self.lblsubmit = StringVar()
        self.button3 = Button(self, text="Submit Order", command=self.submit)
        self.button3.grid(row=line, column=0)
        self.result2 = Label(self, textvariable=self.lblsubmit)
        self.result2.grid(row=line, column=1, sticky=W)

        menubar = Menu(self)
        filemenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Quit", command=window.quit)
        filemenu.add_command(label="Reset", command=self.reset)
        filemenu.add_command(label="Calculate Price", command=self.calculate)
        window.config(menu=menubar)

    def reset(self):
        """Reset the Radiobuttons and Entry boxes"""
        self.radio1.select()
        for i in range(len(self.products)):
            self.entry[i].delete(0, END)
        self.result.delete(0, END)

    def calculate(self):
        """Event handler for the calculator"""
        self.total = 0
        for i in range(len(self.products)):
            if (self.entry[i].get()):
                self.total += (self.prices[i] * int(self.entry[i].get()))

        if (self.ship.get() == "1 Day"):
            self.total += Decimal(self.shipdays["1 Day"])
        elif (self.ship.get() == "2 Days"):
            self.total += Decimal(self.shipdays["2 Days"])
        elif (self.ship.get() == "3 Days"):
            self.total += Decimal(self.shipdays["3 Days"])

        strPrice = "{0:.2f}".format(self.total)
        self.result.delete(0, END)
        self.result.insert(END, strPrice)

    def submit(self):
        """Insert order information to wworders database"""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd12!",
            database="wworders")

        self.mycursor = self.mydb.cursor()

        sql = ("INSERT INTO ordersummary "
               "(orderdate, shipmethod, totalprice) "
               "VALUES (%s, %s, %s)")
        val = (date.today(), self.ship.get(), self.total)

        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.mydb.close()
        self.lblsubmit.set("Order number "
                           + str(self.mycursor.lastrowid) + " submitted")


window = Tk()
window.title("Wood Delivery Calculator")
window.geometry('400x325')
app = Application(window)
app.mainloop()