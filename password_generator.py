import tkinter as tk
import random
import string

# Frame  #
root = tk.Tk()
root.title("Password Generator")
root.geometry("700x330+300+150")
root.config(bg="#F5F5DC")  
root.resizable(False, False)

# Header 
header_frame = tk.Frame(root, width=700, height=70, bg="#8B0000") 
header_frame.place(x=0, y=0)

title_label = tk.Label(header_frame,text="PASSWORD GENERATOR",font=("Times New Roman", 25, "bold"),bg="#8B0000",
fg="#FFFFFF")
title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#  Decorative Line
divider = tk.Frame(root, bg="#000000", height=4, width=700)
divider.place(x=0, y=70)

# Generate Password Function 
def generate_password():
    length = 12
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#!&_"
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Password Display 
password_entry = tk.Entry(root,font=("Times New Roman", 18, "bold"),width=33,bd=3,relief=tk.SOLID,
justify='center',bg="#FFFFFF",fg="#000000")
password_entry.place(x=150, y=140)

# Generate Button
generate_button = tk.Button(root,text="GENERATE",font=("Times New Roman", 18, "bold"),bg="#8B0000",
fg="#000000",padx=20,pady=5,command=generate_password)
generate_button.place(x=245, y=200)

# Footer 
footer = tk.Label(root,text="Classic Password Tool | Built with Python",font=("Times New Roman", 12),
bg="#F5F5DC",fg="#000000")
footer.place(x=210, y=280)

root.mainloop()