import tkinter as tk
from PIL import Image, ImageTk

def Nachricht():
    Label.config(image=Bild)
    Label.image = Bild  # Keep a reference to avoid garbage collection

fenster = tk.Tk()
fenster.title("Test")

# Load the image using Pillow
original_image = Image.open("Test.jpeg")
Bild = ImageTk.PhotoImage(original_image)

Button = tk.Button(fenster, text="Knopf", command=Nachricht)
Button.pack(pady=20)

Label = tk.Label(fenster)
Label.pack(pady=20)

fenster.mainloop()
