from tkinter import *

ventana = Tk()
ventana.title('Ventana de MOUSA')
ventana.config(bg="white")

ventana.iconbitmap("Travel_folder_file_10328.ico")


pantalla = Frame()
pantalla_2 = Frame()
pantalla.config(cursor='hand2')
pantalla_2.config(cursor='pirate')

etiqueta = Label(pantalla, text='Etiqueta 1')
etiqueta2 = Label(pantalla, text='Etiqueta 2')
etiqueta3 = Label(pantalla, text='Etiqueta 3')


etiqueta.pack(side=RIGHT)
etiqueta2.pack(side=LEFT)
etiqueta3.pack(side=TOP)

pantalla_2.pack(side=RIGHT, anchor='nw')
pantalla.pack(side=LEFT, anchor='sw')
pantalla.config(width=500, height=500)
pantalla_2.config(width=700, height=500)
pantalla.config(bg='blue')
pantalla_2.config(bg='red')
pantalla.config(bd=700)
pantalla.config(relief='sunken')
pantalla_2.config(relief= 'flat')
ventana.mainloop()









