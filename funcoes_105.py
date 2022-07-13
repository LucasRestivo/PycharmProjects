def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos, aceita várias
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r


resp = notas(5.5, 10, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
