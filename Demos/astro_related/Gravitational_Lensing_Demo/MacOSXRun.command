#!/bin/bash

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

cd "$dir"

ipython notebook ./gravitational_lensing.ipynb 


