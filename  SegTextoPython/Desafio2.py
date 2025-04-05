# Desafio 2 – Filtrar frases curtas
# Cria um script que: - Segmenta um texto em frases. - Ignora frases com menos de 4 palavras.
# - Mostra apenas as frases restantes.

import os
import pickle
import nltk
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from nltk.tokenize import TreebankWordTokenizer

import nltk
nltk.download('punkt')


# Caminho para o modelo Punkt local
caminho_modelo = "/Users/Marcita/forma/SegTextoPython/nltk_data/tokenizers/portuguese.pickle"

# Verificar existência do modelo
if not os.path.exists(caminho_modelo):
    messagebox.showerror("Erro", f"Modelo Punkt não encontrado em:\n{caminho_modelo}")
    exit()

# Carregar modelo Punkt
with open(caminho_modelo, "rb") as f:
    tokenizer_frases = pickle.load(f)

# Tokenizador de palavras (não depende do punkt)
tokenizador_palavras = TreebankWordTokenizer()

# Funções
def segmentar_texto():
    texto = entrada.get("1.0", "end-1c")
    frases = tokenizer_frases.tokenize(texto)
    saida.delete("1.0", "end")
    for f in frases:
        saida.insert("end", f + "\n")

def contar_palavras():
    texto = entrada.get("1.0", "end-1c")
    palavras = tokenizador_palavras.tokenize(texto)
    saida.delete("1.0", "end")
    saida.insert("end", f"Total de palavras: {len(palavras)}")

def filtrar_frases_curtas():
    texto = entrada.get("1.0", "end-1c")
    frases = tokenizer_frases.tokenize(texto)
    
    # Filtrar frases com menos de 4 palavras
    frases_filtradas = [frase for frase in frases if len(tokenizador_palavras.tokenize(frase)) >= 4]
    
    # Exibir as frases filtradas
    saida.delete("1.0", "end")
    if frases_filtradas:
        for frase in frases_filtradas:
            saida.insert("end", frase + "\n")
    else:
        saida.insert("end", "Não há frases com 4 ou mais palavras.")

def exportar_csv():
    texto = entrada.get("1.0", "end-1c")
    frases = tokenizer_frases.tokenize(texto)
    df = pd.DataFrame(frases, columns=["Frase"])
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False, encoding="utf-8")
        saida.insert("end", f"\nExportado para: {file_path}")

# Criar janela
janela = tk.Tk()
janela.title("Segmentador de Texto em Português")
janela.configure(bg="#121212")
janela.geometry("900x700")
janela.columnconfigure((0, 1, 2), weight=1)
janela.rowconfigure((2, 5), weight=1)

# Estilo dos botões
button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": "#2196F3",
    "fg": "red",
    "activebackground": "#1976D2",
    "relief": "flat",
    "bd": 0,
    "highlightthickness": 0,
    "padx": 10,
    "pady": 6
}

# Título
titulo = tk.Label(janela, text="Segmentador de Texto", font=("Segoe UI", 16, "bold"), bg="#121212", fg="white", pady=10)
titulo.grid(row=0, column=0, columnspan=3)

# Texto de entrada
tk.Label(janela, text="Texto de entrada:", bg="#121212", fg="white", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w", padx=10)
entrada = tk.Text(janela, height=10, wrap="word", font=("Consolas", 11), bg="#1e1e1e", fg="white", insertbackground="white", relief="flat", borderwidth=10)
entrada.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

# Botões
frame_botoes = tk.Frame(janela, bg="#121212")
frame_botoes.grid(row=3, column=0, columnspan=3, pady=15)
tk.Button(frame_botoes, text=" Segmentar Frases", command=segmentar_texto, **button_style).pack(side="left", padx=10)
tk.Button(frame_botoes, text=" Contar Palavras", command=contar_palavras, **button_style).pack(side="left", padx=10)
tk.Button(frame_botoes, text=" Filtrar Frases Curtas", command=filtrar_frases_curtas, **button_style).pack(side="left", padx=10)
tk.Button(frame_botoes, text=" Exportar para CSV", command=exportar_csv, **button_style).pack(side="left", padx=10)

# Resultado
tk.Label(janela, text="Resultado:", bg="#121212", fg="white", font=("Segoe UI", 10, "bold")).grid(row=4, column=0, sticky="w", padx=10)
saida = tk.Text(janela, height=12, wrap="word", font=("Consolas", 11), bg="#1e1e1e", fg="white", insertbackground="white", relief="flat", borderwidth=10)
saida.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

# Iniciar a interface gráfica
janela.mainloop()
