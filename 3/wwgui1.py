from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.products = ["Lumber-2x4x96 inch",
                         "Lumber-2x6x96 inch",
                         "Lumber-2x4x96 inch Treated",
                         "Lumber-2x6x96 inch Treated",
                         "Plywood-1/4x48x96 inch",
                         "Plywood-1/2x48x96 inch",
                         "Plywood-1/2x48x96 inch Particleboard"]
        self.prices = [5.50,
                       8.50,
                       8.75,
                       13.25,
                       33.00,
                       37.25,
                       19.25]
        self.shipdays = {"1 Day": 20.00,
                         "2 Days": 15.00,
                         "3 Days": 10.00}
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
                                     text="{0:.2f}".format(self.prices[i]))
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
        self.button1 = Button(self, text="Reset")
        self.button1.grid(row=line, column=0)
        self.button2 = Button(self, text="Calculate Price")
        self.button2.grid(row=line, column=1)

        line += 1
        self.label3 = Label(self, text="")
        self.label3.grid(row=line, column=0)

        line += 1
        self.label4 = Label(self, text="Total:")
        self.label4.grid(row=line, column=0, sticky=E)
        self.result = Entry(self, width=10)
        self.result.grid(row=line, column=1, sticky=W)


window = Tk()
window.title("Wood Delivery Calculator")
window.geometry('400x325')
app = Application(window)
app.mainloop()