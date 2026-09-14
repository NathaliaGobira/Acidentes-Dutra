# Acidentes na Dutra

Análise de acidentes na Rodovia Presidente Dutra (BR-116) a partir de dados públicos da ANTT e da PRF.

O projeto combina duas fontes complementares: a ANTT fornece dados detalhados por ocorrência (tipo de acidente, veículos envolvidos, vítimas, km); a PRF complementa com informações que a ANTT não tem, como causa do acidente e condição climática.

---

## Motivação

A Dutra é uma das rodovias mais movimentadas do país, conectando São Paulo ao Rio de Janeiro. Os dados são públicos, reais e localmente relevantes — o que torna este projeto um bom exercício de análise aplicada, com possibilidade de gerar insights de utilidade pública.

---

## Fontes de dados

| Fonte | Dataset | Período | Link |
|---|---|---|---|
| ANTT | Demonstrativo de Acidentes — RIOSP | mar/2022 – jul/2026 | [CSV](https://dados.antt.gov.br/dataset/ef0171a8-f0df-4817-a4ed-b4ff94d87194/resource/0d180b06-fd26-4ecc-a77c-5bbb50c486a6/download/demostrativo_acidentes_riosp.csv) |
| ANTT | Acidentes por km — NOVADUTRA | jan/2010 – abr/2022 | [CSV](https://dados.antt.gov.br/dataset/8a57b663-2302-405a-bf5a-cbece12c13d1/resource/3c29b0ac-d5c9-466c-810b-19d4c3c8ad52/download/demostrativo_acidentes_novadutra.csv) |
| PRF | Acidentes por ano | 2022 – 2026 | [gov.br/prf](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes) |

Os CSVs não estão versionados neste repositório. Baixe-os diretamente nas fontes acima e coloque em `data/raw/` conforme a estrutura descrita abaixo.

---

## Estrutura do projeto

```
Acidentes-Dutra/
│
├── data/
│   ├── raw/
│   │   ├── ANTT/
│   │   │   ├── antt_riosp.csv
│   │   │   └── antt_novadutra.csv
│   │   └── PRF/
│   │       ├── prf_22.csv
│   │       ├── prf_23.csv
│   │       ├── prf_24.csv
│   │       ├── prf_25.csv
│   │       └── prf_26.csv
│   └── processed/
│       └── acidentes.db       ← banco SQLite gerado pelo banco_db.py
│
├── Notebooks/
│   └── antt.ipynb             ← exploração e análise
│
├── SQL/
│   ├── ANTT/
│   │   ├── riosp.sql
│   │   └── NovaDutra.sql
│   └── PRF/
│       ├── prf_union.sql
│       └── prf_limpo.sql
│
├── banco_db.py                ← script principal de carga e limpeza
├── requirements.txt
└── .gitignore
```

---

## Como reproduzir o banco de dados

**1. Crie o ambiente Python:**

```bash
conda create -n dutra python=3.11
conda activate dutra
pip install -r requirements.txt
```

**2. Baixe os CSVs** nas fontes listadas acima e coloque nas pastas correspondentes em `data/raw/`.

**3. Rode o script de carga:**

```bash
python banco_db.py
```

O script lê os CSVs, corrige encoding e tipos de dados, filtra a PRF para BR-116/RJ-SP e grava tudo no banco `data/processed/acidentes.db`.

---

## Tabelas no banco

| Tabela | Fonte | Linhas | Descrição |
|---|---|---|---|
| `acidentes_riosp` | ANTT | 36.716 | Dados brutos da concessionária RIOSP — fonte principal da análise |
| `acidentes_novadutra` | ANTT | 115.888 | Dados históricos da NOVADUTRA (até 2022) — uso pontual/exploratório |
| `acidentes_prf` | PRF | ~22.800 | Acidentes da BR-116/RJ-SP filtrados dos 5 CSVs anuais da PRF |

A tabela `acidentes_riosp` é a fonte principal. A PRF é usada como contexto complementar (causa, clima) — nunca em join linha a linha com a RIOSP, sempre em comparações agregadas.

---

## Stack

- **Python** — pandas, matplotlib, seaborn
- **Banco** — SQLite (`acidentes.db`)
- **Ambiente** — conda (`dutra`)
- **Notebooks** — Jupyter

---

## Estado atual

O pipeline de carga está completo. Os dados estão no banco, limpos e prontos para análise.

A próxima etapa é a análise exploratória (EDA):
- Distribuição de acidentes por faixa de km
- Padrões por dia da semana e horário
- Tipos de acidente mais comuns e sua relação com gravidade
- Contexto de causa e clima via dados da PRF

---

## Fora do escopo (por ora)

- Outros trechos da BR-116 fora do eixo RJ-SP
- Comparação com outras rodovias
- Modelos preditivos
