import re

texto_paragrafos = '''Este é o primeiro parágrafo.

Este é o segundo parágrafo, com mais texto.

O terceiro termina aqui.'''


texto = "Olá! Este é um teste de segmentação. Vamos analisar palavra por palavra?"

# Parágrafos
paragrafos = texto_paragrafos.strip().split('\n\n')
print(" Parágrafos:")
for p in paragrafos:
    print("-", p)

# Frases com regex
frases_regex = re.split(r'(?<=[.!?]) +', texto)
print("\n Frases com regex:", frases_regex)


