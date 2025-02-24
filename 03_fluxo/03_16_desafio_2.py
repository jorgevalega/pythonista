import turtle
import customtkinter as ctk

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  # Modo de apariencia: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Tema de colores: "blue", "green", "dark-blue"

# Crear la ventana principal
app = ctk.CTk()
app.title("Control de Turtle con CustomTkinter")
app.geometry("400x300")

# Crear una instancia de Turtle
screen = turtle.Screen()
screen.title("Dibujo con Turtle")
t = turtle.Turtle()
t.shape("turtle")
t.color("green")  # Cambiar el color de la tortuga a verde

# Variables de control para los widgets
direccion_var = ctk.StringVar(value="Adelante")  # Dirección predeterminada
pixeles_var = ctk.StringVar()
rotacion_var = ctk.StringVar(value="Ninguna")  # Rotación predeterminada

# Función para mover la tortuga
def mover_tortuga():
    direccion = direccion_var.get()
    pixeles = int(pixeles_var.get())
    rotacion = rotacion_var.get()

    if rotacion == "Izquierda":
        t.left(90)
    elif rotacion == "Derecha":
        t.right(90)

    if direccion == "Adelante":
        t.forward(pixeles)
    elif direccion == "Atrás":
        t.backward(pixeles)

# Función para habilitar/deshabilitar el botón "Mover"
def validar_campos(*args):
    if direccion_var.get() and pixeles_var.get() and rotacion_var.get():
        boton_mover.configure(state="normal")
    else:
        boton_mover.configure(state="disabled")

# Crear un frame para centrar los widgets
frame_central = ctk.CTkFrame(app)
frame_central.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el frame en la ventana

# Crear los widgets de la interfaz dentro del frame central
label_direccion = ctk.CTkLabel(frame_central, text="Dirección:")
label_direccion.grid(row=0, column=0, padx=10, pady=10, sticky="e")

combo_direccion = ctk.CTkOptionMenu(frame_central, variable=direccion_var, values=["Adelante", "Atrás"])
combo_direccion.grid(row=0, column=1, padx=10, pady=10, sticky="w")

label_pixeles = ctk.CTkLabel(frame_central, text="Píxeles:")
label_pixeles.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entrada_pixeles = ctk.CTkEntry(frame_central, textvariable=pixeles_var)
entrada_pixeles.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label_rotacion = ctk.CTkLabel(frame_central, text="Rotación:")
label_rotacion.grid(row=2, column=0, padx=10, pady=10, sticky="e")

combo_rotacion = ctk.CTkOptionMenu(frame_central, variable=rotacion_var, values=["Ninguna", "Izquierda", "Derecha"])
combo_rotacion.grid(row=2, column=1, padx=10, pady=10, sticky="w")

boton_mover = ctk.CTkButton(frame_central, text="Mover", command=mover_tortuga, state="disabled")
boton_mover.grid(row=3, column=0, columnspan=2, pady=20)

# Asociar validación de campos a cambios en las variables
direccion_var.trace_add("write", validar_campos)
pixeles_var.trace_add("write", validar_campos)
rotacion_var.trace_add("write", validar_campos)

# Iniciar la aplicación
app.mainloop()