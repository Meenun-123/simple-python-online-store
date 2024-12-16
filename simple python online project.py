from tkinter import *
import time

root0 = Tk()
root0.title("Welcome page")
root0.geometry('360x270')
root0.grid()
txt = Label(root0, text="*_*_*_*_*_*_*_*_*_*_*_*PYTHON ONLINE STORE*_*_*_*_*_*_*_*_*_*_*_*_*_*", justify='left')
txt.grid(sticky='w')

def boot():
    root = Tk()
    root.title("Python project") 
    root.geometry('360x270')  
    root.grid()

    txt1 = Entry(root, text="enter text here") 
    txt1.grid(column=1, row=4)

    txt = Label(root, text="Enter your name here:-")  

    def click():
        rot1 = Tk()
        rot1.title("www.pythononlinestore.com/")
        rot1.geometry('740x360')
        rot1.grid()
        time.sleep(1)

        txt3 = Label(rot1, text="-------------------WELCOME TO ONLINE STORE------------------------ ", anchor='w', justify='left')
        txt3.grid(column=1, row=0, sticky='w')
        txt2 = Label(rot1, text="1)no.of pizzas", anchor='w', justify='left')
        txt2.grid(column=0, row=7, sticky='w')
        txt1 = Label(rot1, text="2)no.of cakes", anchor='w', justify='left')
        txt1.grid(column=0, row=8, sticky='w')
        txt0 = Label(rot1, text="3)no.of drinks", anchor='w', justify='left')
        txt0.grid(column=0, row=9, sticky='w')
        txt_1 = Label(rot1, text="4)no.of ice creams", anchor='w', justify='left')
        txt_1.grid(column=0, row=10, sticky='w')

        def next1():
            try:
                x = int(box1.get())
                y = int(box2.get())
                z = int(box3.get())
                i = int(box4.get())
                a = int(150 * x)
                b = int(70 * y)
                c = int(40 * z)
                d = int(20 * i)
                e = int(a + b + c + d)
                f = int(x + y + z + i)
               
                result_window = Tk()
                result_window.title("www.pythononlinestore.com/Final Bill/")
                result_window.geometry('400x300')

                num_label = Label(result_window, text=f"Pizzas you want to buy are {x} (cost of one pizza is 150 Rs): {a} Rs", justify='left')
                num_label.pack(anchor='w')

                num_label1 = Label(result_window, text=f"Cakes you want to buy are {y} (cost of one cake is 70 Rs): {b} Rs", justify='left')
                num_label1.pack(anchor='w')

                num_label2 = Label(result_window, text=f"Drinks you want to buy are {z} (cost of one drink is 40 Rs): {c} Rs", justify='left')
                num_label2.pack(anchor='w')

                num_label3 = Label(result_window, text=f"Ice creams you want to buy are {i} (cost of one ice cream is 20 Rs): {d} Rs", justify='left')
                num_label3.pack(anchor='w')

                num_label4 = Label(result_window, text=f"No. of items that you want to purchase are: {f}", justify='left')
                num_label4.pack(anchor='w')

                num_label5 = Label(result_window, text=f"The total cost of the items that you want to purchase is: {e} Rs", justify='left')
                num_label5.pack(anchor='w')

                def confirm_and_buy():
                    
                    exit_window = Tk()
                    exit_window.title("www.pythononlinestore.com/Final Bill/Exit")
                    exit_window.geometry('300x300')

                    h = Label(exit_window, text="Thank you for Buying.", justify='left')
                    h.grid(sticky='w')

                    j = Label(exit_window, text="Run again (Come again)!!!", justify='left')
                    j.grid(sticky='w')

                    def exit_application():
                        
                        exit_window.destroy()
                        result_window.destroy()
                        rot1.destroy()
                        root.destroy()
                        root0.destroy()

                    exit_button = Button(exit_window, text="Exit", command=exit_application)
                    exit_button.grid(sticky='w')

                    exit_window.mainloop()

                confirm_button = Button(result_window, text="Confirm and Buy", command=confirm_and_buy)
                confirm_button.pack()

                result_window.mainloop()
            except ValueError:
                num_label.config(text="Please enter the correct value")

        box1 = Entry(rot1)
        box1.grid(column=1, row=7, sticky='w')

        box2 = Entry(rot1)
        box2.grid(column=1, row=8, sticky='w')

        box3 = Entry(rot1)
        box3.grid(column=1, row=9, sticky='w')

        box4 = Entry(rot1)
        box4.grid(column=1, row=10, sticky='w')

        but2 = Button(rot1, text="Submit", command=next1)
        but2.grid(column=2, row=20, sticky='w')

        rot1.mainloop()

    txt2 = Label(root, text="Enter the password:-", anchor='w', justify='left')
    txt2.grid(column=0, row=5, sticky='w')
    txt.grid(column=0, row=4, sticky='w')

    box1 = Entry(root)
    box1.grid(column=1, row=5, sticky='w')

    but1 = Button(root, text="Submit", command=click, height=2, width=10)
    but1.grid(column=2, row=7, sticky='w')

    root.mainloop()

but0 = Button(root0, text="ENTER", height=4, width=10, fg='red', command=boot)
but0.grid(column=0, row=2, sticky='w')
root0.mainloop()
