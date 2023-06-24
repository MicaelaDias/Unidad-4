import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from tkinter import ttk, messagebox
class Aplicacion:
    __ventana=None
    __precioSinIva=None
    __precioConIva=None
    __porcentaje=None
    __iva=None
    __mostrar=None
    __mostrarIva=None
    def __init__(self):
        self.__ventana=Tk()
        
        self.__ventana.resizable(0,0)
        self.__ventana.title("Calculadora IVA")
        
        self.marco=ttk.Frame(self.__ventana, padding=(40,50))
        self.__precioSinIva=DoubleVar()
        self.__precioConIva=DoubleVar()
        self.__porcentaje=DoubleVar()
        self.__iva=DoubleVar()
        self.valor=IntVar()
        self.__mostrar=StringVar()
        self.__mostrarIva=StringVar()
        self.__precioSinIva.set('')
        self.__iva.set('')
        self.__mostrar.set('')
        #Cabecera
        self.tituloLbl=tk.Label(self.__ventana,text='Cálculo de IVA',bg='light blue',borderwidth=1,width=41)
        self.precioLbl=ttk.Label(self.marco,text='Precio sin IVA',padding=(5,5))
        self.precioSinIva=ttk.Entry(self.marco,textvariable=self.__precioSinIva)
        self.precioSinIva.focus()
        ttk.Radiobutton(self.marco, text='IVA 21%',value=0,variable=self.valor,command=self.porcentaje).grid(row=2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(self.marco, text='IVA 10.5%',value=1,variable=self.valor,command=self.porcentaje).grid(row=3, column=0, columnspan=1, sticky='w')
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.ivaLb=tk.Label(self.marco,text='IVA')
        self.ivaLabel=tk.Label(self.marco,textvariable=self.__mostrarIva,borderwidth=1,relief='solid',width=15)
        self.precioIvaLbl=tk.Label(self.marco,text='Precio con IVA')
        self.precioConIvaLabel=tk.Label(self.marco,textvariable=self.__mostrar,borderwidth=1,relief='solid',width=15)
        self.separ2= ttk.Separator(self.marco, orient=HORIZONTAL)
        self.calcularB=tk.Button(self.marco,text='Calcular',bg='light blue',command=self.calcular)
        self.salir=tk.Button(self.marco,text='Salir',bg='red',command=self.__ventana.destroy)
        #ubicar
        self.marco.grid(column=0,row=1)
        self.tituloLbl.grid(column=0,row=0)
        self.precioLbl.grid(column=0,row=1)
        self.precioSinIva.grid(column=1,row=1)
        self.separ1.grid(column=0,row=5,rowspan=2)
        self.ivaLb.grid(column=0,row=6)
        self.ivaLabel.grid(column=1,row=6)
        self.precioIvaLbl.grid(column=0,row=7)
        self.precioConIvaLabel.grid(column=1,row=7)
        self.separ2.grid(column=0,row=8,columnspan=20)
        self.calcularB.grid(column=0,row=10,rowspan=4)
        self.salir.grid(column=1, row=10,rowspan=2)
       
        self.__ventana.mainloop()
    def porcentaje(self):
        if self.valor.get()==0:
            self.__porcentaje.set(21)
        else:
            if self.valor.get()==1:
                self.__porcentaje.set(10.5)
    def calcular(self):
        try:
            valor=float(self.precioSinIva.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')   
            self.__precioSinIva.set('')
            self.__iva.set('')
            self.__mostrar.set('')
            self.precioSinIva.focus()
            
        else:
            self.__iva.set(valor*self.__porcentaje.get()/100)
            self.__precioConIva.set(self.__iva.get()+valor)
            self.__mostrarIva.set('{:.1f}'.format(self.__iva.get()))
            self.__mostrar.set('{:.1f}'.format(self.__precioConIva.get()))
