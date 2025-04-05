# segmentador_nltk.py
import os
import nltk
import pickle
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer

# Caminho local para o ficheiro .pickle - ajustado para o macOS
caminho_modelo = r"/Users/Marcita/forma/SegTextoPython/nltk_data/tokenizers/portuguese.pickle"

# Verifica se o ficheiro existe
if not os.path.exists(caminho_modelo):
    raise FileNotFoundError(f"Modelo não encontrado em: {caminho_modelo}")

# Carrega o modelo Punkt do disco
with open(caminho_modelo, "rb") as f:
    tokenizer_frases = pickle.load(f)

# Tokenizador de palavras que não depende de punkt
tokenizador_palavras = TreebankWordTokenizer()

# Texto de exemplo
texto = "O Python é ótimo. É fácil de aprender. Vamos começar?"

# Segmentação de frases
frases = tokenizer_frases.tokenize(texto)

# Segmentação de palavras
palavras = tokenizador_palavras.tokenize(texto)

# Escrever e ler de um arquivo de exemplo
with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write("Esta é a primeira. E esta é a segunda frase. Aqui vem a terceira!")

with open("exemplo.txt", "r", encoding="utf-8") as f:
    texto_f = f.read()

# Segmentação de frases no texto lido
frases_lidas = tokenizer_frases.tokenize(texto_f)

# Imprimir as frases e o número de palavras
for i, frase in enumerate(frases_lidas, 1):
    palavras_na_frase = tokenizador_palavras.tokenize(frase)
    print(f"Frase {i}: {frase} ({len(palavras_na_frase)} palavras)")
