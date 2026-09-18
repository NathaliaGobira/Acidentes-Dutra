import pandas as pd   # para ler os CSVs
import sqlite3        # para criar e escrever no banco
from pathlib import Path

BASE = Path(__file__).parent

CSV_RIOSP   = BASE / 'data/raw/ANTT/antt_riosp.csv'
CSV_NOVADUTRA = BASE / 'data/raw/ANTT/antt_novadutra.csv'
BANCO       = BASE / 'data/processed/acidentes.db'

ARQUIVOS_PRF = [
        BASE / 'data/raw/PRF/prf_17.csv',
        BASE / 'data/raw/PRF/prf_18.csv',
        BASE / 'data/raw/PRF/prf_19.csv',
        BASE / 'data/raw/PRF/prf_20.csv',
        BASE / 'data/raw/PRF/prf_21.csv',
        BASE / 'data/raw/PRF/prf_22.csv',
        BASE / 'data/raw/PRF/prf_23.csv',
        BASE / 'data/raw/PRF/prf_24.csv',
        BASE / 'data/raw/PRF/prf_25.csv',
        BASE / 'data/raw/PRF/prf_26.csv',
]
    
# Padronizando os dados da RIOSP

df_riosp = pd.read_csv(
    CSV_RIOSP,
    sep=';',           # separador é ponto e vírgula, não vírgula
    encoding='latin-1',  # encoding correto para preservar acentos
)

df_riosp.columns = (df_riosp.columns.str.lower().str.strip())

df_riosp['km'] = (df_riosp['km'].str.replace(',', '.').astype(float))

print(f"  {len(df_riosp)} linhas lidas.")

# Padronizando os dados da NovaDutra

df_novadutra = pd.read_csv(
    CSV_NOVADUTRA,
    sep=';',           # separador é ponto e vírgula, não vírgula
    encoding='latin-1',  # encoding correto para preservar acentos
)

df_novadutra.columns = (df_novadutra.columns.str.lower().str.strip())

df_novadutra['km'] = (df_novadutra['km'].str.replace(',', '.').astype(float))

print(f"  {len(df_novadutra)} linhas lidas.")

print("Lendo PRF (5 arquivos)...")

pedacos = []
for arquivo in ARQUIVOS_PRF:
    df = pd.read_csv(
        arquivo,
        sep=';',
        encoding = 'latin-1'
    )

    pedacos.append(df)
    print(f"  {arquivo.name}: {len(df)} linhas")

df_prf = pd.concat(pedacos, ignore_index=True)

df_prf.columns = df_prf.columns.str.lower().str.strip()

df_prf['km'] = (df_prf['km'].str.replace(',', '.').astype(float))

#Filtrando as rodovias e estados

df_prf = df_prf[
    (df_prf['br'] == 116) &
    (df_prf['uf'].isin(['RJ', 'SP']))
]

print(f"  Total após filtro BR-116/RJ-SP: {len(df_prf)} linhas.")
print(f"\nGravando em {BANCO}...")
conn = sqlite3.connect(BANCO)  # abre (ou cria) o banco

df_riosp.to_sql(
    'acidentes_riosp',   # nome da tabela dentro do banco
    conn,
    if_exists='replace', # se já existir, apaga e recria (idempotente)
    index=False,         # não salva o índice do pandas como coluna
)

print("  acidentes_riosp ✓")

df_novadutra.to_sql(
    'acidentes_novadutra',   # nome da tabela dentro do banco
    conn,
    if_exists='replace', # se já existir, apaga e recria (idempotente)
    index=False,         # não salva o índice do pandas como coluna
)

print("  acidentes_novadutra✓")

df_prf.to_sql(
    'acidentes_prf',   # nome da tabela dentro do banco
    conn,
    if_exists='replace', # se já existir, apaga e recria (idempotente)
    index=False,         # não salva o índice do pandas como coluna
)
print("  acidentes_prf ✓")
conn.close()  # fecha a conexão
print("\nPronto! Banco criado com sucesso.")