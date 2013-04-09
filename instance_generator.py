# -*- coding: utf8 -*-

import sys
import random

# semente gerada aleatoriamente
SEED = 14594637

FAIXA_PRECOS_PERUS = (5, 20)
FAIXA_PRECOS_PRATOS = (3, 15)
FAIXA_DEMANDAS = (10, 50)
FAIXA_QUANTIDADE_CARNE_ESCURA = (2, 7)
FAIXA_QUANTIDADE_CARNE_CLARA = (2, 7)
FAIXA_PERCENTUAL_CARNE_CLARA = (0.0, 1.0)

def main(args):
	if len(args) != 3:
		print "Usage: python %s NUMERO_PRATOS NUMERO_TIPOS_PERUS" % args[0]
		exit()

	n_pratos, n_perus = int(args[1]), int(args[2])
	instance = ""

	# gera o set de pratos
	instance += generate_param(
		"set Pratos", 
		["Prato%d" % i for i in range(n_pratos)], 
		single_line=True)

	# gera o set de perus
	instance += generate_param(
		"set TiposDePeru", 
		["Tipo%d" % i for i in range(n_perus)], 
		single_line=True)

	# gera as demandas dos pratos
	instance += generate_param(
		"param Demanda", 
		["Prato%d %d" % (i, random.randint(*FAIXA_DEMANDAS)) 
			for i in range(n_pratos)])

	# gera os preços de venda dos pratos
	instance += generate_param(
		"param PrecoDeVenda", 
		["Prato%d %d" % (i, random.randint(*FAIXA_PRECOS_PRATOS)) 
			for i in range(n_pratos)])

	# gera os preços dos perus
	instance += generate_param(
		"param PrecoDosPerus", 
		["Tipo%d %d" % (i, random.randint(*FAIXA_PRECOS_PERUS)) 
			for i in range(n_perus)])

	# gera as quantidades de carne clara dos perus
	instance += generate_param(
		"param QuantidadeDeCarneClaraPorPeru", 
		["Tipo%d %d" % (i, random.randint(*FAIXA_QUANTIDADE_CARNE_CLARA)) 
			for i in range(n_perus)])

	# gera as quantidades de carne escura dos perus
	instance += generate_param(
		"param QuantidadeDeCarneEscuraPorPeru", 
		["Tipo%d %d" % (i, random.randint(*FAIXA_QUANTIDADE_CARNE_ESCURA)) 
			for i in range(n_perus)])

	# gera os percentuais mínimos de carne clara nos pratos
	instance += generate_param(
		"param PercentualMinimoDeCarneClara", 
		["Prato%d %.1f" % (i, random.uniform(*FAIXA_PERCENTUAL_CARNE_CLARA)) 
			for i in range(n_pratos)])

	# imprime a instância gerada
	print instance

def generate_param(prefix, items, single_line=False):
	lb = "\n" if not single_line else ""
	lbi = "\n" if not single_line else " "
	if not single_line: items = ["\t%s" % i for i in items]

	out = [prefix, " := ", lb, lbi.join(items), ";", "\n\n"]
	return "".join(out)

if __name__ == '__main__':
	main(sys.argv)
