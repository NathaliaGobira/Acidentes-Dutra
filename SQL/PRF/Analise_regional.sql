WITH tb_regional AS (

    SELECT * 
    FROM acidentes_prf
    
    WHERE municipio IN ('BARRA MANSA',
                        'ITATIAIA', 
                        'PINHEIRAL', 
                        'PIRAI', 
                        'PORTO REAL', 
                        'RESENDE', 
                        'VOLTA REDONDA',
                        'GUARATINGUETA',
                        'LAVRINHAS',
                        'CRUZEIRO',
                        'CACHOEIRA PAULISTA',
                        'CANAS',
                        'LORENA',
                        'QUELUZ')

),

tb_contagem_sentido AS (

    SELECT count(id),
           sentido_via 
    FROM tb_regional
    GROUP BY sentido_via
),

tb_faseDia AS (

    SELECT count(id),
           fase_dia 
    FROM tb_regional
    GROUP BY fase_dia
),

tb_Dia AS (

    SELECT count(id),
           dia_semana 
    FROM tb_regional
    GROUP BY dia_semana
),

tb_acidente_km AS (

    SELECT count(id),
           municipio, 
           km  
    FROM tb_regional
    GROUP BY km, municipio
    ORDER BY count(id) DESC
    LIMIT 10
),

tb_causa_acidente AS (

    SELECT count(id),
           causa_acidente
    FROM tb_regional 
    GROUP BY causa_acidente
    ORDER BY count(id) DESC
)

SELECT count(id),
           tipo_acidente
    FROM tb_regional 
    GROUP BY tipo_acidente
    ORDER BY count(id) DESC limit 10