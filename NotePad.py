import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

window = tk.Tk()
window.title('NotePad')
window.geometry('500x500')
style = Style(theme='darkly')
style = ttk.Style()

style.configure('TNotebook.Tab', font=('TkDefaultFont', 14, 'bold'))

notebook = ttk.Notebook(window, style='TNotebook')

notes = {}
try:
    with open('notes.json', 'r') as f:
        notes = json.load(f)
except FileNotFoundError:
    pass


notebook = ttk.Notebook(window)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def addNote():
    noteFrame = ttk.Frame(notebook, padding=10)
    notebook.add(noteFrame, text='New Note')

    titleLabel = ttk.Label(noteFrame, text='Title:')
    titleLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

    titleEntry = ttk.Entry(noteFrame, width=40)
    titleEntry.grid(row=0, column=1, padx=10, pady=10)

    contentLabel = ttk.Label(noteFrame, text='Content:')
    contentLabel.grid(row=1, column=0, padx=10, pady=1, sticky='W')

    contentEntry = tk.Text(noteFrame, width=40, height=10)
    contentEntry.grid(row=1, column=1, padx=10, pady=10)

    def saveNote():
        title = titleEntry.get()
        content = contentEntry.get('1.0', tk.END)

        notes[title] = content.strip()

        with open('notes.json', 'w') as f:
            json.dump(notes, f)

        notesContent = tk.Text(notebook, width=40, height=10)
        notesContent.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(notesContent, text=title)

    saveButton = ttk.Button(noteFrame, text='Save', command=saveNote, style='secondary.TButton')
    saveButton.grid(row=2, column=1, padx=10, pady=10)

def loadNotes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)

        for title, content in notes.items():
            noteContent = tk.Text(notebook, width=40, height=10)
            noteContent.insert(tk.END, content)
            notebook.add(noteContent, text=title)
    except FileNotFoundError:
        pass

loadNotes()

def deleteNote():
    currentTab = notebook.index(notebook.select())
    noteTitle = notebook.tab(currentTab, 'text')

    confirm = messagebox.askyesno('Delete Note', f'Are you sure you want to delete {noteTitle}')

    if confirm:
        notebook.forget(currentTab)
        notes.pop(noteTitle)

        with open('notes.json', 'w') as f:
            json.dump(notes, f)

newButton = ttk.Button(window, text='New Note', command=addNote, style='info.TButton')
newButton.pack(side=tk.LEFT, padx=10, pady=10)

deleteButton = ttk.Button(window, text='Delete', command=deleteNote, style='primary.TButton')
deleteButton.pack(side=tk.LEFT, padx=10, pady=10)

window.mainloop()