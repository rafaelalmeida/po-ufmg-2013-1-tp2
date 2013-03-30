# Declara os conjuntos do problema.
set Pratos;
set TiposDePeru;

# Declara variáveis
var KgsDeCarneClara{Pratos} >= 0;
var KgsDeCarneEscura{Pratos} >= 0;
var QuantidadeDePerusComprados{TiposDePeru} >= 0;

# Declara parâmetros
param Demanda{Pratos} >= 0;
param PrecoDeVenda{Pratos} >= 0;
param PrecoDosPerus{TiposDePeru} >= 0;
param QuantidadeDeCarneClaraPorPeru{TiposDePeru} >= 0;
param QuantidadeDeCarneEscuraPorPeru{TiposDePeru} >= 0;
param PercentualMinimoDeCarneClara{Pratos} >= 0;

# Função objetivo
maximize Lucro: 
	(sum {p in Pratos} 
		(KgsDeCarneClara[p] + KgsDeCarneEscura[p]) * PrecoDeVenda[p])
	-
	(sum {p in Perus} PrecoDosPerus[p])

# Restrição de demanda dos pratos
s.t. RestricaoDeDemanda{p in Pratos}:
	KgsDeCarneClara[p] + KgsDeCarneEscura[p] <= Demanda[p]

# Restrição que relaciona a quantidade de carne clara utilizada à quantidade de 
# perus comprados
s.t. RestricaoDeUtilizacaoDeCarneClara:
	sum {p in Pratos} KgsDeCarneClara[p] 
	<= 
	sum {p in Perus} QuantidadeDeCarneClaraPorPeru[p]

# Restrição análoga, para carne escura
s.t. RestricaoDeUtilizacaoDeCarneEscura:
	sum {p in Pratos} KgsDeCarneEscura[p] 
	<= 
	sum {p in Perus} QuantidadeDeCarneEscuraPorPeru[p]

# Restrição de proporcionalidade das carnes
s.t. RestricaoDeProporcionalidade{p in Pratos}:
	KgsDeCarneClara[p] / (KgsDeCarneClara[p] + KgsDeCarneEscura[p]) 
	>= 
	PercentualMinimoDeCarneClara[p]
