import pyperclip

def converter_espacos_para_pontos(texto):
    # Substituir todos os espaços por pontos
    texto_convertido = texto.replace(' ', '.')
    return texto_convertido

def converter_pontos_para_espacos(texto):
    # Substituir todos os pontos por espaços
    texto_convertido = texto.replace('.', ' ')
    return texto_convertido

# Obter entrada do usuário
tipo_conversao = input("Escolha o tipo de conversão (1 para Espaços para Pontos, 2 para Pontos para Espaços): ")
texto_original = input("Digite o texto: ")

# Aplicar a conversão conforme escolha do usuário
if tipo_conversao == '1':
    texto_convertido = converter_espacos_para_pontos(texto_original)
    print(f"Texto Original:\n{texto_original}\n\nTexto Convertido:\n{texto_convertido}")
elif tipo_conversao == '2':
    texto_convertido = converter_pontos_para_espacos(texto_original)
    print(f"Texto Original:\n{texto_original}\n\nTexto Convertido:\n{texto_convertido}")
else:
    print("Escolha inválida. Por favor, escolha 1 ou 2 para o tipo de conversão.")

# Copiar o resultado para a área de transferência
pyperclip.copy(texto_convertido)
print("Resultado copiado para a área de transferência.")
