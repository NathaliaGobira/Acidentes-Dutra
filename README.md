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
registro — cada base conta os acidentes por uma metodologia diferente):

| Fonte | Papel | O que traz de único |
|-------|-------|---------------------|
| **PRF** | Principal no recorte | `municipio`, latitude/longitude, causa do acidente, condição meteorológica, uso do solo, traçado da via |
| **ANTT** (RIOSP) | Contexto agregado | Detalhamento por tipo de veículo (automóvel, moto, caminhão, ônibus...) e um nível a mais de gravidade |

Para o recorte regional a PRF é a fonte principal porque só ela tem `municipio` e
coordenadas — a ANTT registra apenas o `km`.

| Dataset | Período | Link |
|---|---|---|
| ANTT — Demonstrativo de Acidentes (RIOSP) | mar/2022 – jul/2026 | [CSV](https://dados.antt.gov.br/dataset/ef0171a8-f0df-4817-a4ed-b4ff94d87194/resource/0d180b06-fd26-4ecc-a77c-5bbb50c486a6/download/demostrativo_acidentes_riosp.csv) |
| ANTT — Acidentes por km (NOVADUTRA) | jan/2010 – abr/2022 | [CSV](https://dados.antt.gov.br/dataset/8a57b663-2302-405a-bf5a-cbece12c13d1/resource/3c29b0ac-d5c9-466c-810b-19d4c3c8ad52/download/demostrativo_acidentes_novadutra.csv) |
| PRF — Acidentes por ano | 2022 – 2026 | [gov.br/prf](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes) |

> **Atenção metodológica:** o filtro por `BR-116` sozinho **não** isola a Dutra —
> a BR-116 também inclui a Régis Bittencourt (SP→PR) e o ramal serrano no RJ.
> Por isso o recorte é feito por lista de municípios, não só pela rodovia.

Os CSVs (`data/raw/`) e o banco (`data/processed/`) **não são versionados**
(ver `.gitignore`). Baixe os arquivos nas fontes acima e coloque em `data/raw/`
conforme a estrutura abaixo.

## Estrutura do projeto

```
Acidentes-Dutra/
├── banco_db.py          # carga: lê os CSVs (ANTT + PRF) e monta o banco SQLite
├── requirements.txt     # dependências Python
├── data/
│   ├── raw/             # CSVs originais — não versionado
│   │   ├── ANTT/        # antt_riosp.csv, antt_novadutra.csv
│   │   └── PRF/         # prf_22.csv ... prf_26.csv
│   └── processed/       # banco acidentes.db e figuras — não versionado
├── Notebooks/
│   ├── analise_regional.ipynb   # EDA do recorte regional (foco atual)
│   └── antt.ipynb               # exploração/limpeza da base ANTT
└── SQL/                 # queries de referência (pastas ANTT/ e PRF/)
```

## Como reproduzir

O ambiente é gerenciado com **conda**.

```bash
# 1. criar e ativar o ambiente
conda create -n dutra python=3.11
conda activate dutra

# 2. instalar as dependências
pip install -r requirements.txt

# 3. baixar os CSVs (ver "Fontes de dados") e colocá-los em data/raw/

# 4. montar o banco SQLite
python banco_db.py

# 5. abrir a análise
jupyter notebook Notebooks/analise_regional.ipynb
```

## Tabelas no banco

| Tabela | Fonte | Descrição |
|---|---|---|
| `acidentes_prf` | PRF | Acidentes da BR-116/RJ-SP; **fonte principal** do recorte regional (tem município, coordenadas, causa e clima) |
| `acidentes_riosp` | ANTT | Concessionária RIOSP (a partir de mar/2022); contexto agregado de tipo de veículo |
| `acidentes_novadutra` | ANTT | Histórico NOVADUTRA (até 2022); uso pontual/exploratório |

A PRF e a ANTT são comparadas sempre de forma agregada — nunca em join linha a
linha, porque cada base registra o mesmo acidente por uma metodologia diferente.

## Estado atual

- Pipeline de carga pronto (`banco_db.py`).
- Recorte regional definido e validado (3.001 acidentes na PRF, 2022–2026).
- Em andamento: análise exploratória do recorte (causa, clima, horário, uso do
  solo, tipo de veículo, mapa de pontos críticos).

## Stack

Python (pandas), SQL (SQLite), visualização (matplotlib / seaborn), Jupyter.
