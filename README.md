# Projeto individual - Módulo 4 (SENAC/Resilia)<br>

Projeto: <br>
**Relatórios semanais.**  <br>

Aluno: <br>
**Matheus Augusto de Souza.** <br>

e-mail para contato: <br>
**mataugusto1999@gmail.com** <br>

<br><br>
- Apresentação do problema: <br>
Uma loja deseja produzir relatórios
semanais com ganhos e despesas. O gerente da
loja me contratou para gerar um relatório de uma
semana e, após isso, mostrar ao dono da loja como a
análise dos dados pode ser útil para o negócio. Para
isso, ele me enviou uma tabela de exemplo das
despesas de uma semana:
<br>

![tabela projeto individual.png](https://github.com/mattaugustt/projeto-individual-mod.-4/blob/main/tabela%20inicial.png)

<br>
Além disso, ele também me informou que os ganhos não estão nessa planilha, mas que ele
possui a seguinte lista: 2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893
respectivos aos dias da semana. Ele deixou que eu tome liberdade para incluir no relatório as
estatísticas que eu desejar, mas ele deseja que o relatório contenha outros dados que estão representados nas queries mais abaixo. <br><br>


- O que foi feito?
1. A criação do Data-Frame com a tabela enviada pela loja.<br>
2. A adição de uma coluna no data-frame com os ganhos diários informados pela loja.<br>
3. Após a criação e incrementação do data-frame, fiz a análise dos dias com ganhos acima de 4 mil e dias com ganhos abaixo de 4 mil.<br>
4. Comecei a responder as queries exigidas pelo gerente.<br>
<br><br>


# Respostas obtidas para cada query e como foram feitas:
<br>

**Minhas análises:**  <br>

1. Dias da semana com ganhos inferiores à 4 mil: <br>
```
df.query('Ganhos < 4000') <br><br>
```
Retorna as linhas dos dias: Segunda, Terça, Quarta e Domingo.<br><br>

2. Dias da semana com ganhos superiores à 4 mil: <br>
```
df.query('Ganhos > 4000') <br><br>
```
Retorna as linhas dos dias: Quinta, Sexta e Sábado. <br><br>

**QUERY 1:**
<br>
A subtração de impostos dos ganhos diários, que nesta semana foi de 7%.
<br>
Primeiro fiz a conversão de quanto vale 7% para cada dia da semana e, após isso, fiz a diferença do ganho diário com o valor de impostos diários. Depois de calcular os valores reajustados, de cada dia da semana, adicionei uma nova coluna com os mesmos, denominada "Reajustado (0,7%)".
<br><br>

**QUERY 2:**
<br>
A soma total dos ganhos.
Utilizei a função '.sum()' para fazer a soma dos valores da semana inteira, tanto para os valores sem reajuste ('Ganhos') quanto pros valores reajustados ('Reajustado (0,7%)').<br>
<br>Como foi utilizada a função: <br>
```
df['Ganhos'].sum()   #-> sem o reajuste
df['Reajustado (0,7%)'].sum()   #-> com o reajuste
```
Resultados obtidos:<br>
1. 26325.0
2. 24482.25
<br><br>

**QUERY 3:**<br>
A média semanal dos ganhos.<br>
O processo foi semelhante com o da soma, mudando apenas a função utilizada. Neste caso, utilizamos a função '.mean()' que retorna a média. Apliquei também para as duas colunas: 'Ganhos' e 'Reajustado (0,7%)'.<br>
```
df['Ganhos'].mean()   #-> média dos ganhos semanal sem reajuste
df['Reajustado'].mean()   #-> média dos ganhos semanal com reajuste
```
Resultados obtidos: <br>
1. 3760.714285714286
2. 3497.464285714286
<br><br>

**QUERY 4:**<br>
A soma total das despesas por categoria.<br>
Primeiramente fiz a soma de cada categoria indivualmente, com a função '.sum()', onde as seguintes variaveis indicam cada categoria: <br>
l - Limpeza; (400) <br>
c - Comida; (2324.64)<br> 
t - Transporte; (1550) <br> 
o - Outros. (3630)<br> 
w - Total. (7904.639999999999)<br>

E, no fim, fiz a soma de todas elas ('w') e retornei a mesma. <br><br>

**QUERY 5:**<br>
A média semanal de todas as despesas.<br>
De forma similar com a query anterior, apliquei a função de média '.mean()' para cada uma das despesas e depois somei todas estas, resultando numa média geral (total).<br>
l - Limpeza; (57.142857142857146) <br>
c - Comida; (332.09142857142854)<br> 
t - Transporte; (221.42857142857142) <br> 
o - Outros. (518.5714285714286)<br> 
w - Total. (1129.2342857142858)<br>
<br>
A variável 'w' é o total da soma das médias.<br><br>

**QUERY 6:**<br>
O lucro diário para informar qual dia foi mais lucrativo e o lucro total da semana.<br>
Para esse query eu fiz a soma dos gastos diários e após isso fiz a subtração dos valores de ganhos diários reajustados ('Reajustado (0,7%)') com o total dos gastos diários.<br>
Após isso, criei uma nova coluna denominada 'Lucro diário' para a adição dos valores na tabela. <br>
```
df['Lucro diário'] = g-r    #-> g = ganho diário reajustado; r = gasto diário.
```
<br>
Após isso, basta utilizar-mos a função '.max()' na coluna de 'Lucro diário' para obter-mos o maior lucro diário da semana. <br>

```
df['Lucro diário'].max()  
```
<br>
O valor que nos é retornado é: <br>
3769.075
<br><br>
Para sabermos o dia da semana em que esse valor foi alcançado, basta buscarmos a linha através da função 'loc'.<br>

```
x = df['Lucro diário'].max()  #valor máximo
df.loc[df['Lucro diário'] == x]    #imprime a linha com o maior valor de lucro diário
```
<br>

**Resultado obtido (linha obtida):**
<br>
- Dia: Sexta <br>
- Limpeza: 100  <br>
- Comida: 411.53 <br>
- Transporte: 275   <br>
- Outros: 0  <br>
- Ganhos: 4898.5 <br>
- Reajustado (0,7%): 4555.605    <br>
- Gasto diário: 786.53  <br>
- Lucro diário: 3769.075  <br>
<br><br>

- Tabela final com os dados que julgo necessários estarem na planilha: <br>
![Tabela Final](https://github.com/mattaugustt/projeto-individual-mod.-4/blob/main/tabela%20final.png)
