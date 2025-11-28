## Resumo Executivo e Técnico: Descarte Irregular de Lixo em Belém

O estudo socioeconômico e territorial dos bairros de Belém revela uma forte associação entre as condições de desenvolvimento humano e a ocorrência de Depósitos Irregulares de Entulho (DIEs). Os achados indicam que o descarte irregular de lixo está mais concentrado em áreas com menor desenvolvimento socioeconômico, sendo influenciado por fatores como o tamanho do bairro, o número de moradores e, principalmente, a renda e o Índice de Desenvolvimento Humano (IDH).

##  Principais Achados Técnicos

### 1. Indicadores de Descarte Irregular (DIEs)

* **Frequência de Coleta**: A média de dias de coleta é de 3.59 dias/semana (desvio-padrão de 1.27). No entanto, 71.83% dos bairros possuem coleta de 3 a 3.5 dias/semana, evidenciando que a maioria dos bairros tem coleta parcial (3 dias), enquanto apenas 19.72% têm coleta próxima a 6 dias.

* **Dispersão:** A quantidade estimada de Depósitos Irregulares de Entulho (DIEs) apresenta uma média de 4.37 por bairro (desvio-padrão de 2.33), com a maioria dos bairros registrando entre 3 e 5 DIEs (47.89% com 4 DIEs, e 22.54% com 6 DIEs). O valor máximo atinge 15 DIEs.

* **Quantidade Registrada (QTI):** A variável `QTI` (quantidade de Depósitos Irregulares registrados, para 21 observações) tem uma média de 3.81 e uma distribuição concentrada em valores baixos (42.86% com 2 QTI e 33.33% com 4 QTI)

### 2. Padrão Socioeconômico dos Bairros

* **Renda:** A renda média (`ren_avg`) é de R\$1,194.20, mas a mediana (`ren_mdn`) é significativamente menor(R\$698.88 ) indicando uma alta concentração de renda em valores mais baixos. A maior parte dos bairros (80.28%) tem uma renda mediana concentrada na faixa de   R\$605.00 ou menos.

* **População:** A distribuição populacional é desigual, com a maioria dos bairros (46.48%) tendo até 5,132 moradores (`Mor`). A média de Moradores por Habitação (`Mor/Hab`) é de 3.72, um indicador relativamente estável entre os bairros.

* **IDH:** varia significativamente, com bairros na faixa de IDH considerado médio (8.45% com 0.598 ou menos) e uma grande concentração nas faixas de 0.648 a 0.748 (cerca de 49%).

## Insights para o Descarte Irregular de Lixo

### 1. Influência da Renda e Desenvolvimento Humano (IDH)

Existe uma correlação negativa e estatisticamente significativa entre o descarte irregular e os indicadores de desenvolvimento e renda:

* `ren_avg` vs `QTI`: Bairros com maior renda média tendem a ter menos registros de descarte irregula ($r = -0.4406$). 
* `IDH` vs `QTI`: Bairros com melhor Índice de Desenvolvimento Humano (IDH) tendem a registrar menos descarte irregular ($r = -0.4399$).
* Correlação Geral (DIEs): Na matriz de correlação, a variável DIEs apresenta correlações negativas moderadas com a maioria dos indicadores de desenvolvimento, como `IDH` ($r = -0.477$), `IDH-E` ($r = -0.468$) e `ren_avg` ($r = -0.443$), reforçando a tese de que piores condições de vida estão associadas a maior descarte irregular.


### 2. Influência da Densidade e Tamanho do Bairro

As características territoriais e populacionais têm uma influência importante:

* Área (`area\_km2`) vs DIEs: Correlação positiva moderada de $r = 0.564$. Bairros maiores tendem a ter mais DIEs.
* População (`Mor`) vs DIEs (e QTI):
  * Mor vs DIEs: Correlação positiva fraca de $r = 0.175$
  * Mor vs QTI: Correlação positiva moderada de $r = 0.4847$ ($p < 0.05$). Isso sugere que bairros mais populosos (Mor) têm um número significativamente maior de registros de descarte irregular (QTI), indicando que a escala populacional é um fator de risco.
* Moradores por Habitação (`Mor/Hab`) vs DIEs: Correlação positiva moderada de $r = 0.420$. Bairros com mais moradores por residência tendem a ter mais DIEs.


### 3. Territórios maiores têm maior probabilidade de se tornarem áreas de abandono

A maior extensão territorial amplifica o risco de descarte irregular devido a três fatores inter-relacionados:
* **Áreas Não Fiscalizadas e de Baixa Cobertura:** A grande extensão territorial dos bairros acarreta um esforço logístico de fiscalização desproporcional, resultando na baixa frequência de monitoramento e na diminuição da percepção de risco pelos infratores, o que incentiva o descarte irregular em áreas isoladas.
* Espaços Vazios e Terrenos Baldios: A maior extensão territorial aumenta a disponibilidade de terrenos baldios e espaços vazios, que são percebidos como locais neutros e fora da vista para o descarte clandestino, e frequentemente desencadeiam um efeito contágio que acelera a degradação e o abandono.
* Trechos Periféricos de Difícil Acesso: A infraestrutura viária deficiente (ruas não pavimentadas e acessos estreitos) em áreas periféricas de bairros grandes impede a circulação eficiente dos caminhões de coleta e fiscalização, criando um ambiente de alta vulnerabilidade que favorece o descarte clandestino de diversos tipos de resíduos.

## Ações Estratégicas


### A. Fator Operacional: A Disparidade do Serviço

A infraestrutura de coleta desigual nas periferias funciona como um gatilho direto para o descarte.

**Síntese 1: Logística de Fiscalização Comprometida**
A grande extensão territorial dos bairros acarreta um esforço logístico de fiscalização desproporcional, resultando na baixa frequência de monitoramento e na diminuição da percepção de risco pelos infratores, o que incentiva o descarte irregular em áreas isoladas.

**Síntese 2: Acúmulo de Lixo**
A maior extensão territorial aumenta a disponibilidade de terrenos baldios e espaços vazios, que são percebidos como locais neutros e fora da vista para o descarte clandestino, e frequentemente desencadeiam um efeito contágio que acelera a degradação e o abandono.

**Síntese 3: Acesso Precário e Coleta Reduzida**
A infraestrutura viária deficiente (ruas não pavimentadas e acessos estreitos) em áreas periféricas de bairros grandes impede a circulação eficiente dos caminhões de coleta e fiscalização, criando um ambiente de alta vulnerabilidade que favorece o descarte clandestino de diversos tipos de resíduos.

**Impacto Direto da Frequência**
A correlação negativa estatisticamente significativa entre frequência de coleta ($r = -0.2557$) e DIEs confirma que a redução da frequência de coleta (prevalente nas periferias com 3 dias/semana) contribui diretamente para o aumento de Descarte Irregular de Resíduos.


### B. Fatores Territoriais e Demográficos: A Amplificação do Risco

O tamanho do bairro e sua densidade populacional amplificam a dificuldade de gestão.

**Bairros Maiores e Populosos:**
A correlação forte com a área ($\mathbf{r = 0.564}$) e a correlação moderada com o número de moradores ($r \approx 0.485$ para QTI) mostram que o problema é exacerbado em grandes aglomerados.

**Adensamento Residencial:**
O alto adensamento ($\text{Mor/Hab}: r = 0.420$) sugere que a falta de espaço para armazenamento doméstico contribui para o descarte em vias públicas.

### C. Fatores Socioeconômicos: A Raiz do Problema

A estratégia deve priorizar a alocação de recursos em áreas de vulnerabilidade, onde o problema é mais agudo.

**Prioridade na Renda e IDH Baixo:**
O descarte é significativamente maior em bairros com baixo IDH ($r \approx -0.477$) e baixa renda ($r \approx -0.443$).

**Foco na Renda Mediana:**
A maioria dos bairros (80.28%) tem renda mediana ($\text{ren\_mdn}$) de R$ 605,00 ou menos, indicando que a grande massa do problema está concentrada em bairros de baixa renda que carecem de infraestrutura de suporte.
