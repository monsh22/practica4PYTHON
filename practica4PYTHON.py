import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_campos():
    limpiar_campos()

def guardar_datos():
    # Obtener los datos de los campos
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()

    # Verificar que los campos no este?n vaci?os
    if not nombres or not apellidos or not edad or not estatura or not telefono:
        messagebox.showerror("Error", "Todos los campos deben estar llenos.")
        return

    # Obtener el ge?nero seleccionado
    genero = "No especificado"
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # Crear una cadena con los datos
    datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} an?os\nEstatura: {estatura} cm\nTele?fono: {telefono}\nGe?nero: {genero}\n"

    try:
        # Guardar los datos en un archivo de texto
        with open("datos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n")

        # Mostrar un mensaje con los datos capturados
        messagebox.showinfo("Informacio?n", "Datos guardados con e?xito:\n\n" + datos)

        # Limpiar los controles despue?s de guardar
        limpiar_campos()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo.\nDetalles: {e}")

## Creacio?n de Ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")

# Crear variable para el RadioButton
var_genero = tk.IntVar()

## Creacio?n de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres :")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos :")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono :")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad :")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura :")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

## Creacio?n de Botones
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_campos)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btnGuardar.pack()

# Ejecutar ventana
ventana.mainloop()
