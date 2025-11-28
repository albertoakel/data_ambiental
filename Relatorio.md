## Resumo Executivo e Técnico: Descarte Irregular de Lixo em Belém

O estudo socioeconômico e territorial dos bairros de Belém revela uma forte associação entre as condições de desenvolvimento humano e a ocorrência de Depósitos Irregulares de Entulho (DIEs). A análise indica que o descarte irregular está concentrado em áreas de menor desenvolvimento socioeconômico, sendo influenciado por um conjunto de fatores que incluem o tamanho do bairro, a densidade populacional e, de forma mais crítica, a renda e o Índice de Desenvolvimento Humano (IDH).

## Análise Descritiva e Estatística dos Fatores Determinantes

### 1. Indicadores Operacionais e a Realidade da Coleta

O panorama do descarte irregular em Belém é caracterizado por uma coleta de lixo insuficiente e uma dispersão significativa de pontos de descarte A frequência média de coleta é de 3,59 dias/semana, sendo que a grande maioria dos bairros (71,83%) possui um serviço parcial, entre 3 e 3,5 dias. Em paralelo, a quantidade de Depósitos Irregulares de Entulho (DIEs) apresenta uma média de 4,37 por bairro, com a maior parte deles registrando entre 3 e 5 pontos. A variável de Quantidade Registrada (QTI), com média de 3,81, confirma a concentração em valores baixos, porém generalizados. A **figura** 1 apresenta o mapa por dias da semana para coleta de lixo.

![Figura 1](image/folium_mapa.png)

**Figura 1:** Mapa dos setores de coleta de lixo em Belém. Em verde 6 dias na semana. Em Amarelo 3 dias na semana. 

### 2.Padrão Socioeconômico: A Raiz do Problema

O tecido social de Belém é marcado por significativa desigualdade. A renda média da cidade é de R$ 1.194,20, mas a renda mediana é drasticamente menor, de R$ 698,88, um sinal claro da concentração de renda em patamares baixos. Com efeito, 80,28% dos bairros têm uma renda mediana de R$ 605,00 ou menos. A distribuição populacional também é desigual, com quase metade dos bairros (46,48%) abrigando até 5.132 moradores. O Índice de Desenvolvimento Humano (IDH) varia, com a maior parte dos bairros (cerca de 49%) concentrando-se em faixas consideradas médias. Figura 2 

![Figura 2](/home/akel/PycharmProjects/Data_ambiental/image/Mapa_bairro_ren_mdn.png)

**Figura 2:**

## Insights para o Descarte Irregular de Lixo

### A Influência Crítica da Renda e do Desenvolvimento Humano

Existe uma relação clara e estatisticamente significativa entre a prosperidade de um bairro e a ocorrência de descarte irregular. Bairros com maior renda média e melhor IDH tendem a registrar menos descarte irregular. Esta correlação negativa é evidenciada pelos coeficientes de `ren_avg` vs `QTI` ($r = -0,4406$) e `IDH` vs `QTI` ($r = -0,4399$). De forma mais ampla, a variável DIEs correlaciona-se negativamente com `IDH` ($r = -0,477$) e `ren_avg` ($r = -0,443$), reforçando que piores condições de vida estão intrinsecamente ligadas a maiores índices do problema. 

![Figura 3](/home/akel/PycharmProjects/Data_ambiental/image/IDH_QTI.png.png)**Figura 3**: Relação entre Moradores, renda média, e IDH com QTI( Quantidade de Depósitos Irregulares)

### O Efeito Amplificador do Território e da Densidade Populacional

As características físicas e demográficas dos bairros atuam como um catalisador para o descarte irregular. Bairros com maior extensão territorial (`area_km2`) apresentam uma correlação positiva moderada ($r = 0,564$) com a existência de mais DIEs. O tamanho da população também é um fator de risco, com uma correlação positiva moderada entre `Mor` e `QTI` ($r = 0,4847$). Ademais, o adensamento residencial, medido por Moradores por Habitação (`Mor/Hab`), também mostra uma correlação positiva ($r = 0,420$), sugerindo que a falta de espaço para armazenamento doméstico contribui para o descarte em vias públicas.

![Figura 4](/home/akel/PycharmProjects/Data_ambiental/image/Figura4.png)

**Figura 4**: Relação entre Area[km2], moradores/Habitantes e moradores com renda com QTI( Quantidade de Depósitos Irregulares)

### A Dinâmica do Abandono em Territórios Expansivos

A maior extensão territorial cria um ambiente propício para o descarte irregular devido a uma combinação de fatores. A logística de fiscalização torna-se desproporcional, resultando em baixa frequência de monitoramento e reduzida percepção de risco. Simultaneamente, a maior disponibilidade de terrenos baldios e espaços vaziosé percebida como uma oportunidade para o descarte clandestino, iniciando um "efeito contágio" de degradação. Este cenário é agravado pela infraestrutura viária deficiente em áreas periféricas de bairros grandes, que impede a circulação eficiente de caminhões de coleta e veículos de fiscalização, criando zonas de alta vulnerabilidade.

## Ações Estratégicas e Recomendações

### Enfrentando a Disparidade do Serviço de Coleta

A infraestrutura operacional desigual funciona como um gatilho direto para o descarte. A confirmação estatística de que uma menor frequência de coleta correlaciona-se com mais DIEs ($r = -0,2557$) sublinha a necessidade urgente de reestruturar o serviço. A solução passa por aumentar a frequência de coleta nos bairros periféricos de alta vulnerabilidade, equiparando-a ao padrão das áreas centrais.

![Figura 5](/home/akel/PycharmProjects/Data_ambiental/image/figura5.png)

**Figura 5**: Número de dias médios de coleta de lixo.

### Mitigando os Riscos Territoriais e Demográficos

Para combater o efeito amplificador do tamanho e da densidade, a gestão deve ser inteligente e focalizada. É crucial utilizar os dados de área (`area_km2`) e população (`Mor`) para direcionar a fiscalização e o monitoramento de forma proativa, especialmente em bairros maiores e mais populosos, contendo assim o efeito contágio em terrenos baldios.

### Atacando a Raiz Socioeconômica do Problema

A estratégia final e mais fundamental deve priorizar a alocação de recursos onde o problema é mais agudo. Dado que o descarte é significativamente maior em bairros com baixo IDH ($r \approx -0,477$) e baixa renda ($r \approx -0,443$), e que a maioria dos bairros tem renda mediana igual ou inferior a R$ 605,00, as políticas públicas devem ser canalizadas para estas áreas de vulnerabilidade, onde a carência de infraestrutura de suporte é mais crítica.

As políticas de intervenção devem, portanto, ser integradas e georreferenciadas, atacando de forma simultânea os fatores sociais, territoriais e operacionais para um resultado efetivo e duradouro.



