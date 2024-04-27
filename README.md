# Análise e Previsão vendas de uma farmacêuticas 
Neste projeto de uma indústria farmacêutica, a compreensão das tendências de mercado e dos padrões de consumo é essencial para garantir a oferta adequada de medicamentos e atender às necessidades da população. Neste estudo, exploramos um conjunto de dados abrangente de seis anos de vendas de medicamentos. Através de uma análise detalhada, buscamos identificar padrões de demanda, sazonalidades e correlações entre diferentes classes de medicamentos. Além disso, empregamos técnicas de previsão para estimar as vendas futuras, fornecendo insights valiosos para gestores da empresa.

Sobre o conjunto de dados
O conjunto de dados é construído a partir do conjunto de dados inicial, composto por dados transacionais coletados ao longo de 6 anos (período de 2014 a 2019), indicando data e hora da venda, nome da marca do medicamento farmacêutico e quantidade vendida, exportados do sistema de ponto de venda na farmácia individual. Um grupo selecionado de medicamentos do conjunto de dados (57 medicamentos) é classificado nas seguintes categorias do Sistema de Classificação Anatômica Terapêutica Química (ATC):

M01AB - Produtos anti-inflamatórios e antirreumáticos, não esteroides, derivados de ácido acético e substâncias relacionadas
M01AE - Produtos anti-inflamatórios e antirreumáticos, não esteroides, derivados de ácido propiônico
N02BA - Outros analgésicos e antipiréticos, ácido salicílico e derivados
N02BE/B - Outros analgésicos e antipiréticos, pirazolonas e anilidas
N05B - Medicamentos psicolepticos, medicamentos ansiolíticos
N05C - Medicamentos psicolepticos, medicamentos hipnóticos e sedativos
R03 - Medicamentos para doenças obstrutivas das vias aéreas
R06 - Antihistamínicos para uso sistêmico
Os dados de vendas são amostrados para os períodos horários, diários, semanais e mensais. Os dados já estão pré-processados, onde o processamento incluiu detecção e tratamento de outliers e imputação de dados ausentes.

# Nosso objetivo é avaliar a venda de diferentes medicamentos, de modo a conseguir capturar alguns insigths importantes como:                                         

1 Variação na Demanda de Medicamentos:

Durante o período de 2014 a 2019, observamos flutuações significativas na demanda por diferentes classes de medicamentos. Entre os produtos anti-inflamatórios e antirreumáticos (M01AB e M01AE), por exemplo, notamos um aumento consistente na procura, possivelmente devido ao envelhecimento da população e ao aumento das condições relacionadas à inflamação e doenças reumáticas. Por outro lado, classes como os medicamentos psicolepticos (N05B e N05C) apresentaram variações mais sutis, sugerindo uma demanda relativamente estável ao longo do período analisado.

2 Padrões Temporais de Vendas:

Ao analisar os padrões temporais de vendas, identificamos meses específicos que se destacaram pelo volume de vendas. Por exemplo, observamos picos de vendas de medicamentos para doenças obstrutivas das vias aéreas (R03) durante os meses de inverno, refletindo a sazonalidade das doenças respiratórias. Além disso, os meses de verão apresentaram uma demanda reduzida para medicamentos hipnóticos e sedativos (N05C), indicando uma possível diminuição do estresse e da ansiedade durante esse período.

3 Classificação de Medicamentos por Volume de Vendas:

Ao classificar as classes de medicamentos por volume de vendas mensais, pudemos identificar tendências interessantes. Por exemplo, os analgésicos e antipiréticos (N02BA e N02BE/B) foram consistentemente classificados entre os mais vendidos em todos os meses analisados, destacando a prevalência de dores e febres como queixas comuns entre a população.

4 Correlação entre Vendas de Medicamentos:

Ao explorar a correlação entre as vendas mensais de diferentes classes de medicamentos, encontramos algumas associações surpreendentes. Por exemplo, observamos uma correlação positiva entre as vendas de produtos anti-inflamatórios e antirreumáticos (M01AB e M01AE) e os medicamentos para doenças obstrutivas das vias aéreas (R03), sugerindo uma possível conexão entre condições inflamatórias e respiratórias.

5 Previsão de Vendas:

Utilizando técnicas de previsão, fomos capazes de estimar as vendas futuras de medicamentos com base em padrões históricos e tendências identificadas. Essas previsões fornecem informações cruciais para o planejamento estratégico de estoques, permitindo que as empresas se preparem adequadamente para atender à demanda dos consumidores de forma eficiente.

6 Prescrição da Análise:

Com base nos resultados obtidos, recomendamos uma abordagem holística para o gerenciamento de estoques e estratégias de marketing. Isso inclui a otimização da oferta de produtos mais demandados, a identificação de oportunidades de diversificação e o desenvolvimento de campanhas direcionadas para atender às necessidades específicas dos consumidores em diferentes períodos e regiões.





