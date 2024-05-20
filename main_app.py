#mengimport package yg dibutuhkan

import qrcode, PIL #import package qrcode dan pillow
from PIL import ImageTk #mengimport imagetk dari package pillow
import tkinter as tk #import package tkinter sebagai tk
from tkinter import ttk,filedialog,messagebox #mengimport ttk,filedialog,messagebox dari package tkinter

#mendefinisikan fungsi

def createQR(*args): #mendefinisikan fungsi createQR
    data = text_entry.get()
    if data:
        img = qrcode.make(data) # QR code
        resized_img = img.resize((280,250,))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0, anchor=tk.NW,image= tkimage)
        qr_canvas.image = tkimage


def saveQR(*args): #mendefinisikan fungsi saveQR
    data = text_entry.get()
    if data:
        img = qrcode.make(data) # QR code
        resized_img = img.resize((280,250,))
        
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess","QR Code is Saved")
    else:
        messagebox.showwarning("Error", "Enter some data first")



#GUI/user interface

root = tk.Tk()
root.title("QR Code Generator") #memberikan judul 
root.geometry("300x380") #memberikan ukuran pada interface
root.config(bg="white") #memberikan warna pada background interface
root.resizable(0,0) #membuat ukuran interface tidak bisa diubah

frame1 = tk.Frame(root, bd=2, relief=tk.RAISED) #membuat frame1 pada interface
frame1.place(x=10, y=0, width=280, height=250) #mengatur tata letak frame1

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN) #membuat frame2 pada interface
frame2.place(x=10, y=260, width=280, height=100) #mengatur tata letak frame2

cover_img = tk.PhotoImage(file="Logo_SMK_Negeri_3_Depok (1).png")

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0, anchor=tk.NW,image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("Double-1",saveQR)
qr_canvas.pack(fill=tk.BOTH)


text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=5)

btn1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn1.place(x=25, y=50)

btn2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn2.place(x=100, y=50)

btn3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn3.place(x=175, y=50)


root.mainloop()