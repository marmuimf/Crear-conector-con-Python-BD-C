#Interfaz gestionada con un XML

#instalar libreria: pip install bs4 para poder leer XML desde Python
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def salir():
    raiz.destroy()#salgo del programa

raiz = tk.Tk()

#definicion Ventana
raiz.title("Formulario Disney")
raiz.geometry("700x550+100+100")#margenes ventana
raiz.iconbitmap("logo.ico")

barramenu= tk.Menu(raiz)
#elemento menu: Archivo
raiz.config(menu=barramenu)
archivo = tk.Menu(barramenu,tearoff=0)#tearoff=1 sacar barra de herramientas
barramenu.add_cascade(label="Arhivo",menu=archivo)
#añado comandos de menu: Archivo
archivo.add_command(label="Nuevo")
archivo.add_command(label="Salir",command=salir)
#elemento menu: Ayuda
ayuda = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=ayuda)

ttk.Label(raiz,text="Indica tu pelicula favorita de las siguientes:").pack(padx=5,pady=5)
ttk.Combobox(raiz,values=['Cenicienta','Blancanieves','La Sirenita','Mulan']).pack(padx=10,pady=10)#campo desplegable

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for campo in xml.find_all("campo"): #encuentra todos los elementos que se llamen campo
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "entrada":
        ttk.Entry(raiz).pack(padx=10,pady=5)
    elif tipo == "etiqueta":
        ttk.Label(raiz,text=texto).pack(padx=5,pady=5)
    elif tipo == "boton":
        ttk.Button(raiz,text=texto).pack(padx=5,pady=5)
    elif tipo == "multiple":
        ttk.Checkbutton(raiz,text=texto).pack(padx=10,pady=10) #campos de seleccion multiple
    elif tipo == "numerico":
        ttk.Spinbox(raiz,from_=0,to=100).pack(padx=10,pady=10)#campo numerico
    elif tipo == "deslizable":
        ttk.Scale(raiz,from_=0,to=100).pack(padx=10,pady=10)#deslizable
    elif tipo == "radio":
        ttk.Radiobutton(raiz,text=texto).pack(padx=5,pady=5)
    

tk.mainloop()

    
