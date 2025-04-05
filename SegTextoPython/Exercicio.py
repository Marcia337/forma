import os
import nltk
import pickle
from nltk.tokenize import PunktSentenceTokenizer, TreebankWordTokenizer

# Caminho ajustado para o arquivo .pickle
caminho_modelo = "/Users/Marcita/forma/SegTextoPython/nltk_data/tokenizers/portuguese.pickle"

# Verifica se o arquivo existe
if not os.path.exists(caminho_modelo):
    raise FileNotFoundError(f"Modelo não encontrado em: {caminho_modelo}")

# Carrega o modelo Punkt do disco
try:
    with open(caminho_modelo, "rb") as f:
        tokenizer = pickle.load(f)
except Exception as e:
    raise Exception(f"Erro ao carregar o modelo: {str(e)}")

# Texto de exemplo
texto = "Olá! Este é um teste de segmentação. Vamos analisar palavra por palavra?"

# Segmentar em frases com o modelo local
frases = tokenizer.tokenize(texto)
print("Frases segmentadas:")
for i, frase in enumerate(frases, 1):
    print(f"- Frase {i}: {frase}")

# Segmentar cada frase em palavras
print("\nPalavras por frase:")
tokenizer_palavras = TreebankWordTokenizer()
for i, frase in enumerate(frases, 1):
    palavras = tokenizer_palavras.tokenize(frase)
    print(f"- Frase {i}: {palavras}")