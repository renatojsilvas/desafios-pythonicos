"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s, minimo_numero_de_caracteres = 2, numero_de_caracteres_do_inicio=2, numero_de_caracteres_do_fim=2):
    if tamanho_da_string(s) < minimo_numero_de_caracteres:
        return ''
    return primeiros_caracteres(s, numero_de_caracteres_do_inicio) + \
           ultimos_caracteres(s, numero_de_caracteres_do_fim)

def tamanho_da_string(s):
    return len(s)

def primeiros_caracteres(s, caracteres):
    return s[:caracteres]

def ultimos_caracteres(s, caracteres):
    return s[-caracteres:]

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
