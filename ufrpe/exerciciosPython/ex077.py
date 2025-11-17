tupla = ('nessa', 'aula', 'vamos', 'aprender', 'olho', 'que', 'sao', 'tuplas', 'elastico', 'como',
         'utilizar', 'elas', 'melhor')
for palavras in tupla:
    if 'a' or 'e' or 'i' or 'o' or 'u' in palavras:
        print(f'Na palavra {palavras.upper():10}temos as vogais: ', end=' ')
        for letras in palavras:
            if letras in 'aeiou':
                print(letras, end=' ')
        print('')





