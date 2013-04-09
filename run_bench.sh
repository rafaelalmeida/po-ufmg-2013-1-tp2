#!/bin/bash

glpsol --model restaurantes.mod --data bench.data --output /dev/null | grep "[Time|Memory] used"