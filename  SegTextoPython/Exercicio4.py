# segmentador_nltk.py
import os
import nltk
import pickle
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
import pandas as pd

# Caminho local para o ficheiro .pickle - com o seu caminho
caminho_modelo = "/Users/Marcita/forma/SegTextoPython/nltk_data/tokenizers/portuguese.pickle"

# Verifica se o ficheiro existe
if not os.path.exists(caminho_modelo):
    raise FileNotFoundError(f"Modelo não encontrado em: {caminho_modelo}")

# Carrega o modelo Punkt do disco
with open(caminho_modelo, "rb") as f:
    tokenizer = pickle.load(f)

# Exemplo de leitura
with open("amostra.txt", "w", encoding="utf-8") as f:
    f.write("Hoje está sol. Amanhã talvez chova. O tempo é imprevisível.")

with open("amostra.txt", "r", encoding="utf-8") as f:
    texto_lido = f.read()
    frases_lidas = tokenizer.tokenize(texto_lido)

# Exportar
df = pd.DataFrame(frases_lidas, columns=["Frase"])
df.to_csv("frases_exportadas.csv", index=False, encoding="utf-8")
print("✅ Exportado para 'frases_exportadas.csv'")
