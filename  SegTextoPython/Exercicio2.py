import spacy
nlp = spacy.load("pt_core_news_sm")

texto = "Olá! Este é um teste de segmentação. Vamos analisar palavra por palavra?"
doc = nlp(texto)

print(" Frases (spaCy):")
for sent in doc.sents:
    print("-", sent.text)

print("\n Palavras (spaCy):")
for token in doc:
    print(token.text, end=" | ")