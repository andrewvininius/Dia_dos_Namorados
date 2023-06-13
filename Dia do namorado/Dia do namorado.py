import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title('Feliz Dia dos Namorados!')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#8B0000')

data = datetime.today().strftime('%d/%m')

if data == '12/06':
    frase = "Feliz Dia dos Namorados! \u2764"  
    label = tk.Label(root, text=frase, font=('Arial', 24))
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
