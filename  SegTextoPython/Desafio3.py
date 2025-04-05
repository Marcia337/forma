import os
import pickle
import pandas as pd
import nltk
from nltk.tokenize import TreebankWordTokenizer
from tkinter import filedialog, messagebox

# Baixar o pacote necessário
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

# Função para segmentar o texto de cada linha
def segmentar_frases_csv():
    # Escolher o arquivo CSV de entrada
    arquivo_entrada = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if not arquivo_entrada:
        return
    
    # Ler o arquivo CSV
    df = pd.read_csv(arquivo_entrada)

    # Verificar se existe uma coluna 'texto'
    if 'texto' not in df.columns:
        messagebox.showerror("Erro", "Não foi encontrada a coluna 'texto' no arquivo CSV.")
        return

    # Lista para armazenar as frases
    frases_resultado = []

    # Processar cada linha de texto
    for index, row in df.iterrows():
        texto = row['texto']
        frases = tokenizer_frases.tokenize(texto)
        
        # Adicionar cada frase à lista
        for frase in frases:
            frases_resultado.append([frase])

    # Salvar o resultado em um novo arquivo CSV
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df_resultado = pd.DataFrame(frases_resultado, columns=["Frase"])
        df_resultado.to_csv(file_path, index=False, encoding="utf-8")
        messagebox.showinfo("Sucesso", f"Frases segmentadas salvas em: {file_path}")

# Criar interface gráfica
import tkinter as tk

# Função para criar a interface
def criar_interface():
    # Criar janela
    janela = tk.Tk()
    janela.title("Segmentação de Texto em CSV")
    janela.configure(bg="#121212")
    janela.geometry("400x200")

    # Estilo dos botões
    button_style = {
        "font": ("Segoe UI", 12, "bold"),
        "bg": "#2196F3",
        "fg": "white",
        "activebackground": "#1976D2",
        "relief": "flat",
        "bd": 0,
        "highlightthickness": 0,
        "padx": 10,
        "pady": 10
    }

    # Título
    titulo = tk.Label(janela, text="Segmentação de Frases de CSV", font=("Segoe UI", 16, "bold"), bg="#121212", fg="white", pady=20)
    titulo.grid(row=0, column=0, columnspan=2)

    # Botão para segmentar CSV
    tk.Button(janela, text="Segmentar CSV", command=segmentar_frases_csv, **button_style).grid(row=1, column=0, columnspan=2, pady=10)

    # Iniciar a interface gráfica
    janela.mainloop()

# Iniciar a interface
criar_interface()
