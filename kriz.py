import tkinter as tk

def draw_crossword(canvas, file_name, size):
    with open(file_name, "r") as file:
        for i, line in enumerate(file):
            line = line.strip()
            number, word = line.split(" ", maxsplit=1)
            number = int(number)
            index = word.find(word[number - 1])
            canvas.create_text(index * size + size // 2, i * size + size // 2, text=word[number-1], font=("Arial", size//2), fill="red")
            for j, letter in enumerate(word):
                x1, y1 = j * size, i * size
                x2, y2 = x1 + size, y1 + size
                if j == index:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="black")
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")
                canvas.create_text(x1 + size // 2, y1 + size // 2, text=letter, font=("Arial", size//2), fill="black")

#vytvorenie okna
root = tk.Tk()
root.title("Krížovka")

#vytvorenie Canvas
width, height = 800, 500
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

#vykreslenie krizovky
draw_crossword(canvas, "crossword.txt", 50)

#popis tajnicky
label_text = "Tajnička: Maturita(už len aby to samé napísalo sem)"
label = tk.Label(root, text=label_text, font=("Arial", 14))
label.pack()

root.mainloop()