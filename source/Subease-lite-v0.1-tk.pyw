import tkinter as tk
from tkinter import Entry, Label, Button, Text
import pyperclip

def converter_espacos_para_pontos():
    # Recupera o texto do widget de entrada
    texto_original = entrada_texto.get()

    # Realiza a substituição de espaços por pontos
    texto_convertido = texto_original.replace('.', ' ')

    # Atualiza o texto no widget de resultado
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, f"Título Original:\n{texto_original}\n\nTítulo Convertido:\n{texto_convertido}")

    # Copia o texto convertido para a área de transferência
    pyperclip.copy(texto_convertido)

    # Configura a mensagem de status
    status_label.config(text="Resultado copiado para a área de transferência.\nAgora é só colar na busca de um site de legendas\ne encontrar a sua legenda!", fg='green', justify='left')

# Configuração da janela
window = tk.Tk()
window.title("SubEase Lite v0.1 - Otimizador de busca por legendas by @alanmugiwara")
window.geometry("560x450")

# Rótulo e campo de entrada
Label(window, text="Digite ou cole o título do seu arquivo:", anchor='w').grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
entrada_texto = Entry(window, width=50)
entrada_texto.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')

# Botão de execução
btn_executar = Button(window, text="Converter", command=converter_espacos_para_pontos)
btn_executar.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

# Resultado
resultado_texto = Text(window, height=10, width=50)
resultado_texto.grid(row=3, column=0, padx=10, pady=(10, 0), sticky='w')

# Status
status_label = Label(window, text="", anchor='w', fg="black")
status_label.grid(row=4, column=0, padx=10, pady=(0, 10), sticky='w')

# Texto informativo
texto_informativo = "SubEase - Ponha o título do seu arquivo de vídeo e com um clique\no SubEase já deixa o título sem espaços. Ele já copia o resultado.\nÉ só você colar no site de busca de legendas da sua preferência. \n\nRIP legendas.tv 🪦"
Label(window, text=texto_informativo, anchor='w', fg="black", justify='left').grid(row=5, column=0, padx=10, pady=(0, 10), sticky='w')

# Inicia o loop da aplicação
window.mainloop()
