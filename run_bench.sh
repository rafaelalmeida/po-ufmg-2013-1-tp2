#!/bin/bash

python instance_generator.py 10 10 > instancias/bench.data
glpsol --model restaurantes.mod --data instancias/bench.data --output 
/dev/null | grep "[Time|Memory] used"
