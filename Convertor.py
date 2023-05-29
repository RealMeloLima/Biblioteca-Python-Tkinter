import tkinter as tk
import ttkbootstrap as ttk
def convert():
    m_imput = entryInt.get()
    km_output = m_imput / 1000
    print(entryInt.get())
    output_string.set(f'{km_output} Km')

#Window
window = ttk.Window(themename= 'journal')
window.title('Demo')
window.geometry('400x150')

#Labels
title_label = ttk.Label(master = window, text = 'Metros para Quilômetros', font='Calibri 24 bold')
title_label.pack()

#Input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entryInt)
button = ttk.Button(master = input_frame, text= 'Converter', command= convert)
entry.pack(side='left', padx=10)
button.pack(side='left', padx=10)
input_frame.pack(pady=10)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text='Output', font='Calibri 20',textvariable=output_string)
output_label.pack(pady= 5)

#Run
window.mainloop()
