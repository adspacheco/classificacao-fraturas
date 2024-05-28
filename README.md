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

- Avulsion fracture - Train: 109, Test: 14, Total: 123
- Comminuted fracture - Train: 134, Test: 14, Total: 148 
- Fracture Dislocation - Train: 137, Test: 19, Total: 156
- Greenstick fracture - Train: 106, Test: 16, Total: 122 
- Hairline Fracture - Train: 101, Test: 10, Total: 111   
- Impacted fracture - Train: 75, Test: 9, Total: 84      
- Longitudinal fracture - Train: 68, Test: 12, Total: 80 
- Oblique fracture - Train: 69, Test: 16, Total: 85
- Pathological fracture - Train: 116, Test: 18, Total: 134
- Spiral Fracture - Train: 74, Test: 12, Total: 86
