import tkinter
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

canvas.create_rectangle()

with open("crossword.txt", "r") as file:
    words = [line.strip() for line in file]
    
print(words)
slovo = words[0]
print()

canvas.mainloop()