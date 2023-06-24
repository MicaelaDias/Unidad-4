import tkinter as tk
from  tkinter  import *
from tkinter import ttk,font,messagebox
class Aplicacion:
    __ventana=None
    __cantidadVestimenta=None
    __cantidadA=None
    __cantidadE=None
    __precioVbase=None
    __precioAbase=None
    __precioEbase=None
    __precioVactual=None
    __precioAactual=None
    __precioEactual=None
    __ipc=None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title('Calculadora IPC')
        self.__ventana.resizable(0,0)
        #fuente=font.Font(weight='bold')
         #VARIABLES DE CONTROL
        self.__cantidadVestimenta=IntVar()
        self.__cantidadA=IntVar()
        self.__cantidadE=IntVar()
        self.__precioVbase=DoubleVar()
        self.__precioVactual=DoubleVar()
        self.__precioAbase=DoubleVar()
        self.__precioAactual=DoubleVar()
        self.__precioEbase=DoubleVar()
        self.__precioEactual=DoubleVar()
        self.__ipc=StringVar()
        self.__cantidadVestimenta.set('')
        self.__cantidadA.set('')
        self.__cantidadE.set('')
        self.__precioVbase.set('')
        self.__precioVactual.set('')
        self.__precioAbase.set('')
        self.__precioEactual.set('')
        self.__precioAactual.set('')
        self.__precioEbase.set('')


        self.__ipc.set('XX.XX %')
        self.marco=ttk.Frame(self.__ventana,border=2,relief='raised',padding=(40,40))
        self.itemLbl=ttk.Label(self.marco,text='Item',padding=(2,2))
        self.cantidadLbl=ttk.Label(self.marco,text='Cantidad',padding=(2,2))
        self.precioBaseLbl=ttk.Label(self.marco,text='Precio Año Base',padding=(2,2))
        self.precioActualLbl=ttk.Label(self.marco,text='Precio Año Actual',padding=(2,2))
        self.vestimentaLbl=ttk.Label(self.marco, text='Vestimenta',padding=(2,2))
        self.alimentoLbl=ttk.Label(self.marco,text='Alimento',padding=(2,2))
        self.educacionLbl=ttk.Label(self.marco,text='Educación',padding=(2,2))
        self.ipcLbl=ttk.Label(self.marco,text='IPC%')
        self.valor=ttk.Label(self.marco,textvariable=self.__ipc)
       

    
       

        #textVestimenta
        self.vestimentaCtext=ttk.Entry(self.marco,textvariable=self.__cantidadVestimenta,width=10)
        self.vestimentaPBtext=ttk.Entry(self.marco,textvariable=self.__precioVbase,width=10)
        self.vestientaPAtext=ttk.Entry(self.marco,textvariable=self.__precioVactual,width=10)
        #textAlimento
        self.alimentoCtext=ttk.Entry(self.marco,textvariable=self.__cantidadA,width=10)
        self.alimentoPBtext=ttk.Entry(self.marco,textvariable=self.__precioAbase,width=10)
        self.alimentoPAtext=ttk.Entry(self.marco,textvariable=self.__precioAactual,width=10)
        #textEducacion
        self.educacionCtext=ttk.Entry(self.marco,textvariable=self.__cantidadE,width=10)
        self.educacionPBtext=ttk.Entry(self.marco,textvariable=self.__precioEbase,width=10)
        self.educacionPAtext=ttk.Entry(self.marco,textvariable=self.__precioEactual,width=10)
        #botones
        botonCalcular=ttk.Button(self.marco,text='Calcular',command=self.calcular)
        boton=ttk.Button(self.marco,text='Salir',command=self.__ventana.destroy)
        #ubicacion
        self.vestimentaCtext.focus()
        self.marco.grid(column=0,row=0)
        self.itemLbl.grid(column=0,row=1)
        self.cantidadLbl.grid(column=1,row=1)
        self.precioBaseLbl.grid(column=2,row=1)
        self.precioActualLbl.grid(column=3,row=1)
        self.vestimentaLbl.grid(column=0,row=2)
        self.alimentoLbl.grid(column=0,row=3)
        self.educacionLbl.grid(column=0,row=4)
        self.vestimentaCtext.grid(column=1,row=2)
        self.vestimentaPBtext.grid(column=2,row=2)
        self.vestientaPAtext.grid(column=3,row=2)
        self.alimentoCtext.grid(column=1,row=3)
        self.alimentoPBtext.grid(column=2,row=3)
        self.alimentoPAtext.grid(column=3,row=3)
        self.educacionCtext.grid(column=1,row=4)
        self.educacionPBtext.grid(column=2,row=4)
        self.educacionPAtext.grid(column=3,row=4)
        botonCalcular.grid(column=1,row=6)
        boton.grid(column=2,row=6)
        self.ipcLbl.grid(column=0,row=7)
        self.valor.grid(column=1,row=7)

        self.__ventana.mainloop()
    def calcular(self):
       try:
        valorVC=int(self.vestimentaCtext.get())
        valorVPB=float(self.vestimentaPBtext.get())
        valorVPA=float(self.vestientaPAtext.get())
        valorAC=int(self.alimentoCtext.get())
        valorAPB=float(self.alimentoPBtext.get())
        valorAPA=float(self.alimentoPAtext.get())
        valorEC=int(self.educacionCtext.get())
        valorEPB=float(self.educacionPBtext.get())
        valorEPA=float(self.educacionPAtext.get())
       except ValueError:
          messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numerico')
     
       else:
          costoBase=valorVC*valorVPB+valorAC*valorAPB+valorEC*valorEPB
          costoActual=valorVC*valorVPA+valorAC*valorAPA+valorEC*valorEPA
          print(costoBase)
          print(costoActual)
         
          if costoActual!=0:
            division=costoActual/costoBase
            print(division)
            self.__ipc.set(int(division)*100)