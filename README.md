
<div align="center">
  <h1>Análise e Previsão Vendas de uma Farmacêuticas</h1>
  <img src="https://github.com/weslei-silva87/Analise-Pevisao-vendas-farmaceutica/assets/163655532/e52ed809-2908-413d-95ea-3cd67b1237f4" alt="Design sem nome (4)" width="600">
</div>

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

<div align="center">
  <h1>Variação na Demanda de Medicamentos</h1>
  <img src="https://github.com/weslei-silva87/Analise-Pevisao-vendas-farmaceutica/assets/163655532/1d7820af-1429-4208-9f46-39b6e708abf6" alt="Indicadores 1 Todos Medicamentos">
</div>

Durante o período de 2014 a 2019, observamos flutuações significativas na demanda por diferentes classes de medicamentos. Entre os produtos anti-inflamatórios e antirreumáticos (M01AB e M01AE), por exemplo, notamos um aumento consistente na procura, possivelmente devido ao envelhecimento da população e ao aumento das condições relacionadas à inflamação e doenças reumáticas. Por outro lado, classes como os medicamentos psicolepticos (N05B e N05C) apresentaram variações mais sutis, sugerindo uma demanda relativamente estável ao longo do período analisado.

<div align="center">
  <h1>Medicamentos que Apresentaram aumento ou Diminuição de Demanda entre 2014 e 2019</h1>
  <img src="https://github.com/weslei-silva87/Analise-Pevisao-vendas-farmaceutica/assets/163655532/7f1afe61-0c7d-4c75-ba60-058d3e50905b" alt="Demanda 01">
</div>

As mudanças notáveis nas vendas de diversas classes de medicamentos. Em particular, destacamos o significativo crescimento nas vendas de medicamentos para doenças obstrutivas das vias aéreas (R03), com um aumento impressionante de 49,71%. Esse aumento substancial pode refletir uma maior incidência de condições respiratórias, bem como uma conscientização crescente sobre a importância do tratamento adequado dessas doenças.

Além disso, as vendas de antihistamínicos para uso sistêmico (R06) também apresentaram um crescimento significativo, com um aumento de 79,80% ao longo do período analisado. Esse aumento pode estar relacionado a uma maior demanda por tratamentos para alergias e condições respiratórias relacionadas.

Por outro lado, observamos uma queda acentuada nas vendas de medicamentos psicolepticos, como os medicamentos hipnóticos e sedativos (N05C), que diminuíram em 64,31%. Essa redução pode refletir uma mudança nas práticas de prescrição, uma maior conscientização sobre os riscos associados ao uso prolongado desses medicamentos e uma busca crescente por abordagens não farmacológicas para o tratamento de distúrbios do sono e ansiedade.

Além disso, as vendas de medicamentos ansiolíticos (N05B) e analgésicos e antipiréticos (N02BA) também diminuíram, com quedas de 25,96% e 24,38%, respectivamente. Essas reduções podem estar relacionadas a uma maior conscientização sobre o uso racional de medicamentos, políticas de prescrição mais restritas e uma mudança nas preferências dos pacientes em relação aos tratamentos.

Essas mudanças nas vendas de medicamentos refletem as tendências em evolução no setor farmacêutico e destacam a importância de monitorar de perto o mercado para garantir uma oferta adequada de medicamentos e promover o uso seguro e eficaz dos mesmos.


<div align="center">
  <h1>Padrões Temporais de Vendas</h1>
  <img src="https://github.com/weslei-silva87/Analise-Pevisao-vendas-farmaceutica/assets/163655532/fc4eceba-d1a7-49e8-9621-5eb7dd0ff87a" alt="Vendas ao Longo do Tempo">
</div>

A sazonalidade influencia significativamente a dinâmica do mercado farmacêutico. Durante o período analisado, observamos claramente quais meses em períodos de maior e menor demanda por medicamentos, fornecendo insights valiosos para gestores.

Os meses de outubro e dezembro destacam-se como períodos de alta demanda, caracterizados por um aumento significativo nas vendas. O mês de outubro, consistentemente ao longo dos anos, registra um pico de vendas, indicando uma sazonalidade relacionada ao aumento de doenças respiratórias e alérgicas durante o período de transição para as estações mais frias. Da mesma forma, dezembro emerge como um mês de destaque, particularmente devido às festas de fim de ano, que podem influenciar o aumento da procura por medicamentos.

Por outro lado, meses como julho e junho surgem como períodos de menor demanda por medicamentos. Julho, frequentemente associado às férias de meio de ano, registra uma diminuição na procura, refletindo possíveis mudanças no comportamento do consumidor durante esse período. Junho também pode apresentar vendas mais baixas, sugerindo variações sazonais ou outros fatores externos que afetam a demanda por medicamentos.

# 3 Classificação de Medicamentos por Volume de Vendas:

Ao classificar as classes de medicamentos por volume de vendas mensais, pudemos identificar tendências interessantes. Por exemplo, os analgésicos e antipiréticos (N02BA e N02BE/B) foram consistentemente classificados entre os mais vendidos em todos os meses analisados, destacando a prevalência de dores e febres como queixas comuns entre a população.

# 4 Correlação entre Vendas de Medicamentos:

Ao explorar a correlação entre as vendas mensais de diferentes classes de medicamentos, encontramos algumas associações surpreendentes. Por exemplo, observamos uma correlação positiva entre as vendas de produtos anti-inflamatórios e antirreumáticos (M01AB e M01AE) e os medicamentos para doenças obstrutivas das vias aéreas (R03), sugerindo uma possível conexão entre condições inflamatórias e respiratórias.

# 5 Previsão de Vendas:

Utilizando técnicas de previsão, fomos capazes de estimar as vendas futuras de medicamentos com base em padrões históricos e tendências identificadas. Essas previsões fornecem informações cruciais para o planejamento estratégico de estoques, permitindo que as empresas se preparem adequadamente para atender à demanda dos consumidores de forma eficiente.

# 6 Prescrição da Análise:

Com base nos resultados obtidos, recomendamos uma abordagem holística para o gerenciamento de estoques e estratégias de marketing. Isso inclui a otimização da oferta de produtos mais demandados, a identificação de oportunidades de diversificação e o desenvolvimento de campanhas direcionadas para atender às necessidades específicas dos consumidores em diferentes períodos e regiões. 

# Conclusão
Este portfólio representa uma análise abrangente e detalhada das vendas de medicamentos ao longo de seis anos, fornecendo informações valiosas para stakeholders do setor farmacêutico. As conclusões e recomendações apresentadas têm o potencial de direcionar estratégias e decisões, contribuindo para o crescimento e sucesso das organizações neste mercado dinâmico e competitivo.





