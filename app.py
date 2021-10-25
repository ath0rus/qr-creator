import tkinter as tk
from tkinter import messagebox
import qrcode as qr
import cv2 as cv

image = ""

##Check version/ test pop up
# tkinter._test()

#setup
window = tk.Tk()
window.title("QR Code Generator")
# window.geometry("200x150")
# 

#button functions
def test():
    tk.messagebox.showinfo("Test", e1.get())
    # cv.imshow("Image", img)

def genqr():
    global img
    img = qr.make(e1.get())
    e1.delete(0, 'end')
    img.save("qrcode1.png")
    tk.messagebox.showinfo("QR Code", "Your qr code was made")

# def open()


L1 = tk.Label(window, text = "Text/ Url")
L1.grid(row = 0, column= 0)

e1 = tk.Entry(window)
e1.grid(row = 0, column = 1)

B1 = tk.Button(window, text = "Generate", command=genqr)
B1.grid(row = 1, column= 0, columnspan= 2)

#ensures that the window stays open untill the user or code closes it
window.mainloop()