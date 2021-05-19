from tkinter import*

def sum():
    number1 = entry_number1.get()
    number2 = entry_number2.get()
    answer = int(number1)+int(number2)
    lable_a.configure(text = "The answer is: " + answer)

form_p = Tk()

lable_number1 = Label(master = form_p , text= "Number1")

entry_number1 = Entry(master = form_p)

lable_number2 = Label(master = form_p , text= "Number2")

entry_number2 = Entry(master = form_p)

button_p = Button(master = form_p , text = "+" , command = sum)

lable_a = Label(master= form_p, text = "")

lable_number1.pack()

entry_number1.pack()

lable_number2.pack()

entry_number2.pack()

button_p.pack()

lable_a.pack()

mainloop()