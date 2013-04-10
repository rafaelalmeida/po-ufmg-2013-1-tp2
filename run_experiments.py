# -*- coding: utf8 -*-

import sys
import subprocess
import re

RANGE_NUM_PRATOS = (2, 10000)
RANGE_NUM_PERUS = (2, 10000)
INCREMENT = 100
NUMBER_OF_RUNS = 3

def main(args):
    min_pratos = RANGE_NUM_PRATOS[0]
    min_perus = RANGE_NUM_PERUS[0]

    # testa variando o número de pratos
    outfile = open("experiments/pratos.csv", "w")
    for p in range(0, RANGE_NUM_PRATOS[1] + INCREMENT, INCREMENT):
        # calcula parâmetros da instância
        n_pratos = max(p, min_pratos)
        n_perus = min_perus

        # imprime progresso
        print "Rodando para %d pratos e %d perus" % (n_pratos, n_perus)

        # roda instâncias
        results = [run_random_instance(n_pratos, n_perus) 
                   for j in range(NUMBER_OF_RUNS)]
            
        # tira média das instâncias e escreve resultados
        media = [sum(y) / len(y) for y in zip(*results)]
        outfile.write(",".join(map(str, [n_pratos] + media)) + "\n")
    outfile.close()

    # testa variando o número de perus
    outfile = open("experiments/perus.csv", "w")
    for p in range(0, RANGE_NUM_PERUS[1] + INCREMENT, INCREMENT):
        # calcula parâmetros da instância
        n_pratos = min_pratos
        n_perus = max(p, min_perus)

        # imprime progresso
        print "Rodando para %d pratos e %d perus" % (n_pratos, n_perus)

        # roda instâncias
        results = [run_random_instance(n_pratos, n_perus) 
                   for j in range(NUMBER_OF_RUNS)]
            
        # tira média das instâncias e escreve resultados
        media = [sum(y) / len(y) for y in zip(*results)]
        outfile.write(",".join(map(str, [n_perus] + media)) + "\n")
    outfile.close()


def run_random_instance(n_pratos, n_perus):
    out = subprocess.check_output("python instance_generator.py %d %d | "
        "glpsol --model restaurante.mod --data /dev/stdin --output /dev/null" 
        % (n_pratos, n_perus), shell=True)

    time = float(re.search(r"Time used:\ +(\d+\.\d+)", out).group(1))
    memory = int(re.search(r"Memory used:.*\((\d+)", out).group(1))
    return (time, memory)

if __name__ == '__main__':
    main(sys.argv)