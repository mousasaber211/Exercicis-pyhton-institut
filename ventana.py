from tkinter import *
ventana = Tk()
ventana.title('Ventana de Mousa')
ventana.config(bg="white")


pantalla = Frame()
pantalla.config(cursor='hand2')
etiqueta = Label(pantalla, text='Etiqueta 1')
etiqueta2 = Label(pantalla, text='Etiqueta 2')
etiqueta3 = Label(pantalla, text='Etiqueta 3')

etiqueta.pack()
etiqueta2.pack()
etiqueta3.pack()

pantalla.pack(side=TOP, anchor=W)
pantalla.config(width=500, height=500)
pantalla.config(bg='blue')
pantalla.config(bd=300)
pantalla.config(relief='sunken')
ventana.mainloop()









