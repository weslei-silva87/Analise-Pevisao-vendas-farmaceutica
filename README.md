# Previsão vendas de uma farmacêuticas

Sobre o conjunto de dados
O conjunto de dados é construído a partir do conjunto de dados inicial, composto por 600.000 dados transacionais coletados ao longo de 6 anos (período de 2014 a 2019), indicando data e hora da venda, nome da marca do medicamento farmacêutico e quantidade vendida, exportados do sistema de ponto de venda na farmácia individual. Um grupo selecionado de medicamentos do conjunto de dados (57 medicamentos) é classificado nas seguintes categorias do Sistema de Classificação Anatômica Terapêutica Química (ATC):

M01AB - Produtos anti-inflamatórios e antirreumáticos, não esteroides, derivados de ácido acético e substâncias relacionadas
M01AE - Produtos anti-inflamatórios e antirreumáticos, não esteroides, derivados de ácido propiônico
N02BA - Outros analgésicos e antipiréticos, ácido salicílico e derivados
N02BE/B - Outros analgésicos e antipiréticos, pirazolonas e anilidas
N05B - Medicamentos psicolepticos, medicamentos ansiolíticos
N05C - Medicamentos psicolepticos, medicamentos hipnóticos e sedativos
R03 - Medicamentos para doenças obstrutivas das vias aéreas
R06 - Antihistamínicos para uso sistêmico
Os dados de vendas são amostrados para os períodos horários, diários, semanais e mensais. Os dados já estão pré-processados, onde o processamento incluiu detecção e tratamento de outliers e imputação de dados ausentes.


Nosso objetivo é avaliar a venda de diferentes medicamentos, de modo a conseguir capturar alguns insigths importantes como:
1) Quais classes de medicamentos apresentaram aumento ou diminuição de demanda entre 2014 e 2019?
2) Quais os meses com mais e menos vendas?
3) Quais as classes de medicamentos mais e menos vendidos por mês?¶
4) Existe correlação entre a venda mensal de determinadas classes de medicamentos?
5) Relizar previsão de vendas dos medicamenos
6) Realizar prescrição da analise
