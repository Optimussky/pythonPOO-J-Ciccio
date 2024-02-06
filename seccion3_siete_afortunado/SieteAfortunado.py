# Siete Afortunado

# Clases
    # Atributos
    # Métodos
    # Ciclos
    # Arreglos

# Interfaces gráficas
    # Eventos


from tkinter import *
import random 

class SieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
    
    def crear_interfaz(self):
        ventana = Tk()
        ventana.title("💰 Siete Afortunado 💲")
        ventana.minsize(340,450)
        ventana.geometry('340x450')

        boton = Button(ventana, text="Jugar!", command=self.jugar, font='arial 18 bold')
        boton.pack()

        foto = PhotoImage(file=r'dinero.png')
        self.gano = Label(ventana, image=foto)

        self. campos = [StringVar() for elemnto in range(3)]
        posicion = 10
        for campo in self.campos:
            label = Label(ventana, textvariable=campo, background='white', foreground='Black', font='arial 42 bold')
            label.place(x=posicion, y=100, width=100, height=100)
            posicion += 110


        mainloop()

    def generar_numero(self):
        return random.randint(0,9)

    def jugar(self):
        hay_un_siete = False
        for i in range(3):
            valor = self.generar_numero()
            self.campos[i].set(valor)
            if (valor == 7):
                hay_un_siete = True
        
        if (hay_un_siete):
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()

        

jugar = SieteAfortunado()