texto = input("Por favor, insira uma string: ")
deslocamento = int(input("Por favor, digite o deslocamento: "))

textoCifrado = ""

for char in texto:
    #Se o caracter é uma letra
    if char.isalpha():
        codigo = ord(char)
        codigo += deslocamento
        if char.isupper():
            if codigo > ord('Z'):
                codigo -= 26
            elif codigo < ord('A'):
                codigo += 26
        else:
            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26
        textoCifrado += chr(codigo)
    else:
        #Se o caracter não é uma letra
        textoCifrado += char


print("Texto cifrado: ", textoCifrado)
