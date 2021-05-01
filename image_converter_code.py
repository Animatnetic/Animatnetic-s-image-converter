from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
import os


def png_convert():
    filename = fd.askopenfilename()
    Image.open(filename).save("convert_result.png")
    if filename.endswith(".png"):
        Error_prompt = Label(root, text="Same Image type", width=20, font=("bold", 15),fg="red")
        Error_prompt.place(x=80, y=280)
    else:
        Success_prompt = Label(root, text="Converted successfully", width=20, font=("bold", 15),fg="red")
        Success_prompt.place(x=80, y=280)
        show_image = Image.open(filename)
        show_image.show()


def jpeg_convert():
    filename = fd.askopenfilename()
    Image.open(filename).save("convert_result.jpg")
    if filename.endswith(".jpeg"):
        Error_prompt = Label(root, text="Same Image type", width=20, font=("bold", 15), fg="red")
        Error_prompt.place(x=80, y=280)
    else:
        Success_prompt = Label(root, text="Converted successfully", width=20, font=("bold", 15),fg="green")
        Success_prompt.place(x=80, y=280)
        show_image = Image.open(filename)
        show_image.show()


def pdf_convert():
    filename = fd.askopenfilename()
    Image.open(filename).save("convert_result.pdf", resoultion=100.0)
    if filename.endswith("pdf"):
        Error_prompt = Label(root, text="Same Image type", width=20, font=("bold", 15), fg="red")
        Error_prompt.place(x=80, y=280)
    else:
        Success_prompt = Label(root, text="Converted successfully", width=20, font=("bold", 15),fg="red")
        Success_prompt.place(x=80, y=280)
        show_image = Image.open(filename)
        show_image.show()


root=Tk()
root.geometry("400x400")
root.title("Image_Converter")

Label_1=Label(root,text="Brows A file", width=20, font=("bold",15),fg="black")
Label_1.place(x=80,y=80)


Button(root,text="Convert to PNG", width=20, height=3, bg="grey",fg="white", command=png_convert).place(x=120,y=120)
Button(root,text=" Convert to PDF", width=20, height=3, bg="grey",fg="white", command=pdf_convert).place(x=120,y=220)
Button(root,text=" Convert to JPG", width=20, height=3, bg="grey",fg="white", command=jpeg_convert).place(x=120,y=320)

root.mainloop()