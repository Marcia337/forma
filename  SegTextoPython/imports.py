import nltk
from nltk.tokenize import PunktSentenceTokenizer, TreebankWordTokenizer

# Baixa o modelo padrão 'punkt' (necessário apenas na primeira execução)
nltk.download('punkt')

# Cria o tokenizador de sentenças usando o modelo padrão
tokenizer = PunktSentenceTokenizer()

# Texto de exemplo
texto = "Olá! Este é um teste de segmentação. Vamos analisar palavra por palavra?"

# Segmentar em frases
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