from tkinter import * 

def function_write():
    file_name = entry_name.get()+".txt"
    note = open(file_name , "w")
    text = text_diary.get("1.0" , "end")
    note.write(text)
    note.close()

def function_read():
    file_name = entry_name.get()+".txt"
    note = open(file_name , "r")
    n = note.read()
    text_diary.delete("1.0" , "end")
    text_diary.insert(1.0 , n)
    note.close()


form_diary = Tk()

label_massage = Label(master = form_diary , text = "نام فایل خود را وارد کنید")

entry_name = Entry(master = form_diary)

text_diary = Text(master = form_diary)

button_write = Button(master = form_diary , text = "ذخیره" , command = function_write)

button_read = Button(master=form_diary, text="بازکردن", command = function_read)

label_massage.pack()
entry_name.pack()
text_diary.pack()
button_write.pack()
button_read.pack()

mainloop()
