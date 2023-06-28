import tkinter as tk

root = tk.Tk()
root.geometry('700x700')

canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

head = canvas.create_oval(300, 100, 400, 200,  width=3)
body = canvas.create_line(350, 200, 350, 300, fill='black', width=3)
left_leg = canvas.create_line(350, 300, 280, 400, fill='black', width=3)
right_leg = canvas.create_line(350, 300, 420, 400, fill='black', width=3)
left_arm = canvas.create_line(350, 240, 280, 200, fill='black', width=3)
right_arm = canvas.create_line(350, 240, 420, 200, fill='black', width=3)

root.mainloop()