import tkinter as tk
import requests
from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion:
    __ventana=None
    __pesos=None
    __dolares=None
    __venta=None
    __mostrar=None
    def __init__(self):
        
        url='https://www.dolarsi.com/api/api.php?type=dolar'
        respuesta=requests.get(url)
        dJson=respuesta.json()
       
        i=0
        longitud=len(dJson)
        bandera=True
        while i<longitud and bandera:
            if dJson[i]['casa']['nombre']=='Oficial':
                bandera=False
            else:
                i+=1
        if not bandera:
            self.__venta=float(dJson[i]['casa']['venta'].replace(',','.'))
        
        self.__ventana = Tk()
        self.__ventana.geometry('330x115')
        self.__ventana.resizable(0,0)
        self.__ventana.title('Conversor de moneda')
        #variables de control
        self.__dolares=IntVar()
        self.__pesos=DoubleVar()
        
        self.__mostrar=StringVar()
        self.__dolares.set('')
        self.__pesos.set('')
        #cuerpo
        self.marco=ttk.Frame(self.__ventana,relief="sunken",padding=(80,10))
        self.__dolares.trace('w',self.calcular)
        self.dolarEntry=tk.Entry(self.marco,textvariable=self.__dolares,width=10)
        self.dolarEntry.focus()
        self.dolaresLabel=tk.Label(self.marco,text='dólares')
        self.equivalenteLabel=tk.Label(self.marco,text='es equivalente a')
        self.precioLb=tk.Label(self.marco,textvariable=self.__mostrar)
        self.pesosLabel=tk.Label(self.marco,text='pesos')
        self.salirB=tk.Button(self.marco,text='Salir',command=self.__ventana.destroy,width=11)
        
        #ubicar
        self.marco.grid(row=0,column=0,sticky='nw')
        self.dolarEntry.grid(column=1,row=1)
        self.dolaresLabel.grid(column=2,row=1,sticky='nwes')
        self.equivalenteLabel.grid(column=0,row=3)
        self.precioLb.grid(column=1,row=3)
        self.pesosLabel.grid(column=2,row=3)
        self.salirB.grid(column=2,row=4)
        self.__ventana.mainloop()
    def calcular(self,*args):
        if self.dolarEntry.get()!='':
            try:
                valor=int(self.dolarEntry.get())
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
                self.__dolares.set('')
                self.__mostrar.set('')
                self.dolarEntry.focus()
            else:
                if valor>0:
                    self.__pesos.set(valor*self.__venta)
                else:
                    self.__pesos.set(0)
                self.__mostrar.set('{:.3f}'.format(self.__pesos.get()))
                self.dolarEntry.focus()
        else:
            self.__mostrar.set('')        