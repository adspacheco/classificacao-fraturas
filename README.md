# classificacao-fraturas
Modelo de Deep Learning para classificação de tipos de fraturas ósseas em imagens de raio-X

Problema: Construir um modelo de Deep Learning utilizando as técnicas aprendidas em aula para classificar os tipos de fraturas em ossos.

Dados: Pasta com os datasets: classificacao-imagem-tipos-fraturas-ossos-imagens-raio-x

## Geral

O conjunto de dados de imagem contém 10 diferentes tipos de fraturas

- Avulsion fracture
  - Fratura por entorse: um pedaço do osso duro se solta onde um ligamento ou tendão está preso, geralmente por um puxão forte em jovens ou por osteoporose em idosos.
- Comminuted fracture
  - Fraturas Cominutivas: fratura na qual o osso é estilhaçado ou esmagado em inúmeros pedaços.
- Fracture Dislocation
  - Fratura-Luxação: fratura perto de uma articulação, que também faz a articulação se deslocar.
- Greenstick fracture
  - Fratura em galho verde: osso quebra parcialmente, mas não se separa completamente, como um galho jovem e flexível.
- Hairline Fracture
  - Fratura por estresse: fratura fina no osso, como uma rachadura, mas o osso não se separa completamente.
- Impacted fracture
  - Fratura impactada: quando partes do osso quebrado se empurram uma contra a outra.
- Longitudinal fracture
  - Fratura longitudinal: osso quebra ao longo do seu comprimento.
- Oblique fracture
  - Fratura oblíqua: osso quebra em um ângulo.
- Pathological fracture
  - Fratura patológica: osso quebra devido a uma doença, como câncer ou osteoporose.
- Spiral Fracture
  - Fratura espiral: osso quebra em espiral ao redor do eixo do osso, geralmente por uma torção.


## Classificaçäo

### Fraturas Menos Graves
- Fratura por estresse (Hairline Fracture): fratura fina no osso, como uma rachadura, mas o osso não se separa completamente.
- Fratura em galho verde (Greenstick Fracture): osso quebra parcialmente, mas não se separa completamente, como um galho jovem e flexível.
- Fratura longitudinal (Longitudinal Fracture): osso quebra ao longo do seu comprimento.
- Fratura oblíqua (Oblique Fracture): osso quebra em um ângulo.
- Fratura impactada (Impacted Fracture): quando partes do osso quebrado se empurram uma contra a outra.

### Fraturas Moderadamente Graves
- Fratura por entorse (Avulsion Fracture): um pedaço do osso duro se solta onde um ligamento ou tendão está preso, geralmente por um puxão forte em jovens ou por osteoporose em idosos.
- Fratura espiral (Spiral Fracture): osso quebra em espiral ao redor do eixo do osso, geralmente por uma torção.
- Fratura-luxação (Fracture Dislocation): fratura perto de uma articulação, que também faz a articulação se deslocar.

### Fraturas Mais Graves
- Fraturas Cominutivas (Comminuted Fracture): fratura na qual o osso é estilhaçado ou esmagado em inúmeros pedaços.
- Fratura patológica (Pathological Fracture): osso quebra devido a uma doença, como câncer ou osteoporose.

## Total de Arquivos

- Avulsion fracture - Train: 109, Test: 14, Total: 123, Proportion Train: 88.62%, Proportion Test: 11.38%
- Comminuted fracture - Train: 134, Test: 14, Total: 148, Proportion Train: 90.54%, Proportion Test: 9.46%
- Fracture Dislocation - Train: 137, Test: 19, Total: 156, Proportion Train: 87.82%, Proportion Test: 12.18%
- Greenstick fracture - Train: 106, Test: 16, Total: 122, Proportion Train: 86.89%, Proportion Test: 13.11%
- Hairline Fracture - Train: 101, Test: 10, Total: 111, Proportion Train: 90.99%, Proportion Test: 9.01%
- Impacted fracture - Train: 75, Test: 9, Total: 84, Proportion Train: 89.29%, Proportion Test: 10.71%
- Longitudinal fracture - Train: 68, Test: 12, Total: 80, Proportion Train: 85.00%, Proportion Test: 15.00%
- Oblique fracture - Train: 69, Test: 16, Total: 85, Proportion Train: 81.18%, Proportion Test: 18.82%
- Pathological fracture - Train: 116, Test: 18, Total: 134, Proportion Train: 86.57%, Proportion Test: 13.43%
- Spiral Fracture - Train: 74, Test: 12, Total: 86, Proportion Train: 86.05%, Proportion Test: 13.95%

## Problema

### Premissa - Fratura Grave (Sim/Não)

#### Osso se separou do corpo ou não

### Fratura Não Grave
- Fratura por estresse (Hairline Fracture): fratura fina no osso, como uma rachadura, mas o osso não se separa completamente.
- Fratura em galho verde (Greenstick Fracture): osso quebra parcialmente, mas não se separa completamente, como um galho jovem e flexível.
- Fratura longitudinal (Longitudinal Fracture): osso quebra ao longo do seu comprimento.
- Fratura oblíqua (Oblique Fracture): osso quebra em um ângulo.
- Fratura impactada (Impacted Fracture): quando partes do osso quebrado se empurram uma contra a outra.
Total Menos Graves - Train: 419, Test: 63, Total: 482

### Fraturas Grave
- Fratura por entorse (Avulsion Fracture): um pedaço do osso duro se solta onde um ligamento ou tendão está preso, geralmente por um puxão forte em jovens ou por osteoporose em idosos.
- Fratura espiral (Spiral Fracture): osso quebra em espiral ao redor do eixo do osso, geralmente por uma torção.
- Fratura-luxação (Fracture Dislocation): fratura perto de uma articulação, que também faz a articulação se deslocar.
- Fraturas Cominutivas (Comminuted Fracture): fratura na qual o osso é estilhaçado ou esmagado em inúmeros pedaços.
- Fratura patológica (Pathological Fracture): osso quebra devido a uma doença, como câncer ou osteoporose.
Total Mais Graves - Train: 570, Test: 77, Total: 647

### Propostas

1) Identificar fratura grave (Sim/Não) - Binário

2) Dentro do grupo da fratura identificar qual tipo de fratura - multilabel
  - 3) Modelo para Não Grave (5 classes)
  - 4) Modelo para Grave (5 classes)
 
    - ou 5) Modelo multilabel com todas as classes (10 classes)

Avaliar métricas (acurácia, tempo de processamento) de cada modelo e justificar a escolha de um deles para utilização. Se 2 modelos multilabel para identificar o tipo entre não grave e grave. Ou 1 modelo para classificar o tipo de fratura dentre as 10 classes.

### Considerações do Professor

- Seguir apenas no binário grave sim/não
- Justificativa do "osso se separou do corpo ou não" está ok, no ponto de vista negocial
- Além disso, o objetivo da classificação é importante. Trazer notícias que embasem essa escolha também. P.ex, priorizar atendimento de fratura grave.
- Primeiro modelo multilabel com todas as fraturas para ter uma justificativa técnica também
  - Alguns tipos de fraturas vai ser possível verificar as métricas com dificuldade na classificação, p.ex.
- Classificar em grave ou não, com essas considerações de negócio e técnica, está ok. Classificar o tipo de fratura dentro do grave ou não é uma complexidade e entregar apenas se for como EXTRA.
