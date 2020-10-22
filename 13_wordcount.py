"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from collections import Counter


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        processa(filename, print_words)
    elif option == '--topcount':
        processa(filename, print_top)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


def processa(filename, metodo):
    # lê o conteúdo do arquivo -> entrada
    conteudo_do_arquivo = le_o_arquivo(filename)
    # processa o algoritmo -> processamento
    resultado = metodo(conteudo_do_arquivo)
    # imprime -> saída
    imprime_resultado(resultado)


def le_o_arquivo(filename):
    f = open(filename)
    linhas = []
    while True:
        linha = f.readline()
        if not linha:
            break
        linhas.append(linha.split())
    f.close()
    converte_listas_para_lista = lambda t: [item.lower() for sublist in t for item in sublist]
    return converte_listas_para_lista(linhas)


def imprime_resultado(resultado):
    for letra, quantidade in resultado:
        print(letra, quantidade)


def print_words(conteudo_do_arquivo):
    return sorted(list(dict((i, conteudo_do_arquivo.count(i)) for i in conteudo_do_arquivo).items()))


def print_top(conteudo_do_arquivo, quantidade_de_palavras_mais_comuns=20):
    return Counter(conteudo_do_arquivo).most_common(quantidade_de_palavras_mais_comuns)


if __name__ == '__main__':
    main()
