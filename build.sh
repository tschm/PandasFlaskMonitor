#!/bin/bash
FOLDER="$(cd "$(dirname "$0")" && pwd)"
rm -rf ${FOLDER}/env
conda create --yes -p ${FOLDER}/env python=3.4.3 flask=0.10.1 nose=1.3.7 pandas=0.16.2





