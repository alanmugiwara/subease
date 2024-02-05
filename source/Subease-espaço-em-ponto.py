def converter_pontos_para_espacos(texto):
    # Substituir todos os pontos por espaços
    texto_convertido = texto.replace('.', ' ')
    return texto_convertido

# Obter entrada do usuário
texto_original = input("Digite o texto com pontos: ")

# Chamar a função e exibir o resultado
texto_convertido = converter_pontos_para_espacos(texto_original)
print(f"Texto Original:\n{texto_original}\n\nTexto Convertido:\n{texto_convertido}")