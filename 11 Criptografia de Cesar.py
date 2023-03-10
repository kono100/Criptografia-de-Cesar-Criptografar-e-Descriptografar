modo = input('Você deseja:\n1 - Criptografar\n2 - Decriptografar\n3 - Sair \n: ')
resultado = ''

if (modo == '1'):
    texto = input('Digite o que deseja Criptografar\n: ')
    
    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i]) + 3)
        print(resultado)
        resultado = ''


if (modo == '2'):
    texto = input('Digite o que deseja Descriptografar: \n')
    
    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i]) - 3)
        print(resultado)
        resultado = ''


if (modo == '3'):
      print("Até mais...")