# Acidentes na Dutra — análise regional (Piraí → Guaratinguetá)

Análise exploratória de acidentes na Rodovia Presidente Dutra (BR-116), com foco
no trecho do **Sul do Vale do Paraíba** — 14 municípios cortados pela rodovia,
de **Piraí (RJ)** a **Guaratinguetá (SP)**. É uma região de polo industrial onde
a Dutra mistura moradores em deslocamento local e caminhoneiros em trânsito de
carga; acidentes ali travam a via por longos períodos e afetam a todos.

O objetivo é duplo: **diagnóstico** de causas e padrões dos acidentes e um
**exercício de portfólio** cobrindo o pipeline de dados de ponta a ponta
(coleta → limpeza → SQL → análise → visualização).

## Recorte

Municípios analisados (na ordem da estrada, Rio → São Paulo):

- **RJ:** Piraí, Pinheiral, Volta Redonda, Barra Mansa, Porto Real, Resende, Itatiaia
- **SP:** Queluz, Lavrinhas, Cruzeiro, Cachoeira Paulista, Canas, Lorena, Guaratinguetá

Limite leste em Piraí porque logo depois vem a serra das Araras, que tem outra
dinâmica de tráfego.

## Fontes de dados

Duas fontes públicas, usadas de forma **complementar** (nunca unidas registro a
registro — cada acidente é contado por uma metodologia diferente em cada base):

| Fonte | Papel | O que traz de único |
|-------|-------|---------------------|
| **PRF** (Polícia Rodoviária Federal) | Principal no recorte | `municipio`, `latitude`/`longitude`, `causa_acidente`, condição meteorológica, uso do solo, traçado da via |
| **ANTT** (concessionária RIOSP) | Contexto agregado | Detalhamento por tipo de veículo (automóvel, moto, caminhão, ônibus...) e um nível a mais de gravidade |

Para o recorte regional a PRF é a fonte principal porque só ela tem `municipio` e
coordenadas — a ANTT registra apenas o `km`.

> **Atenção metodológica:** o filtro por `BR-116` sozinho **não** isola a Dutra —
> a BR-116 também inclui a Régis Bittencourt (SP→PR) e o ramal serrano no RJ.
> Por isso o recorte é feito por lista de municípios, não só pela rodovia.

Os arquivos de dados (`data/raw/` e `data/processed/`) **não são versionados**
(ver `.gitignore`). Baixe os CSVs originais em:
[dados abertos da ANTT](https://dados.antt.gov.br) e
[dados abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos).

## Estrutura do projeto

```
Acidentes-Dutra/
├── banco_db.py          # carga: lê os CSVs (ANTT + PRF) e monta o banco SQLite
├── requirements.txt     # dependências Python
├── data/
│   ├── raw/             # CSVs originais (ANTT, PRF) — não versionado
│   └── processed/       # banco acidentes.db e figuras — não versionado
├── Notebooks/
│   ├── analise_regional.ipynb   # EDA do recorte regional (foco atual)
│   └── antt.ipynb               # exploração/limpeza da base ANTT
└── SQL/                 # queries de referência
```

## Como reproduzir

O ambiente é gerenciado com **conda**.

```bash
# 1. criar e ativar o ambiente
conda create -n acidentes-dutra python=3.12
conda activate acidentes-dutra

# 2. instalar as dependências
pip install -r requirements.txt

# 3. baixar os CSVs (ver "Fontes de dados") e colocá-los em data/raw/

# 4. montar o banco SQLite
python banco_db.py

# 5. abrir a análise
jupyter notebook Notebooks/analise_regional.ipynb
```

## Estado atual

- Pipeline de carga pronto (`banco_db.py`): tabelas `acidentes_riosp`,
  `acidentes_novadutra` e `acidentes_prf` no banco `data/processed/acidentes.db`.
- Recorte regional definido e validado (3.001 acidentes na PRF, 2022–2026).
- Em andamento: análise exploratória do recorte (causa, clima, horário, uso do
  solo, tipo de veículo, mapa de pontos críticos).

## Stack

Python (pandas), SQL (SQLite), visualização (matplotlib / seaborn), Jupyter.
