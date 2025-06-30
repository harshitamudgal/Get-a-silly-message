from tkinter import *
from PIL import Image, ImageTk
import random

import sys
import os

def resource_path(relative_path):
    try:
       
        base_path = sys._MEIPASS
    except Exception:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

image_paths = [
    resource_path("images/img.png"),
    resource_path("images/img2.jpg"),
    resource_path("images/img3.jpeg"),
    resource_path("images/img4.jpg"),
    resource_path("images/img5.jpg"),
    resource_path("images/img6.jpeg"),
    resource_path("images/img7.png"),
    resource_path("images/img8.jpg"),
    resource_path("images/img9.jpg"),
    resource_path("images/img10.jpg"),
    resource_path("images/img11.jpg"),
    resource_path("images/img12.png"),
    resource_path("images/img13.jpg")
]



def type_text(label, text, i=0):
    if i == 0:
        label.config(text="")  # Clears before typing
    if i <= len(text):
        label.config(text=text[:i])
        label.after(40, lambda: type_text(label, text, i + 1))

def takename():
    name=namevar.get()
    
    if not name:
        type_text(reply_label, "Hey -_- tell me your name first!")
        image_label.pack_forget()  # Hide image if no name
        return
    
    messages = [
        "Hey {name}, you look abso-fuckin-lutely gorgeous today!",
        "{name}, you're doing amazing, sweetie.",
        "Yo {name}! The world is lucky to have you.",
        "Keep shining, {name}!",
        "Hi {name}, you deserve cookies today.",
        "Aw {name}, you look like you could use a hug, come here🫂",
        "Sup {name}, you little lazy legend 💫",
        "Well hello there, {name}. Get your ass up to work!",
        "{name}, you deserve better.",
        "Oh Honey, it does get better. \n Just one step at a time.",
        "Hey {name}, drink some water and romanticize your damn life.",
        "{name}, blink twice if you're procrastinating again.",
        "Reminder: {name}, your ancestors didn't survive plagues\n for you to cry over him/her.",
        "{name}, just be delulu, it's easier that way.",
        "The sun called. It’s jealous of your glow, {name}."
    ]
    
    random_message = random.choice(messages).format(name=name)
    random_image_path = random.choice(image_paths)

    og_image = Image.open(random_image_path)
    resized_image = og_image.resize((400, 200))
    image = ImageTk.PhotoImage(resized_image)
    
    # Update image_label with new image
    image_label.config(image=image)
    image_label.image = image  # prevent garbage collection

    type_text(reply_label, random_message)
    image_label.pack(pady=10)


window=Tk()
window.geometry("700x450")
window.minsize(700, 400)
window.configure(bg="#FFF8F0") 
window.title("Sign from the Heaven")

label=Label(text="Hey, kid. Tell me your name",
            font=("courier", 14),
            pady=15, padx=10, background="mint cream", relief="sunken")
label.pack(fill=X)

namevar=StringVar()

entry=Entry(window, textvariable=namevar)
entry.pack(pady=5)

button = Button(window, text="Send to the pearly gates", pady=5, padx=5,
                command=takename, bg="ivory", font=("consolas", 10))
button.pack(pady=10)

reply_label=Label(text="", font=("consolas", 11), padx=5, pady=4, justify="center")
reply_label.pack()


initial_image = Image.open(image_paths[0])
initial_resized = initial_image.resize((400, 200))
initial_photo = ImageTk.PhotoImage(initial_resized)
image_label = Label(window, image=initial_photo, relief="raised")
image_label.image = initial_photo
image_label.pack(pady=10)

# og_image = Image.open(r"C:\Users\harsh\OneDrive\Desktop\smth sm\Python\img.png")
# resized_image = og_image.resize((400, 200)) 

# image = ImageTk.PhotoImage(resized_image)
# image_label = Label(window, image=image, relief="raised")
# image_label.image = image  # Prevents garbage collection

footer = Label(window, text="✨Made with love by ur mom✨",
               font=("courier", 9), fg="#999", bg="#FFF8F0")
footer.pack(side=BOTTOM, pady=5, fill=X)
            
entry.bind("<Return>", lambda event: takename()) #can use enter key to submit too (yay)
window.mainloop()