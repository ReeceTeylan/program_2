# Second Program
# Name and Dream Job

import pyfiglet
import shutil
import time
import tkinter as tk
from tkinter import font

# Main Window
window = tk.Tk()
window.title("Name and Dream Job")
name_label = tk.Label(window, text="What is your name?",
font = font.Font(family = "Consolas",size = 16))
name_label.grid(row = 0, column = 0, padx = 10, pady = 10)
job_label = tk.Label(window, text="What is your Dream Job?",
font = font.Font(family = "Consolas",size = 16))
job_label.grid(row = 1, column = 0, padx = 10, pady = 10)
name_entry = tk.Entry(window, font = font.Font(family = "Consolas", size = 14))
name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
job_entry = tk.Entry(window, font = font.Font(family = "Consolas", size = 14))
job_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

def print_name_and_job():
    name = name_entry.get()
    job = job_entry.get()
    text = pyfiglet.figlet_format(f"Hello {name} !!!\nDream Job : {job}")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.008)
print_button = tk.Button(window, text="Print Name and Dream Job",
font = font.Font(family = "Consolas", size = 16),
command=print_name_and_job)
print_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
   


