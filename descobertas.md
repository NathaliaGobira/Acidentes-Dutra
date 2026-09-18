# Descobertas — acidentes na Dutra (Piraí → Guaratinguetá)

Análise dos dados da PRF, recorte de 14 municípios cortados pela Dutra, de Piraí (RJ) a
Guaratinguetá (SP), **excluída a serra das Araras** (ver notas metodológicas).
Período: **2017–2026** (2026 parcial, até julho).

Cada achado está marcado como **[confirmado]** (sólido nos dados) ou **[a investigar]**
(pista que ainda precisa de mais checagem).

## Base e recorte
- **6.055 acidentes** no recorte (2017–2026); **4.593 com vítimas** (feridas ou fatais).
- Vítimas no período: **368 mortos, 1.177 feridos graves, 5.173 feridos leves**.

## Notas metodológicas (por que a base é o que é)
Três decisões que obrigam a tratar os dados com cuidado:

- **Sub-registro de acidentes sem vítima** — a PRF passou a registrar cada vez menos
  acidentes sem vítima ao longo dos anos (de 574 em 2017 para ~80 em 2025). Por isso a
  base é **acidentes com vítimas**, comparáveis ao longo do tempo. [confirmado]
- **Mudança na taxonomia de causa em 2021** — as categorias de `causa_acidente` mudaram
  (amplas → específicas). A análise de **causa** fica restrita a **2021–2026**. [confirmado]
- **Serra das Araras excluída** — a descida da Dutra em Piraí (km < 233) foi removida do
  recorte. É uma dinâmica de serra (curvas, freio, tombamento), diferente do foco do
  trabalho (trecho urbano/planalto onde o morador cruza a via). Eram ~640 acidentes.
  [confirmado]

## Panorama temporal
- **Efeito pandemia visível**: acidentes com vítimas caem até 2020 (vale) e se recuperam
  até 2024–25. A queda do *total* (com sem-vítima) é enganosa — é sub-registro. [confirmado]
- **Mortes não caíram na pandemia**: mesmo com menos acidentes em 2020, o número de mortos
  se manteve. Sugere acidentes mais letais (hipótese: estrada vazia → mais velocidade).
  [a investigar]
- **2026 é um ano ruim para mortes**: de janeiro a julho, 28 mortos — contra 16 no mesmo
  período de 2025 e 15 em 2024. O ano deve fechar como o pior dos recentes. [a investigar]

## Causa
- **Fator humano domina**: das causas (2021–2026, com vítimas), **76,9% são humanas**
  (atenção/reação/velocidade/álcool), contra 9,1% via/ambiente, 8,4% veículo e 5,6% clima.
  As duas maiores são "reação tardia" e "ausência de reação" do condutor. [confirmado]

## Clima
- **Clima quase não influencia a gravidade**: associação clima × acidente fatal é
  desprezível (Cramér's V = 0,055; p = 0,009 — significativo, mas irrelevante em
  magnitude). [confirmado]
- **Chuva é menos letal que tempo seco**: 6,0 mortos por 100 acidentes na chuva contra
  8,8 em céu claro. Provável: na chuva se dirige mais devagar. Reforça que o vilão é a
  velocidade/comportamento, não o clima. [a investigar]

## Quando
- **Fim de semana concentra**: domingo (791) e sábado (751) lideram; meio de semana é
  menor (terça, 571, é o vale). [confirmado]
- **O período do dia não muda com o dia da semana**: todo dia tem ~50% dos acidentes em
  pleno dia e ~37% em plena noite. A ideia de "cada dia tem seu horário" não se confirma.
  [confirmado]

## Pedestre e uso do solo (a hipótese do morador)
- **Trecho urbano tem mais atropelamentos**: 9,6% dos acidentes urbanos são atropelamento
  de pedestre, contra 6,2% nos rurais. [confirmado]
- **Atropelamento é o que mais mata**: 44,5 mortos por 100 acidentes, contra 5,1 nos
  demais tipos. Os atropelamentos são só ~7% dos acidentes, mas respondem por **~40% de
  todas as mortes**. O pedestre é a vítima mais vulnerável — valida a preocupação com o
  morador que cruza a via. [confirmado]

## Geografia (pontos críticos)
- **Os acidentes concentram nas cidades maiores**: os km com mais acidentes ficam em
  Guaratinguetá (SP km 58–65), Lorena (SP km 51–56), Resende (RJ km 305–311) e Barra
  Mansa (RJ km 269–279). Coerente com o achado urbano. [confirmado]
- Lembrete metodológico: o km **zera na divisa RJ/SP** — sempre analisar por UF + km.
  [confirmado]

## Ainda por fazer
- **Tipo de veículo** (dados da ANTT/RIOSP): testar a outra metade da hipótese — morador
  (carro/moto) × caminhoneiro (caminhão/carga). A ANTT detalha veículo, a PRF não.
- **Taxa por volume de tráfego (VMD)**: sem ela, "trecho com mais acidentes" mistura
  perigo com exposição. Fonte futura (concessionária/DNIT).
- **Refinar o corte da serra**: o km 233 é aproximado; se houver um marco melhor do fim
  da subida, ajustar.
