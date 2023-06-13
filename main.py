from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
import fileinput
from PIL import Image

def window():
    root = Tk()
    root.title("Gluing_Pictures")
    root.resizable(False, False)
    root.overrideredirect(False)
    root.geometry("370x370")

    image_1 = PhotoImage(file = "docs/1.png")
    image_2 = PhotoImage(file = "docs/2.png")
    image_3 = PhotoImage(file = "docs/3.png")
    image_4 = PhotoImage(file = "docs/4.png")

    def click_button():
        file = askopenfilename()
        fixed_width = 175
        img = Image.open(file)
        width_percent = (fixed_width / float(img.size[0]))
        height_size = int((float(img.size[0]) * float(width_percent)))
        new_image = img.resize((fixed_width, height_size))
        new_image.save('IMG_1.png')
        image_1 = PhotoImage(file = "IMG_1.png")
        # return image_1
    
    btn1 = ttk.Button(image=image_1, command=click_button)
    btn1.grid(row=0, column=0, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=NW)

    btn2 = ttk.Button(image=image_2,width=175, command=click_button)
    btn2.grid(row=0, column=1, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=NE)

    btn3 = ttk.Button(image=image_3,width=175, command=click_button)
    btn3.grid(row=1, column=0, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=SW)

    btn4 = ttk.Button(image=image_4,width=175, command=click_button)
    btn4.grid(row=1, column=1, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=SE)

    root.mainloop()

window()