# Segundo trabalho de Pesquisa Operacional (2013-1)

Este trabalho usa um solver para resolver algumas instâncias de um problema
proposto.

Utilizamos o solver GLPK (pacote `glpk` no APT). Para rodar a instância
do enunciado, utilize o seguinte comando:

```
./run_example.sh
```

Para rodar os experimentos e gerar os gráficos, são necessários o Python
e o GNU Plot. Os gráficos foram gerados no Microsoft Excel. Para rodar a suíte
de testes e gerar os resultados de desempenho na pasta `/experiments` em CSV,
utilize o seguinte comando:

```
python run_experiments.py
```