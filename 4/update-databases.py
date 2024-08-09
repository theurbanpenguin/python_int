from tkinter import *
import mysql.connector


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ssw0rd12!",
            database="wwproducts")

        self.mycursor = self.mydb.cursor()
        self.prices = []
        self.products = []
        self.mycursor.execute("SELECT product, price FROM products")
        self.row = self.mycursor.fetchone()
        while self.row is not None:
            self.products.append(self.row[0])
            self.prices.append(self.row[1])
            self.row = self.mycursor.fetchone()
        self.create_widgets()

    def create_widgets(self):
        self.lblproduct = list(self.products)
        self.entprice = list(self.prices)
        line = 1
        self.label0 = Label(self, text="Wood Product Prices")
        self.label0.grid(row=0, column=0, columnspan=2, sticky=W)

        self.heading1 = Label(self, text="Product")
        self.heading1.grid(row=line, column=0, sticky=W)
        self.heading2 = Label(self, text="Price")
        self.heading2.grid(row=line, column=1, sticky=W)

        for i in range(len(self.products)):
            line += 1
            self.lblproduct[i] = Label(self, text=self.products[i])
            self.lblproduct[i].grid(row=line, column=0, sticky=W)
            self.entprice[i] = Entry(self, width=5)
            self.entprice[i].grid(row=line, column=1, sticky=W)
            self.entprice[i].insert(END, self.prices[i])

        self.label4 = Label(self, text="")
        self.label4.grid(row=line, column=0)
        self.button1 = Button(self, text="Update prices", command=self.update)
        line += 1
        self.button1.grid(row=line, column=0, sticky=W)
        self.entry4 = Entry(self, width=10)
        self.entry4.grid(row=line, column=1)

    def update(self):
        for i in range(len(self.products)):
            self.prices[i] = self.entprice[i].get()
            sql = "UPDATE products SET price = %s WHERE product = %s"
            val = (self.prices[i], self.products[i])
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        self.mydb.close()
        self.entry4.delete(0, END)
        self.entry4.insert(END, "Updated")


window = Tk()
window.title("Wood Product Prices")
window.geometry("400x300")
app = Application(window)
app.mainloop()