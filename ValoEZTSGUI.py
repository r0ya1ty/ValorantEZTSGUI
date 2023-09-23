import ctypes
import tkinter as tk
from tkinter import ttk


def apply_changes():
    window_title = "VALORANT  "
    global original_style
    window_handle = ctypes.windll.user32.FindWindowW(None, window_title)
    if window_handle == 0:
        lbl_status.config(text="Valorant not found")
    else:
        original_style = ctypes.windll.user32.GetWindowLongW(window_handle, ctypes.c_int(-16))
        new_style = original_style & ~0x00800000 & ~0x00040000
        ctypes.windll.user32.SetWindowLongW(window_handle, ctypes.c_int(-16), new_style)
        ctypes.windll.user32.ShowWindow(window_handle, ctypes.c_int(3))
        lbl_status.config(text="True stretched applied")


def unapply_changes():
    window_title = "VALORANT  "
    window_handle = ctypes.windll.user32.FindWindowW(None, window_title)

    if window_handle == 0:
        lbl_status.config(text="Valorant not found")
    else:
        ctypes.windll.user32.SetWindowLongW(window_handle, ctypes.c_int(-16), original_style)
        lbl_status.config(text="True stretch removed")


root = tk.Tk()
root.title("ValorantEZTSGUI")
root.geometry("300x300")

root.configure(bg="#2e2e2e")

frame = ttk.Frame(root, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

lbl_title = ttk.Label(frame, text="ValoEZTSGUI", font=("Arial", 16))
lbl_title.grid(row=0, columnspan=2)

lbl_status = ttk.Label(frame, text="")
lbl_status.grid(row=3, columnspan=2)

btn_apply = ttk.Button(frame, text="Apply", compound=tk.LEFT, command=apply_changes)
btn_apply.grid(row=1, column=0)

btn_unapply = ttk.Button(frame, text="Unapply", compound=tk.LEFT, command=unapply_changes)
btn_unapply.grid(row=1, column=1)

root.mainloop()
