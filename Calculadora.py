from tkinter import *


root = Tk()
root.title("Calculadora")
frame = Frame(root)
frame.pack()

# -------------------------------------------------Control Global-------------------------------------------------
operacion = ""
resultado = 0
check_operacion = 0
# --------------------------------------------------PANTALLA------------------------------------------------------

numero_pantalla = StringVar()
pantalla = Entry(frame, textvariable=numero_pantalla)
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#64f1e9", justify="right")


# -----------------------------------------------Pulsaciones teclado--------------------------------------------
def escribePulsado(tecla):
	global check_operacion
	if (check_operacion == 0):
		numero_pantalla.set(numero_pantalla.get() + tecla)
	else:
		numero_pantalla.set(tecla)
		check_operacion = 0


def suma(n):
	global operacion
	global resultado
	global check_operacion
	resultado += float(n)
	operacion = "suma"
	check_operacion = 1
	numero_pantalla.set(resultado)


def resta(n):
	global operacion
	global resultado
	global check_operacion
	resultado = float(n)
	operacion = "resta"
	check_operacion = 1
	numero_pantalla.set(resultado)


def division(n):
	global operacion
	global resultado
	global  check_operacion
	resultado = float(n)
	operacion = "division"
	check_operacion = 1
	numero_pantalla.set(resultado)

def multiplicacion(n):
	global operacion
	global resultado
	global  check_operacion
	resultado = float(n)
	operacion = "multiplicacion"
	check_operacion = 1
	numero_pantalla.set(resultado)

def exponenciar(n):
	global operacion
	global resultado
	global check_operacion
	resultado = float(n)
	operacion = "exponenciar"
	check_operacion = 1
	numero_pantalla.set(resultado)

def raiz(n):
	global operacion
	global resultado
	global check_operacion
	resultado = float(n)
	operacion = "raiz"
	check_operacion = 1
	igual()


def igual():
	global resultado
	global operacion
	if (operacion == "suma"):
		numero_pantalla.set(resultado + float(numero_pantalla.get()))
	elif (operacion == "resta"):
		numero_pantalla.set(resultado - float(numero_pantalla.get()))
	elif (operacion == "division"):
		numero_pantalla.set(resultado / float(numero_pantalla.get()))
	elif (operacion == "multiplicacion"):
		numero_pantalla.set(resultado * float(numero_pantalla.get()))
	elif (operacion == "exponenciar"):
		numero_pantalla.set(resultado ** float(numero_pantalla.get()))
	elif (operacion == "raiz"):
		numero_pantalla.set(resultado ** (1/float(2)))
	resultado = 0
	operacion=""

# ---------------------------------------------1ª FILA DE BOTONES-------------------------------------------------
boton7 = Button(frame, text="7", width=5, command=lambda: escribePulsado("7"))
boton7.grid(row=1, column=0)
boton8 = Button(frame, text="8", width=5, command=lambda: escribePulsado("8"))
boton8.grid(row=1, column=1)
boton9 = Button(frame, text="9", width=5, command=lambda: escribePulsado("9"))
boton9.grid(row=1, column=2)
boton_div = Button(frame, text="/", width=5, command=lambda: division(numero_pantalla.get()))
boton_div.grid(row=1, column=3)
boton_div = Button(frame, text="^", width=5, command=lambda: exponenciar(numero_pantalla.get()))
boton_div.grid(row=1, column=4)

# ---------------------------------------------2ª FILA DE BOTONES-------------------------------------------------
boton4 = Button(frame, text="4", width=5, command=lambda: escribePulsado("4"))
boton4.grid(row=2, column=0)
boton5 = Button(frame, text="5", width=5, command=lambda: escribePulsado("5"))
boton5.grid(row=2, column=1)
boton6 = Button(frame, text="6", width=5, command=lambda: escribePulsado("6"))
boton6.grid(row=2, column=2)
boton_mult = Button(frame, text="X", width=5, command=lambda: multiplicacion(numero_pantalla.get()))
boton_mult.grid(row=2, column=3)
boton_raiz = Button(frame, text="√", width=5, command=lambda: raiz(numero_pantalla.get()))
boton_raiz.grid(row=2, column=4)

# ---------------------------------------------3ª FILA DE BOTONES-------------------------------------------------
boton1 = Button(frame, text="1", width=5, command=lambda: escribePulsado("1"))
boton1.grid(row=3, column=0)
boton2 = Button(frame, text="2", width=5, command=lambda: escribePulsado("2"))
boton2.grid(row=3, column=1)
boton3 = Button(frame, text="3", width=5, command=lambda: escribePulsado("3"))
boton3.grid(row=3, column=2)
boton_rest = Button(frame, text="-", width=5, command=lambda: resta(numero_pantalla.get()))
boton_rest.grid(row=3, column=3)

# ---------------------------------------------4ª FILA DE BOTONES-------------------------------------------------
boton0 = Button(frame, text="0", width=5, command=lambda: escribePulsado("0"))
boton0.grid(row=4, column=0)
boton_coma = Button(frame, text=",", width=5, command=lambda: escribePulsado("."))
boton_coma.grid(row=4, column=1)
boton_igual = Button(frame, text="=", width=5, command=lambda: igual())
boton_igual.grid(row=4, column=2)
boton_suma = Button(frame, text="+", width=5, command=lambda: suma(numero_pantalla.get()))
boton_suma.grid(row=4, column=3)

root.mainloop()
