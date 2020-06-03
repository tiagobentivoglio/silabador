import re
import sys

def mensagem_erro():
    print("É necessário inserir uma palavra em português.")


def silabador(palavra):
    r_silabasPT = r"(?:ch|nh|lh|gu|qu|ss|ps|^cu(?=i(?!m))|^mu(?=i)|" \
                  r"[mnzskjhx]|[fpbvtdcçrg][lr]?|[lr])?" \
                  r"(?:" \
                  r"[ieaoíéêáâãóõô][iu][iu]?" \
                  r"|[u(i)?]" \
                  r"|[áãâ][eo]" \
                  r"|[õó][e]" \
                  r"|[ieaouíéêáâãóõôúü]" \
                  r")" \
                  r"(?:(?:" \
                  r"(?:(?:n(?!h)|d|m|t|z|x|p(?![slr])|b(?![rl])|g[?!rl])s?(?![ieaouíéêáâãóõôúü]))" \
                  r"|(?:(?:i$)(?![ieaouíéêáãâóõôúüs]))" \
                  r"|(?:(?:s)(?![ieaouíéêáãâóõôúüs]))" \
                  r"|(?:(?:l)(?![hieaouíéêáãâóõôúü]))" \
                  r"|(?:(?:r)(?![rieaouíéêáâãóõôúü]))" \
                  r"))?"
    return  re.findall(r_silabasPT, palavra.lower())

palavra = input('O que deseja separar em sílabas? ')

acentuadas = ('ã','á', 'â', 'é', 'ê', 'ó', 'ô', 'õ', 'í', 'ú')
mono_atonas = ('o', 'a', 'os', 'as', 'um', 'uns', 'me', 'te', 'se', 'lhe', 'nos', 'vos', 'lhes', 'que', 'com', 'de',
               'em ', 'por', 'sem', 'sob', 'à', 'ao', 'da', 'do', 'na', 'no', 'num', 'nuns', 'e', 'mas', 'nem', 'ou',
               'dom', 'frei', 'seus')

x = silabador(palavra)


def classi_ton():
    if len(x) == 1:
        for i in mono_atonas:
            if i == x[0]:
                return "átona"
        else:
            return "oxítona"
    if len(x) == 2:
        for i in acentuadas:
            if i in x[-1]:
                return "oxítona"
        for i in acentuadas:
            if i in x[-2]:
                return "paroxítona"
        if x[-1][-1] in ['l', 'r', 'x', 'i', 'u']:
            return "oxítona"
        elif x[-1][-1] == 's' and x[-1][-2] not in ['a', 'o', 'e']:
            return "oxítona"
        else:
            return "paroxítona"
    if len(x) >= 3:
        for i in acentuadas:
            if i in x[-1]:
                return "oxítona"
        for i in acentuadas:
            if i in x[-2]:
                return "paroxítona"
        for i in acentuadas:
            if i in x[-3]:
                return "proparoxítona"
        if x[-1][-1] in ['l', 'r', 'x', 'i', 'u']:
            return "oxítona"
        if x[-1][-1] == 's' and x[-1][-2] not in ['a', 'o', 'e']:
            return "oxítona"
        else:
            return "paroxítona"


y = len(silabador(palavra))

def classi_qnt(y):
    if y == 1:
        return "monossílaba"
    elif y == 2:
        return "dissílaba"
    elif y == 3:
        return "trissílaba"
    elif y >= 4:
        return "polissílaba"

if palavra.isalpha():
    print(f'A separação de sílabas da expressão "{palavra}" resultou em: {x}')
    print(f'Número de sílabas: {y} ({classi_qnt(y)})')
    print(f'Tonicidade: {classi_ton()}')
else:
    mensagem_erro()
    sys.exit()
