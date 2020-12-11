from tkinter import * 
import grafos_betha as grafos

window = Tk()
window.geometry('350x200')
window.title("grafos")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    grafos.click()

def clicked2():
    grafos.click2()

def exit():
    window.destroy()

def about():
    root = Tk()
    root.geometry('300x200')
    root.title('About')
    info = Label(root, text="este programa fue creado para visualizar grafos a partir de una base de datos determinada")
    info.grid(column=0, row=0)
    
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=400, row=400)
btn2 = Button(window, text="prompting", command=clicked2)
btn2.grid(column=0, row=0)

#barra de menú 
menu = Menu(window)
File = Menu(menu, tearoff=0)
File.add_command(label='about', command=about) 
File.add_command(label='exit', command=exit)
menu.add_cascade(label='opciones', menu=File)
window.config(menu=menu)

if __name__ == "__main__":
    grafos.main()
    window.mainloop()
    