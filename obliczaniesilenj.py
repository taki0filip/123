
import tkinter as tk

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def calculate():
    try:
        n = int(entry.get())
        result = silnia(n)
        output_label.config(text=f"{n}! = {result}")
    except ValueError:
        output_label.config(text="Podaj liczbę całkowitą!")

root = tk.Tk()
root.title("Obliczanie silni")

entry = tk.Entry(root, width=10)
entry.pack(side=tk.LEFT, padx=5, pady=5)

button = tk.Button(root, text="Oblicz", command=calculate)
button.pack(side=tk.LEFT, padx=5, pady=5)

output_label = tk.Label(root, text="")
output_label.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()