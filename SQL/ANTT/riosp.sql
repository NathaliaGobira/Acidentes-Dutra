CREATE TABLE IF NOT EXISTS acidentes_riosp_limpo AS

SELECT *,
       CASE 
            WHEN mortos > 0 AND tipo_de_acidente LIKE '%pedestre%'  
            THEN 'AT01_P - Vitimas'

            WHEN (mortos + levemente_feridos + moderadamente_feridos + gravemente_feridos) > 0
                AND tipo_de_acidente LIKE '%animal%' THEN 'AT01_A - Vitimas'
            
            WHEN mortos > 0 THEN 'AC01 - Vitimas'    
            
            WHEN (levemente_feridos + moderadamente_feridos + gravemente_feridos) > 0 AND tipo_de_acidente LIKE '%pedestre%' 
            THEN 'AT02_P - Feridos'
            
            WHEN (mortos + levemente_feridos + moderadamente_feridos + gravemente_feridos) = 0
                 AND tipo_de_acidente LIKE '%animal%' THEN 'AT02_A - Ilesos'     
            
            WHEN (levemente_feridos + moderadamente_feridos + gravemente_feridos) > 0 THEN 'AC02 - Feridos'
            
            ELSE 'AC03 - Ilesos'
       
       END AS categoria_ocorrencia,
       CASE
            WHEN sentido IN ('Norte', 'Pista Norte', 'Decrescente') THEN 'Norte'
            WHEN sentido IN ('Sul', 'Pista Sul', 'Crescente') THEN 'Sul'
            ELSE 'a verificar'
       END AS sentido_padronizado
       
FROM acidentes_riosp
WHERE trecho LIKE 'BR-116%'
