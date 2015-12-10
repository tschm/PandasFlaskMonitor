#!/bin/bash
git checkout master
git pull
git checkout $1
./build.sh
./test.sh
