from tkinter import *
from tkinter import ttk
from functools import partial
from Imaginario import NumeroComplejo

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=3, sticky=(W, E))
        ttk.Button(mainframe, text='a+bi', command=partial(self.ponerNUMERO, '+')).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=3, row=2, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=4, row=2, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=4, row=3, rowspan=2, ipady=13, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=4, row=5, rowspan=2, ipady=13, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO,'1')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6,columnspan=2, ipadx=38, sticky=W)
        ttk.Button(mainframe, text='C', command=partial(self.borrarPanel)).grid(column=3, row=6, sticky=W)

        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    

    def ponerNUMERO(self, numero):
        if self.__panel.get().count("+") < 1:
            if self.__operadorAux==None:
                valor = self.__panel.get()
                self.__panel.set(valor+numero)
            else:
                self.__operadorAux=None
                if self.__panel.get().count("+") == 1:
                    cadena = self.__panel.get()
                   
                    separado = cadena.split('+')
                    self.__primerOperando = int(separado[0])
                    self.__segundoOperando = int(separado[1])
                    self.__panel.set(numero)
                else:
                    valor=self.__panel.get()
                    self.__primerOperando=int(valor)
                    self.__panel.set(numero)
        else:
            if(numero != '+'):
                if self.__operadorAux==None:
                    valor = self.__panel.get()
                    self.__panel.set(valor+numero)
                else:
                    self.__operadorAux=None
                    if self.__panel.get().count("+") == 1:
                        cadena = self.__panel.get()
                        
                        separado = cadena.split('+')
                        self.__primerOperando=int(separado[0])
                        self.__segundoOperando=int(separado[1])

                        self.__panel.set(numero)
                    else:
                        valor=self.__panel.get()
                        self.__primerOperando = int(valor)
                        self.__panel.set(numero)

    def borrarPanel(self):
        self.__panel.set('')

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':
                        resultado=operando1/operando2
        self.__panel.set(str(resultado))

    def resolverOpCompleja(self,parterealUno,parteImgUno,parteRealdos,parteImagDos,signo):
        resultado = 0
        if signo == "+":
            complejoUno=NumeroComplejo(parterealUno,parteImgUno)
            complejoDos=NumeroComplejo(parteRealdos,parteImagDos)
            suma=complejoUno+complejoDos
            resultado = "{}+{}i".format(suma.getReal(),suma.getImaginario())
        else:
            if (signo == "-"):
                complejoUno=NumeroComplejo(parterealUno,parteImgUno)
                complejoDos=NumeroComplejo(parteRealdos,parteImagDos)
                resta=complejoUno-complejoDos
                resultado = "{}+{}i".format(resta.getReal(),resta.getImaginario())
            else:
                if (signo == "*"):
                    complejoUno=NumeroComplejo(parterealUno,parteImgUno)
                    complejoDos=NumeroComplejo(parteRealdos,parteImagDos)
                    mul=complejoUno * complejoDos
                    resultado="{}+{}i".format(mul.getReal(),mul.getImaginario())
                else:
                    if (signo == "/"):
                        complejoUno=NumeroComplejo(parterealUno,parteImgUno)
                        complejoDos=NumeroComplejo(parteRealdos,parteImagDos)
                        division=complejoUno/complejoDos
                        resultado = "{}+{}i".format(division.getReal(),division.getImaginario())
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            if self.__panel.get().count('+')<1:
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando,operacion,self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
            else:
             
             if (self.__panel.get().count("+")==1):
                    cadenas = self.__panel.get()
                    separa = cadenas.split('+')
                    self.__primerOperandoDos= int(separa[0])
                    self.__segundoOperandoDos = int(separa[1])
                    self.resolverOpCompleja(self.__primerOperando,self.__segundoOperando,self.__primerOperandoDos,self.__segundoOperandoDos,operacion)
                    self.__operador.set('')
                    self.__operadorAux=None 
             
             
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                self.__segundoOperando=int(self.__panel.get())
                print(self.__segundoOperando)
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando) 
                self.__operador.set(op)
                self.__operadorAux=op