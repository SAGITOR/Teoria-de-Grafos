from tkinter import * 
import grafos_betha as grafos

window = Tk()
window.title("grafos")

#hacer el frame 
frame = Frame(window)
frame.pack()
frame.config(bg="lightblue")
frame.config(width=300, height=200)
frame.pack_propagate(False) 


lbl = Label(frame, text="presione uno de los botones para visualizar", bg="lightblue").pack()


def clicked():
    grafos.click()

def clicked2():
    grafos.click2()

def exit():
    window.destroy()

def about():
    root = Tk()
    root.title("About")
    scroll = Scrollbar(root)
    texto = Text(root, height=10, width=50)
    scroll.pack(side=RIGHT, fill=Y)
    texto.pack(side=LEFT, fill=Y) 
    scroll.config(command=texto.yview)
    texto.config(yscrollcommand=scroll.set)
    quote = """El siguiente programa tiene por objetivo brindar una visualización de grafos y prompting de una
situación de comunicación entre diversos nodos. \n 
    Versión 1.0 \n
    Integrantes: \n \n
    Pedro Pablo López Mena\n
    Aaron Patricio Cardenas Toro\n
    Marco Antonio Vivar de la Cruz\n 
    Maxiliano Zvonko Baranda Koschina\n
    Vicente Thomas Reyes Caceres\n \n
    Profesor: Fabian Riquelme \n \n 
    Asignatura: Matemáticas Discretas ICI UV"""
    texto.insert(END, quote)
    root.mainloop()
    
btn = Button(window, text="Grafico de Prompting", command=clicked).place(x=100, y=100)
btn2 = Button(window, text="Grafico de Aristas", command=clicked2).place(x=100, y=50)


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
    