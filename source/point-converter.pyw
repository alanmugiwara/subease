import tkinter as tk
from tkinter import Entry, Label, Button, Text
import pyperclip

def converter_espacos_para_pontos():
    texto_original = entrada_texto.get()
    texto_convertido = texto_original.replace(' ', '.')
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, f"Texto Original:\n{texto_original}\n\nTexto Convertido:\n{texto_convertido}")
    pyperclip.copy(texto_convertido)
    status_label.config(text="Resultado copiado para a área de transferência.")

def converter_pontos_para_espacos():
    texto_original = entrada_texto.get()
    texto_convertido = texto_original.replace('.', ' ')
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, f"Texto Original:\n{texto_original}\n\nTexto Convertido:\n{texto_convertido}")
    pyperclip.copy(texto_convertido)
    status_label.config(text="Resultado copiado para a área de transferência.")

# Configuração da janela
window = tk.Tk()
window.title("Conversor de Espaços e Pontos")
window.geometry("500x400")

# Rótulo e campo de entrada
Label(window, text="Digite o texto:").grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
entrada_texto = Entry(window, width=50)
entrada_texto.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')

# Botões de conversão
btn_espacos_para_pontos = Button(window, text="Espaços para Pontos", command=converter_espacos_para_pontos)
btn_espacos_para_pontos.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

btn_pontos_para_espacos = Button(window, text="Pontos para Espaços", command=converter_pontos_para_espacos)
btn_pontos_para_espacos.grid(row=3, column=0, padx=10, pady=(0, 10), sticky='w')

# Resultado
resultado_texto = Text(window, height=10, width=50)
resultado_texto.grid(row=4, column=0, padx=10, pady=(10, 0), sticky='w')

# Status
status_label = Label(window, text="", anchor='w', fg="green")
status_label.grid(row=5, column=0, padx=10, pady=(0, 10), sticky='w')

# Inicia o loop da aplicação
window.mainloop()
