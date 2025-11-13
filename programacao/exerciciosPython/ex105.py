def notas(*nts, situacao=False):
    """
    -> Função que armazena as notas de um aluno em um dicionário.
    :param nts: Esse parâmetro pode receber diversos valores, os quais serão as notas;
    :param situacao: ativando o parâmetro 'situacao' para True: (situacao=True), irá ser adicionado no dicionário um
                     elemento de aproveitamento escolar.
    :return: retornará o dicionário.
    """
    bancodedados = {'total': len(nts), 'maior': max(nts),
                    'menor': min(nts), 'média': sum(nts)/len(nts)}
    if situacao is True and bancodedados['média'] >= 7:
        bancodedados['situação'] = 'Boa'
    elif situacao is True and 7 > bancodedados['média'] >= 5:
        bancodedados['situação'] = 'Razoável'
    elif situacao is True and bancodedados['média'] < 5:
        bancodedados['situação'] = 'Ruim'
    return bancodedados


analiseNotas = notas(5.5, 2.5, 9, 8.5, situacao=True)
print(analiseNotas)

