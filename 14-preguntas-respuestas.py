import tkinter as tk 
from tkinter import ttk 
import random 

class JuegoPreguntasRespuestasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Preguntas y Respuestas")

        self.preguntas = {
            "Ciencia": {
                "¿Cuál es el planeta más grande del sistema solar?": "Jupiter",
                "¿Quién descubrió la penicilina?": "Alexander Fleming", 
                "¿Qué gas necesitan las plantas para realizar la fotosíntesis?": "Dióxido de carbono"
            },
            "Historia":{
                "¿En qué año se firmó la declaración de la independencia de los Estados Unidos?": "1776", 
                "¿En qué periodo se desarrolló la 2da guerra mundial?": "1939 - 1945",
                "¿En qué año cayó el muro de Berlín?": "1989"
            }
        }

        self.categorias_combobox = ttk.Combobox(self.master, values=list(self.preguntas.keys()))
        self.categorias_combobox.grid(row=0, column=0, padx=5, pady=5)

        self.iniciar_button = ttk.Button(self.master, text="Iniciar Juego", command=self.iniciar_juego)
        self.iniciar_button.grid(row=0, column=1, padx=5, pady=5)

        self.pregunta_label = ttk.Label(self.master, text="")
        self.pregunta_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.respuesta_entry = ttk.Entry(self.master, width=30)
        self.respuesta_entry.grid(row=2, column=0, padx=5, pady=5)

        self.verificar_button = ttk.Button(self.master, text="Verificar", command=self.verificar_respuesta)
        self.verificar_button.grid(row=2, column=1, padx=5, pady=5)

        self.respuesta_correcta_label = ttk.Label(self.master, text="")
        self.respuesta_correcta_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def iniciar_juego(self):
        categoria = self.categorias_combobox.get()
        preguntas_categoria = self.preguntas.get(categoria, {})
        if preguntas_categoria:
            self.pregunta_actual = random.choice(list(preguntas_categoria.keys()))
            self.pregunta_label.config(text=self.pregunta_actual)
            self.respuesta_correcta_label.config(text="")
            self.respuesta_entry.delete(0, tk.END)
        else:
            self.pregunta_label.config(text="No hay preguntas disponibles para esta  categoría")

    def verificar_respuesta(self):
        respuesta_ingresada = self.respuesta_entry.get()
        respuesta_correcta = self.preguntas[self.categorias_combobox.get()].get(self.pregunta_actual)
        if respuesta_ingresada.lower() == respuesta_correcta.lower():
            self.respuesta_correcta_label.config(text="¡Respuesta Correcta!")
        else:
            self.respuesta_correcta_label.config(text=f"Respuesta incorrecta crack, andá a estudiar. Tenías que responder {respuesta_correcta}, no esa guasada!!!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPreguntasRespuestasApp(root)
    root.mainloop()