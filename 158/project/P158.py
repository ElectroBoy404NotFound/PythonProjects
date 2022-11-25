from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)

locked = False
i = 3

def authentication():
    global i
    global locked
    try:
        if len(input_box.get()) == 4:
            if not locked:
                if input_box.get() == "5521":
                    input_value = int(input_box.get())
                    messagebox.showinfo("Message","Credit card accepted")
                else:
                    if i <= 0:
                        locked = True
                        messagebox.showinfo("Alert","Credit card locked")
                    else:
                        i = i - 1
                        messagebox.showinfo("Alert","Credit card not accepted.Please enter correct Pin Code.\n" + str(i) + " tries remain")
            else:
                messagebox.showinfo("Alert","Credit card locked")
        else:
            messagebox.showinfo("Alert","Credit card not accepted.Please enter valid Pin Code")
    except(ValueError):
        messagebox.showinfo("Alert","Credit card not accepted.Please enter valid Pin Code")

btn = Button(root, text = "check credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()